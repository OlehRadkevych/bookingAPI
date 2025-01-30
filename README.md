# Booking API Test Automation Framework

## Project Overview
This project is designed for learning **Python Test Automation** using the public API [Restful Booker API](https://restful-booker.herokuapp.com/apidoc/index.html). The framework is built using **pytest and requests** to validate API functionality efficiently.

## Features
- **Automated API Testing** using `pytest`
- **Dynamic Test Data Generation** with `faker`
- **Environment Configuration Management** using `dotenv`
- **Reusable API Client** to handle API interactions
- **Pytest Fixtures** for better test setup and teardown

## Technologies Used
- **Python 3.12**
- **pytest** (for test execution)
- **requests** (for API interactions)
- **Faker** (for generating test data)
- **Dotenv** (for managing environment variables)

## Project Structure
```
bookingAPI/
│── tests/               # Test cases
│   │── test_health_check.py
│   │── test_create_booking.py
│   │── test_update_booking.py
│   │── test_delete_booking.py
│── utils/               # Utility modules
│   │── api_client.py
│   │── user_booking.py
│── config.py            # Configuration file (Dataclass with Env variables)
│── conftest.py          # Pytest fixtures
│── requirements.txt     # Required dependencies
│── README.md            # Project documentation
```

## Future Improvements
- Add **Logging** for enhanced debugging and reporting
- Implement **parallel test execution** for performance optimization
- Integrate **CI/CD pipeline** for automated test execution
- Add **Allure Reporting** for better test visualization

