import requests
def getClothingPrices():
    url = "https://apidojo-forever21-v1.p.rapidapi.com/products/v2/list"

    querystring = {"category": "women_main", "pageSize": "48", "pageNumber": "1",
                "sortby": "0", "filterColor": "BLACK", "filterSize": "XS/S"}

    headers = {
        'x-rapidapi-key': "91bcf22dd9msh88ccbae757c3c69p14ee16jsna69aea48484e",
        'x-rapidapi-host': "apidojo-forever21-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    # print(response.text)
    print(response["CatalogProducts"][0]["ListPrice"])
    print(response["CatalogProducts"][1]["ListPrice"])
    print(response["CatalogProducts"][2]["ListPrice"])
    print(response["CatalogProducts"][3]["ListPrice"])
    print(response["CatalogProducts"][4]["ListPrice"])

def getClothingUrl(query):
    # print(response.text)
    
    clothing_get = "https://apidojo-forever21-v1.p.rapidapi.com/products/v2/list"
    response = requests.get(clothing_get).json()
    url = response["CatalogProducts"][0]["DefaultProductImage"]
    return url
    # print(response["CatalogProducts"][0]["DefaultProductImage"])

    
