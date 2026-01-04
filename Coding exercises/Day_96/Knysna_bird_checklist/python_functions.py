# Import needed modules
import requests
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta


def get_date_range(years_needed):
    """
    Gets the current date and uses a years_needed parameter to say how many years back to go, giving a start and
    end date for usage in the SABAP2 API for which to pull birding observations.

    Args:
        years_needed (int): The size of the date range required.

    Returns:
        str: Today's date in string format.
        str: The date x years ago (where x is the years needed) in string format.
    """
    current_date = date.today()
    x_years_ago_date = (current_date - relativedelta(years=years_needed))

    return x_years_ago_date.strftime("%Y-%m-%d"), current_date.strftime("%Y-%m-%d")


def fetch_bird_data(pentad, start_date, end_date):
    """
    Uses the inputted pentad and date range to call the SABAP2 API and pull full protocol (FP) observations for the
    pentad over the given date range. The API returns back detailed information with an entry per species observation
    per pentad.

    To make this data useful to the web app, it is then turned into a pandas data frame that stores the card number of
    each FP as well as the species observed. This is then summarises up to get the total number of FPs performed as well
    as the total number of observations per bird species across these FPs.

    A final data frame is outputted that stores all species observed in the pentad over full protocols over the given
    date range, along with their numerical frequency and percentage of full protocols they have been observed in.

    Args:
        pentad (str): unique pentad identifier of the form xxxx_yyyy
        start_date (str): start date over which to look for pentad observations
        end_date (str): end date over which to look for pentad observations

    Returns:
        DataFrame: columns are species observed, frequency noted and percentage of FPs noted within.
    """
    # Pull API data
    url = f"https://api.birdmap.africa/sabap2/v2/R/{start_date}/{end_date}/pentad/{pentad}/data"

    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()['data']

    # Loop through all observations, clean and summarise
    list_of_obs = []
    for observation in data:
        if observation['Common_group'] is None:
            species_name = observation['Common_species']
        else:
            species_name = " ".join([observation['Common_species'], observation['Common_group']])
        species_name = species_name.split()
        species_name = " ".join(species_name)
        obs = [observation["CardNo"], species_name]
        list_of_obs.append(obs)

    # Convert the raw observations into a data frame for easier manipulation
    obs_df = pd.DataFrame(list_of_obs, columns=['CardNo', 'Species'])
    number_of_cards = len(obs_df[['CardNo']].value_counts())
    number_of_obs_per_bird = obs_df[['Species']].value_counts().to_frame(name='Frequency').reset_index()
    number_of_obs_per_bird['Percentage'] = number_of_obs_per_bird['Frequency'] / number_of_cards

    return number_of_obs_per_bird
