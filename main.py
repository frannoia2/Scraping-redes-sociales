from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from rrss import find_rrss
from config import config_func

rrss = open("rrss.txt", "w")
mktpl = open("mktpl.txt", "w")

#ejecutamos la configuración del webdriver por terminal
config_func()

#desglosamos el json de configuración
with open('configuracion.json') as json_file:
    config_data = json.load(json_file)

for curr_config in config_data['browsers']:
    curr_browser = curr_config['browser']
    curr_urls = curr_config['urls_doc']
    curr_xpath = curr_config['xpath']

if(curr_browser=='chrome'):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
elif(curr_browser=='firefox'):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)

urlsFile = open(curr_urls, "r")
urls = urlsFile.readlines()

#ejecutamos la busqueda de rrss
find_rrss(driver, urls, curr_xpath, rrss)