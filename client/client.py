import requests
from data import raw_products_data

url = "http://127.0.0.1:8000/products/add_product"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU1MzMxNDgwLCJpYXQiOjE3MjM3OTU0ODAsImp0aSI6IjQ2NWZkZmE3MzM0NTQ2Mjg4MDExNjUxYTkyZjk0ZThjIiwidXNlcl9pZCI6ImMyYTZiOGE5OWM0MTRiNWJiZjI4YWI0NDljMTVjZWQzIn0.ITR3eVVOB1-FiS1WuV-xOUx92BEdRTwWTIHKdcDuuJY"
}

for product in raw_products_data['products']:
    data = {
        "title": product.get("title"),
        "description": product.get("description"),
        "category": product.get("category"),
        "price": product.get("price"),
        "discountPercentage": product.get("discountPercentage"),
        "rating": product.get("rating"),
        "thumbnail": product.get("thumbnail"),
    }
    if any(value is None for value in data.values()):
        print("Value in {} in null".format(data))
        break

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        created_data = response.json()
        print("Product with id {} is created".format(created_data["productId"]))
    else:
        print(f"Failed to create data: {response.status_code}")
