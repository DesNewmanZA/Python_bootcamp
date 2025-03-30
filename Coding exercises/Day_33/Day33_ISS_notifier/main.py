# Import needed modules
import requests
import datetime
import smtplib

# Define parameters of location - latitude and longitude
MY_LAT = 22.551430
MY_LONG = -33.986840
DUMMY_MAIL = 'test@gmail.com'
DUMMY_PASSWORD = 'password'


# Do API call for sunrise and sunset times to determine if it's nighttime - looks at hour holistically
def is_it_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sunset_info = int(response.json()['results']['sunset'].split('T')[1].split(':')[0])
    sunrise_info = int(response.json()['results']['sunrise'].split('T')[1].split(':')[0])

    hr_now = datetime.datetime.now().hour
    print(sunrise_info, sunset_info, hr_now)

    if hr_now >= sunset_info or hr_now <= sunrise_info:
        return True


# Check to see if the ISS is anywhere in 5 degrees of current location
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG:
        return True
    else:
        return False


if is_it_night() and is_iss_overhead():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(DUMMY_MAIL, DUMMY_PASSWORD)
    connection.sendmail(
        from_addr=DUMMY_MAIL,
        to_addrs=DUMMY_MAIL,
        msg="Subject:ISS notification\n\nThe ISS should be visible from your location in the sky right now."
    )
