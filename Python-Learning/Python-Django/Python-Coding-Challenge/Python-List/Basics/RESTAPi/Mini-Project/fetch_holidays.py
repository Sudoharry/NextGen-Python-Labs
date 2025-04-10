# fetch_holidays.py

"""
This script fetches public holiday data using a REST API, parses the JSON response,
writes it to a CSV file, and uses datetime and CLI input for dynamic usage.

Concepts Covered:
    REST API        --> requests.get()
    JSON Parsing    --> response.json()
    CSV Writing     --> csv.DictWriter()
    Datetime        --> datetime.now().year
    CLI Input       --> input(), reusable format
"""

import requests
import csv
from datetime import datetime


def fetch_holidays(country_code='US', year=datetime.now().year):
    """
    Fetches public holidays for a given country and year using Nager.Date API.
    
    Args:
        country_code (str): ISO country code (e.g., 'US', 'IN').
        year (int): Year for which holidays are to be fetched.

    Returns:
        list: A list of holiday dictionaries or empty list on failure.
    """
    url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}"
    response = requests.get(url)

    if response.status_code != 200:
        print(" Failed to fetch holidays.")
        return []

    return response.json()


def save_to_csv(holidays, filename='holidays.csv'):
    """
    Saves holiday data to a CSV file.

    Args:
        holidays (list): List of holiday dictionaries.
        filename (str): Name of the CSV file to write.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['date', 'localName', 'name', 'countryCode', 'types']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for holiday in holidays:
            writer.writerow({
                'date': holiday['date'],
                'localName': holiday['localName'],
                'name': holiday['name'],
                'countryCode': holiday['countryCode'],
                'types': ','.join(holiday.get('types', []))
            })

    print(f" Holidays saved to {filename}")


if __name__ == '__main__':
    country = input("Enter country code (e.g. US, IN, DE): ").strip().upper()
    year_input = input("Enter year (e.g. 2024): ").strip()

    try:
        year = int(year_input)
    except ValueError:
        print(" Invalid year. Please enter a numeric value.")
        exit(1)

    holidays = fetch_holidays(country, year)
    if holidays:
        save_to_csv(holidays, f"{country}_holidays_{year}.csv")
