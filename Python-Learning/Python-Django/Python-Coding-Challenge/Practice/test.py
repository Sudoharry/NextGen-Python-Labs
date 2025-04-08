from nsetools import Nse
from requests.exceptions import JSONDecodeError, RequestException
import time

def get_stock_sector(symbol):
    """
    Fetch the industry (sector) of a stock from NSE.
    Returns None if there's an error or the sector is not available.
    """
    try:
        nse = Nse()
        # Add a small delay to avoid rate limiting
        time.sleep(1)
        stock_details = nse.get_quote(symbol)
        if stock_details:
            print(f"Received data: {stock_details}")  # Debug info
            return stock_details.get("industry")
        return None
    except (JSONDecodeError, RequestException) as e:
        print(f"Error fetching data for {symbol}: {str(e)}")
        return None
    except Exception as e:
        print(f"Unexpected error for {symbol}: {str(e)}")
        return None

# Example Usage with multiple retries
def try_get_sector(symbol, max_retries=3):
    for attempt in range(max_retries):
        print(f"Attempt {attempt + 1} of {max_retries}")
        result = get_stock_sector(symbol)
        if result:
            return result
        time.sleep(2)  # Wait between retries
    return None

# Test the function
result = try_get_sector("TCS")
if result:
    print(f"Sector: {result}")
else:
    print("Unable to fetch sector information")