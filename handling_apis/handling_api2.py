import requests
import json

def get_products_data():
    response = requests.get("https://api.freeapi.app/api/v1/public/randomproducts")
    if response.status_code == 200:
        products = response.json()["data"]['data']
        return json.dumps(products, indent=4)  # for pretty printing the JSON response
    

print(get_products_data())

def main():
    try:
        products = get_products_data()
        print("Products data:")
        print(products)
    except Exception as e:
        print(f"Error occurred: {e}")
        exit(1)
        

if __name__ == "__main__":
    main()