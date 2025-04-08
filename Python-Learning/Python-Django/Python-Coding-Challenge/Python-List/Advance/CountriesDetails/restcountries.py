import requests
import pandas as pd

def get_country_details(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)

    if response.status_code != 200:
        return f"❌ Country '{country_name}' not found!"

    data = response.json()[0]

    details = {
        'Name': data['name']['common'],
        'Capital': data.get('capital', ['N/A'])[0],
        'Region': data.get('region', 'N/A'),
        'Subregion': data.get('subregion', 'N/A'),
        'Population': data.get('population', 'N/A'),
        'Area (km²)': data.get('area', 'N/A'),
        'Currency': list(data.get('currencies', {}).keys())[0] if 'currencies' in data else 'N/A',
        'Languages': ', '.join(data.get('languages', {}).values()),
        'Flag URL': data.get('flags', {}).get('png', 'N/A')
    }

    return pd.DataFrame.from_dict(details, orient='index', columns=['Value'])

# Example usage
country = input("Enter country name: ")
print(get_country_details(country))
