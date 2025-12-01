INVALID_BOOKINGDATES = [
    None,
    {"checkin": "2025-12-02", "checkout": "2025-12-01"},
    {"checkin": "2025-12-01", "checkout": "2025-12-01"},
    {"checkin": "", "checkout": "2019-01-01"},
    {"checkin": "2018-01-01", "checkout": ""},
    {"checkin": "01-01-2018", "checkout": "2019/01/01"},
    {"checkin": "2018.01.01", "checkout": "2019.01.01"},
]

INVALID_BOOKINGDATES_IDS = [
    "missing_bookingdates",
    "checkout_before_checkin",
    "same_day_booking",
    "missing_checkin",
    "missing_checkout",
    "wrong_format_dash_slash",
    "wrong_format_dots",
]
