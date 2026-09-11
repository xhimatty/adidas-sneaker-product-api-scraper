import requests
import json
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

headers = json.loads(os.getenv('HEADERS'))
cookies = json.loads(os.getenv('COOKIES'))

session = requests.Session()

session.headers.update(headers)
session.cookies.update(cookies)

url = 'https://www.adidas.com/plp-app/api/taxonomy/men-athletic_sneakers'


def get_products():
    results = []

    for start in range(0, 1104, 48):
        params = {
            'start': str(start),
            'experiment': 'ATP-9119-1',
            'sitePath': 'us',
        }

        response = session.get(
            url=url,
            params=params,
        )

        # print(response.status_code)
        # print(response.url)
        data = response.json()
        # print(json.dumps(data, indent=2))

        # print(data.keys())
        # products = data['products']
        # print(json.dumps(products[0], indent=2))

        products = data.get('products', [])

        for product in products:
            results.append({
                'id': product.get('id'),
                'title': product.get('title'),
                'subTitle': product.get('subTitle'),
                'url': product.get('url'),
                'modelNumber': product.get('modelNumber'),
                'colourVariations': product.get('colourVariations', []),
                'image': product.get('image'),
                'priceData': product.get('priceData', {}),
                'ratingCount': product.get('ratingCount'),
                'rating': product.get('rating'),
                'isPrimeAvailable': product.get('isPrimeAvailable'),
                'wishlistEligible': product.get('wishlistEligible'),
            })

    return results

results = get_products()
df = pd.DataFrame(results)
df.to_csv('adidas_men_sneakers.csv', index=False)