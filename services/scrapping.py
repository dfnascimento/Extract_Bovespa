from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pandas as pd
from selenium import webdriver

from config import *



def scrap_pregao(url):
    '''
    Realiza a raspagem dos dados do pregao da B3 e retorna um DataFrame

    Parâmetros:
    url (str): Endereço da página web do pregão da B3

    Retorna:
    pd.DataFrame: DataFrame com os dados do pregão da B3
    
    '''

    options = webdriver.ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    df = pd.DataFrame()

    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "selectPage"))
        )
        
        dropdown = Select(driver.find_element(By.ID, "selectPage"))


        dropdown.select_by_visible_text("120")

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )

        table = driver.find_element(By.TAG_NAME, "table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        
        
        headers = []
        for header in rows[0].find_elements(By.TAG_NAME, "th"):
            headers.append(header.text)
        
        data = []
        for row in rows[1:-2]:  
            cols = row.find_elements(By.TAG_NAME, "td")
            row_data = []
            for col in cols:
                row_data.append(col.text)
            data.append(row_data)

        df = pd.DataFrame(data, columns=headers)
        
    finally:
        driver.quit()  
        return df
