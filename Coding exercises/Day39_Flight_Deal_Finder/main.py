# Import needed items
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# Set origin airport
ORIGIN_CITY_IATA = "CPT"

# Initialize a data manager and a flight searcher
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Get the data in the flights spreadsheet
sheet_data = data_manager.get_destination_data()
# If the IATA codes are missing, populate them using the API
if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

# Get customer emails
customer_data = data_manager.get_customer_emails()
customer_emails = [row["What is your email address?"] for row in customer_data]

# Search for flights
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)

    # If cheaper than lower price, notify
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        if cheapest_flight.stops == 0:
            msg = f"Low price alert! Only GBP {cheapest_flight.price} to fly direct "\
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                      f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else:
            msg = f"Low price alert! Only GBP {cheapest_flight.price} to fly "\
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                      f"with {cheapest_flight.stops} stop(s) "\
                      f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."

        print(f"Lower price flight found to {destination['city']}!")
        notification_manager.send_sms(
             message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                          f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                          f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )
        notification_manager.send_emails(email_list=customer_emails, email_body=msg)

    elif cheapest_flight.price == "N/A":
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )