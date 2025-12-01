# Booking API Test Automation Framework

## Project Overview
This repository contains automated tests for the public [Restful Booker API](https://restful-booker.herokuapp.com/apidoc/index.html). The suite focuses on creating, retrieving, updating, and partially updating bookings, plus basic health and lookup checks, using `pytest` and `requests`.

## Key Features
- Authenticated API client with Basic auth credentials read from environment variables.
- Faker-powered booking data generator for dynamic payloads and negative test cases.
- Pytest fixtures for authenticated sessions, booking lifecycle management, and optional HTML report generation.
- Schema-based validation for booking retrieval responses.
- Parameterized tests covering invalid names, booking dates, and pricing scenarios.

## Project Structure
```
bookingAPI/
├── config.py              # Default base URL and credentials loaded from environment variables
├── requirements.txt       # Test dependencies
├── utils/
│   ├── api_client.py      # Authenticated HTTP client wrapper
│   └── booking.py         # Booking data factory and helper methods
├── tests/
│   ├── conftest.py        # Shared fixtures (API client, booking factory, report hook)
│   ├── data/              # Reusable invalid data matrices
│   ├── test_HealthCheck_API.py
│   ├── test_GetBookingIds_API.py
│   ├── test_GetBooking_API.py
│   ├── test_CreateBooking_API.py
│   ├── test_UpdateBooking_API.py
│   └── test_PartialUpdateBooking_API.py
└── README.md
```

## Setup
1. Ensure Python 3.12+ is available.
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
Environment variables can override defaults in `config.py`:
- `BASE_URL` – API host.
- `_USER` – Username for authentication.
- `PASSWORD` – Password for authentication .
- `AUTH_TOKEN` – Base64-encoded Basic auth token.

## Running Tests
Follow these steps from the repository root:

1. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
2. Run the test suite with `PYTHONPATH` set:
   ```bash
   PYTHONPATH=. pytest
   ```

The `api_client` fixture authenticates once per module before issuing requests. The `create_booking` fixture provisions a booking for tests that require an existing record and cleans it up afterward.

### HTML Report (optional)
A session-scoped `generate_report` fixture triggers a secondary pytest run with `--html=<file>` after the suite finishes. Install `pytest-html` if you want this report to succeed:
```bash
pip install pytest-html
```
Generated reports are saved under `reports/` with a 'reports' filename.

## What the Tests Cover
- **Health check:** `/ping` returns 201.
- **Booking lookup:** `/booking` list retrieval and filtering by first name, last name, check-in, and check-out dates.
- **Booking details:** `/booking/{id}` returns a schema-valid booking for existing IDs and 404 when missing.
- **Create booking:** happy-path creation plus invalid names, prices, and date combinations.
- **Update booking (PUT):** full updates with valid data and validation of invalid names, dates, prices, and malformed payloads.
- **Partial update (PATCH):** firstname/lastname updates and validation against invalid names, dates, prices, or null fields.

## Additional Notes
- The API client raises an exception if authentication fails; ensure credentials are valid before running tests.
- Faker-generated data means payloads differ per run, which helps surface edge cases.