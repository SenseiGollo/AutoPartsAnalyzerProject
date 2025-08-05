import requests
import json
import pandas as pd

def find_sold_items(query, app_id):
    url = "https://svcs.ebay.com/services/search/FindingService/v1"
    headers = {
        "X-EBAY-SOA-OPERATION-NAME": "findCompletedItems",
        "X-EBAY-SOA-SERVICE-VERSION": "1.13.0",
        "X-EBAY-SOA-SECURITY-APPNAME": app_id,
        "X-EBAY-SOA-RESPONSE-DATA-FORMAT": "JSON",
    }
    params = {
        "keywords": query,
        "categoryId": "6024",  # Optional: Parts & Accessories
        "itemFilter(0).name": "SoldItemsOnly",
        "itemFilter(0).value": "true",
        "paginationInput.entriesPerPage": "10",
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    # Debug the full response
    print(json.dumps(data, indent=2))

    try:
        items = data['findCompletedItemsResponse'][0]['searchResult'][0].get('item', [])
        return items
    except KeyError as e:
        print(f"KeyError: {e}")
        return []

# 🔑 Replace this with YOUR real eBay App ID
ebay_app_id = "NahumMan-AutoPart-PRD-90bd59c28-e23f7663"

# 👇 Try it out
items = find_sold_items("2010 Ford Taurus", ebay_app_id)

# 🔄 Convert to DataFrame if not empty
if items:
    df = pd.DataFrame(items)
    print(df.head())
else:
    print("No sold items found.")
