from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
def fun(df_list,r,y):
    url='https://josaa.admissions.nic.in/applicant/seatmatrix/openingclosingrankarchieve.aspx'
    driver=webdriver.Firefox()
    driver.get(url)
    element_dropdown=driver.find_element(By.CSS_SELECTOR,'div.row:nth-child(2) > div:nth-child(2)').click()
    element_dropdown=driver.find_element(By.CSS_SELECTOR,y).click()
    element_dropdown=driver.find_element(By.CSS_SELECTOR,'div.row:nth-child(3) > div:nth-child(2)').click()
    element_dropdown=driver.find_element(By.CSS_SELECTOR,r).click()
    element_dropdown=driver.find_element(By.CSS_SELECTOR,'div.row:nth-child(4) > div:nth-child(2)').click()
    element_dropdown=driver.find_element(By.CSS_SELECTOR,'li.active-result:nth-child(4)').click()
    element_dropdown=driver.find_element(By.CSS_SELECTOR,'div.row:nth-child(5) > div:nth-child(2)').click()
    element_dropdown=driver.find_element(By.CSS_SELECTOR,'li.active-result:nth-child(2)').click()
    element_dropdown=driver.find_element(By.CSS_SELECTOR,'div.row:nth-child(6) > div:nth-child(2)').click()
    element_dropdown=driver.find_element(By.CSS_SELECTOR,'li.active-result:nth-child(2)').click()
    element_dropdown=driver.find_element(By.CSS_SELECTOR,'div.row:nth-child(7) > div:nth-child(2)').click()
    element_dropdown=driver.find_element(By.CSS_SELECTOR,'li.active-result:nth-child(2)').click()
    element_dropdown=driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_btnSubmit').click()

    table=driver.find_element(By.XPATH,'/html/body/form/div[3]/div[2]/div/div[2]/div/table/tbody')
    rows = WebDriverWait(table, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'tr')))
    c=0
    for row in rows:
        tds = row.find_elements(By.TAG_NAME, 'td')
        c+=1
        if len(tds) > 3 :
            df_list.append([x.text.strip() for x in tds if len(x.text) > 0])
    driver.quit()
    return
l=[]
ys=['li.active-result:nth-child(2)','li.active-result:nth-child(3)','li.active-result:nth-child(4)','li.active-result:nth-child(5)','li.active-result:nth-child(6)','li.active-result:nth-child(7)','li.active-result:nth-child(8)']
rs=['li.active-result:nth-child(2)','li.active-result:nth-child(3)','li.active-result:nth-child(4)','li.active-result:nth-child(5)','li.active-result:nth-child(6)','li.active-result:nth-child(7)']
for i in ys:
    for j in rs:
        fun(l,j,i)
        df=pd.DataFrame(l)
        print(f'round {rs.index(j)+1} of year{2022-ys.index(i)} done')
df.to_csv('path_output_file.csv')

