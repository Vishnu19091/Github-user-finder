from bs4 import BeautifulSoup
import requests
import pandas as pd

user=input('Enter User name:').strip()
actions=input('Do you want to download the user details as csv file?(y/n)')

gurl=f'https://api.github.com/users/{user}'

def get_user():
    data=requests.get(gurl)

    if data.status_code!=404:
        datas=data.json()
        df=pd.DataFrame(datas.items())
        df.columns=['Key','Values']
        if actions!='n' or 'N':
            df.to_csv('GitHub_user_details.csv',index=False)
        else: exit

    else:
        print("Not Found! Try another name")
        exit
    print(df)
    
get_user()
