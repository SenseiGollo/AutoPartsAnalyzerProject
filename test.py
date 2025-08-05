import requests
import json

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

    # ADD THIS to debug
    print(json.dumps(data, indent=2))

    # Now safely access the expected path
    try:
        items = data['findCompletedItemsResponse'][0]['searchResult'][0].get('item', [])
        return items
    except KeyError as e:
        print(f"KeyError: {e}")
        return []
