from faker import Faker
class User_booking:
    def __init__(self):
        self.faker = Faker()

    def valid_data(self):
        return {
            "firstname": self.faker.first_name(),
            "lastname": self.faker.last_name(),
            "totalprice": self.faker.random_int(min=50, max=500),
            "depositpaid": self.faker.boolean(),
            "bookingdates": {
                "checkin": self.faker.date_between(start_date="-1y", end_date="today").isoformat(),
                "checkout": self.faker.date_between(start_date="today", end_date="+1y").isoformat()
            },
            "additionalneeds": self.faker.word()
        }

    def invalid_data(self):
        return {
            "firstname": "",
            "lastname": "",
            "totalprice": -100,
            "depositpaid": None,
            "bookingdates": {
                "checkin": "invalid_date",
                "checkout": "invalid_date"
            },
            "additionalneeds": 12345
        }
