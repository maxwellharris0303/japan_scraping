from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse
import quickstart

quickstart.main()
name_list = quickstart.getNameList()
print(name_list)

def get_root_url(url):
    parsed_url = urlparse(url)
    root_url = parsed_url.scheme + "://" + parsed_url.netloc
    return root_url

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com/search?q=google+search&rlz=1C1GCEB_enDE1078DE1078&oq=google+search&gs_lcrp=EgZjaHJvbWUyDwgAEEUYORiDARixAxiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIGCAUQRRg8MgYIBhBFGDwyBggHEEUYPNIBCDM2NDBqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8")

sleep(3)
driver.find_element(By.CSS_SELECTOR, "button[id=\"L2AGLb\"").click()
index = 0
for name in name_list:
    input_search = driver.find_element(By.CSS_SELECTOR, "textarea[jsname=\"yZiJbe\"")
    input_search.clear()
    input_search.send_keys(name)
    input_search.send_keys(Keys.ENTER)
    url_element = driver.find_element(By.CSS_SELECTOR, "a[jsname=\"UWckNb\"]")
    # print(url_element.get_attribute('href'))
    url = get_root_url(url_element.get_attribute('href'))
    print(url)

    quickstart.main()
    RANGE_DATA = f'Sheet1!B{index + 2}:B'

    quickstart.insertURL(RANGE_DATA, url)

    index += 1
print("Done!!!")
 