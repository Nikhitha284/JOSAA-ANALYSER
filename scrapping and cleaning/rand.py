#Extracting data from each round and year
import requests
from bs4 import BeautifulSoup
import pandas as pd
def josa_data(year, Round):
    url = 'https://josaa.admissions.nic.in/applicant/seatmatrix/OpeningClosingRankArchieve.aspx'


    params = {
        "ctl00$ContentPlaceHolder1$ddlInstype": "All",
        "ctl00$ContentPlaceHolder1$ddlInstitute": "ALL",
        "ctl00$ContentPlaceHolder1$ddlBranch": "ALL",         ## setting the values in the dictionary so that we cun run the loop
        "ctl00$ContentPlaceHolder1$ddlSeatType": "ALL",
        "ctl00$ContentPlaceHolder1$btnSubmit": "Submit"
    }
    #filling each input will itself will trigger a post request so we also following that
    with requests.Session() as s:
        R = s.get(url)    ##intial get request
        data = {}
        ## the values of the tags changes after every request so we should update it
        data.update({tag['name']: tag['value'] for tag in BeautifulSoup(R.content, 'html.parser').select('input[name^=__]')})
        data["ctl00$ContentPlaceHolder1$ddlYear"] = year
        R = s.post(url, data=data)
        data.update({tag['name']: tag['value'] for tag in BeautifulSoup(R.content, 'html.parser').select('input[name^=__]')})
        data["ctl00$ContentPlaceHolder1$ddlroundno"] = Round
        R = s.post(url, data=data)
        for key, value in params.items():   ##loop to avoid the repitetion
            data.update({tag['name']: tag['value'] for tag in BeautifulSoup(R.content, 'html.parser').select('input[name^=__]')})
            data[key] = value
            R = s.post(url, data=data)
        table = BeautifulSoup(R.text, 'html.parser').find(id='ctl00_ContentPlaceHolder1_GridView1') ## id for the table

    df = pd.read_html(table.prettify())[0]      ## read_html it reads the table from html
    df.dropna(inplace=True, how="all")

    df["Year"] = year   ## adding the extra column for year and round
    df["Round"] = Round

    return df
years = ['2016','2017','2018','2019','2020', '2021', '2022']
rounds = ['1', '2', '3', '4', '5', '6']

df = pd.DataFrame()
for year in years:
    for Round in rounds:
        df_temp = josa_data(year, Round)
        df = pd.concat([df, df_temp])
        print(Round,"of",year,"done")
df.to_csv('rando.csv')
