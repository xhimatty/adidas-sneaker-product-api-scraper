# Adidas Sneakers Scraper

This scraper collects Adidas men's sneaker product data directly from the site's internal product API.

The system reverse-engineers the API used by the Adidas men's athletic sneakers listing and collects the product information returned by the API.

## What it collects

For each product, the scraper collects:

* Product ID
* Title
* Subtitle
* Product URL
* Model number
* Colour variations
* Product image
* Price data
* Rating count
* Rating
* Prime availability
* Wishlist eligibility

The results are saved to a CSV file:

```text
adidas_men_sneakers.csv
```

## How it works

The scraper sends requests to the endpoint using a persistent `requests.Session()` with the required headers and cookies. The API returns 48 products per request from 23 pages, with 1,104 products available for the selected men's athletic sneakers category.


This gives the following starting positions:

```text
0
48
96
144
...
1008
1056
```

Each product is extracted, added to the results list and finally converted into a Pandas DataFrame and written to CSV.

## Project structure

```text
adidas-sneakers-scraper/
│
├── scraper.py
├── .env
├── .gitignore
├── requirements.txt
└── adidas_men_sneakers.csv
```

## Requirements

Python 3.x

Install the required packages:

```bash
pip install requests python-dotenv pandas
```

## Environment variables

The scraper loads the Adidas request headers and cookies from a `.env` file.

Example:

```
HEADERS='{"User-Agent": "..."}'
COOKIES='{"cookie_name": "..."}'
```


## Running the scraper

Run:

```bash
python scraper.py
```

After the requests finish, the collected products are written to:

```text
adidas_men_sneakers.csv
```

## Notes

> [!Note]
>
>This system was built by monitoring the network traffic from the Adidas men's sneakers page, identifying the API request used to retrieve the product data, and reproducing that request directly with Python.
>
>The approach avoids the overhead of browser automation and relying on brittle CSS selectors to collect the product information.
>
>The API response also contains other information such as categories, breadcrumbs, filters, sorting rules, and query suggestions. This system focuses on the product data.


## Disclaimer
> [!IMPORTANT]
>
>Ensure your use of the website or API follows the website's terms, applicable laws, and any access restrictions.
