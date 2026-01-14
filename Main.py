
import pandas as pd
import requests

from bs4 import BeautifulSoup


product_name = []
price_list = []
description = []
review_list = []


for i in range(2,10):


    url = "https://www.flipkart.com/search?q=mobile+under+50000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_18_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_18_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobile+under+50000%7CMobiles&requestId=76535241-3257-411c-89ca-23fd42abff81&as-searchtext=mobile+under+50000&page="+str(i)
    r = requests.get(url)

    soup = BeautifulSoup(r.text,"lxml")
    box = soup.find("div",class_="QSCKDh dLgFEE")
    

    names=box.find_all("div",class_ = "RG5Slk")
    for i in names:
        name = i.text
        product_name.append(name if name else "N/A")

        
    # print(len(product_name))
    # print(product_name)


    prices = box.find_all("div",class_="hZ3P6w DeU9vF")
    for i in prices:
        name = i.text
        price_list.append(name if name else "N/A")
        
    # print(prices)

    desc = box.find_all("ul",class_="HwRTzP")
    for i in desc:
        name = i.text
        description.append(name if name else "N/A")
    # print(description)

    reviews = box.find_all("div",class_="MKiFS6")
    for i in reviews:
        name = i.text
        review_list.append(name if name else "No reviews")
    
min_len = min(len(product_name),len(price_list),len(description),len(review_list))
df = pd.DataFrame({"Product Name": product_name[:min_len], "Prices": price_list[:min_len],"Description": description[:min_len],"reviews": review_list[:min_len]})


print(df)

df.to_csv("flipkart_mobiles_under_5000.csv")



