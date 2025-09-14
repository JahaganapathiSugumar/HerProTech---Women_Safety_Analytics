from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os

options = Options()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

params = {'behavior': 'allow', 'downloadPath': os.getcwd()}
driver.execute_cdp_cmd('Page.setDownloadBehavior', params)

driver.get("https://developers.facebook.com/apps/518553847299020/whatsapp-business/wa-dev-console/?business_id=1208705436938864")

