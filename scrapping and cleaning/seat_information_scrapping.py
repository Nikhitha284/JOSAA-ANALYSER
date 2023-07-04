from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
url='https://josaa.admissions.nic.in/applicant/seatmatrix/OpeningClosingRankArchieve.aspx'
driver=webdriver.Firefox()
driver.get(url)
element_dropdown=driver.find_element(By.CSS_SELECTOR,'.fontb > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)').click()
element_dropdown=driver.find_element(By.CSS_SELECTOR,'li.active-result:nth-child(2)').click()
element_dropdown=driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_ddlInstitute')
select = Select(element_dropdown)
select.select_by_visible_text('ALL')
element_dropdown=driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_ddlBranch')
select = Select(element_dropdown)
select.select_by_visible_text('ALL')
element_dropdown=driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_btnSubmit').click()
table=driver.find_element(By.XPATH,'/html/body/form/div[6]/div/table/tbody/tr/td/div/div[1]/table/tbody')
df_list=[]
rows = WebDriverWait(table, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'tr')))
for row in rows:
    if rows.index(row)%3==0 and rows.index(row)>=3:
        tds = row.find_elements(By.TAG_NAME, 'td')
        if len(tds) > 3 :
            k=([x.text.strip() for x in tds if len(x.text) > 0])
            if int(k[-2])!=0:   df_list.append(k)
df=pd.DataFrame(df_list)
df.drop(df.columns[[-3]], axis=1, inplace=True)
df.to_csv('seat.csv')
driver.quit()