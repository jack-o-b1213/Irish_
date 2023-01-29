from WebScraper import generateJson
from DataFormatting import read_json
import os


def scraper():
    generateJson()


def generate_df():
    read_json()


if __name__ == "__main__":
    if not os.path.exists('data/housingPrices.json'):
        scraper()
    elif not os.path.exists('data/housingPrices.csv'):
        generate_df()
    else:
        print("CSV file already generated.")
