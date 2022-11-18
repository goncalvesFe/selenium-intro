import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

option = Options()
option.headless = False 
# se não passar essa opção por padrão é falso
# se passar essa opção como verdadeiro a aba do navegador não é aberta para o usuario

driver = webdriver.Chrome("./chromedriver", options=option)
# driver = webdriver.Chrome(executable_path=r"./chromedriver")

driver.get('https://www.google.com/')

time.sleep(2)

search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

search_box.send_keys('Temperatura')

time.sleep(1)

search_box.submit()

time.sleep(1)

# temp = driver.find_element(By.XPATH, '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]/div/div[1]/span[1]').get_attribute('outerHTML')
temp = driver.find_element(By.XPATH, '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]/div/div[1]/span[1]').text

print('A temperatura está em:', temp, '°C')

time.sleep(5) # Let the user actually see something!

driver.quit()
