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
    # print(response["CatalogProducts"][0]["ListPrice"])

    price = response["CatalogProducts"][0]["ListPrice"]
    return price

def getClothingUrl():
    url = "https://apidojo-forever21-v1.p.rapidapi.com/products/v2/list"

    querystring = {"category": "women_main"}
    
    # querystring = {"category": "women_main", "pageSize": "48", "pageNumber": "1",
    #             "sortby": "0", "filterColor": "BLACK", "filterSize": "XS/S"}

    headers = {
        'x-rapidapi-key': "91bcf22dd9msh88ccbae757c3c69p14ee16jsna69aea48484e",
        'x-rapidapi-host': "apidojo-forever21-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    productlength = len(response["CatalogProducts"])
    print(productlength)
    imgurls = []
    for url in range(productlength):
        imgurls.append(response["CatalogProducts"][url]["DefaultProductImage"]) 
    return imgurls                   
