from faker import Faker
from utils.api_client import APIClient


class Booking():
    def __init__(self):
        self.faker = Faker()
        self.api_client = APIClient()
        self.firstname = self.faker.first_name()
        self.lastname = self.faker.last_name()
        self.totalprice = self.faker.random_int(min=50, max=500)
        self.depositpaid = self.faker.boolean()
        self.bookingdates = {
            "checkin": self.faker.date_between(start_date="today", end_date="+1m").isoformat(),
            "checkout": self.faker.date_between(start_date="+1m", end_date="+1y").isoformat()
        }
        self.additionalneeds = self.faker.word()
        self.bookingid = None

    def booking_data(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "totalprice": self.totalprice,
            "depositpaid": self.depositpaid,
            "bookingdates": self.bookingdates,
            "additionalneeds": self.additionalneeds
        }

    def invalid_booking_data(self):
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

    def create_booking_id(self):
        payload = self.booking_data()
        response = self.api_client.post('/booking', json=payload)
        self.bookingid = response.json()['bookingid']
        return self.bookingid

    def delete_booking_id(self):
        booking_id = self.bookingid
        if self.bookingid:
            try:
                response = self.api_client.delete(endpoint=f'/booking/{booking_id}')
                assert response.status_code == 200

            except Exception as e:
                print(e)
        else:
            print('Booking ID is missed')


if __name__ == '__main__':
    booking = Booking()
    booking.create_booking_id()
    booking.delete_booking_id()
