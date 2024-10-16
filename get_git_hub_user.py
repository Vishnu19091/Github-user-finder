from bs4 import BeautifulSoup
import requests
import pandas as pd

user=input('Enter User name:').strip()

gurl=f'https://api.github.com/users/{user}'

def get_user():
    data=requests.get(gurl)

    if data.status_code!=404:
        datas=data.json()
        df=pd.DataFrame(datas.items())
        df=df.rename(columns={0:"Content",1:"Values"})

    else:
        print("Not Found! Try another name")
        exit
    print(df)
    
get_user()
