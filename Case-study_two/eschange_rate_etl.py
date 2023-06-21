import requests
import pandas as pd
from datetime import datetime
import schedule
import time

CURRENCIES = ['NGN', 'GHS', 'KES', 'UGX', 'MAD', 'XOF', 'EGP']
API_ENDPOINT = 'https://xecdapi.xe.com/v1/convert_from.json/'

API_KEY = 'p767mmnphg0a9vtnv8giv0iagg'
HEADERS = {'Authorization': f"Bearer {'p767mmnphg0a9vtnv8giv0iagg'}"}

# Function to fetch exchange rates and save them
def fetch_exchange_rates():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        rates = []

        for currency_to in CURRENCIES:
            response = requests.get(f'{API_ENDPOINT}?from=USD&to={currency_to}', headers=HEADERS)
            data = response.json()
            rate_to_currency = data['to'][0]['mid']
            rate_to_usd = data['from'][0]['mid']

            rates.append({
                'timestamp': timestamp,
                'currency_from': 'USD',
                'USD_to_currency_rate': rate_to_currency,
                'currency_to_USD_rate': rate_to_usd,
                'currency_to': currency_to
            })

        df = pd.DataFrame(rates)

        # Load existing data from file
        try:
            existing_data = pd.read_csv('exchange_rates.csv')
            existing_data['timestamp'] = pd.to_datetime(existing_data['timestamp'])
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df = pd.concat([existing_data, df]).drop_duplicates(subset=['timestamp'], keep='last')
        except FileNotFoundError:
            pass

        # Save data to CSV
        df.to_csv('exchange_rates.csv', index=False)

        print(f'Exchange rates fetched and saved successfully at {timestamp}')
    except Exception as e:
        print(f'Error fetching exchange rates: {str(e)}')

# Schedule the job
schedule.every().day.at('01:00').do(fetch_exchange_rates)
schedule.every().day.at('23:00').do(fetch_exchange_rates)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
