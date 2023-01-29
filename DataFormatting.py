import pandas as pd


def read_json():
    prices_df = pd.read_json('data/housingPrices.json')
    prices_df.replace('â‚¬', '')
    prices_df.to_csv('data/housingPrices.csv')
    print("CSV generated.")
