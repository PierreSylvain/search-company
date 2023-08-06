import os
from agents.search_agent import lookup as search_url
import argparse

OPENAI_APY_KEY = os.environ.get("OPENAI_API_KEY")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get company name and city")
    parser.add_argument("--company", type=str, required=True, help="Enter company name")
    parser.add_argument("--city", type=str, required=True, help="Enter city name")

    args = parser.parse_args()

    company_url = search_url(args.company, args.city)

    print(company_url)

