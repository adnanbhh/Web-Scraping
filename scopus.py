import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def scopus(term):


    import pymongo
    from selenium import webdriver
    import time


    driver = webdriver.Chrome()

    driver.get("https://id.elsevier.com/as/authorization.oauth2?platSite=SC%2Fscopus&ui_locales=en-US&scope=openid+profile+email+els_auth_info+els_analytics_info+urn%3Acom%3Aelsevier%3Aidp%3Apolicy%3Aproduct%3Aindv_identity&response_type=code&redirect_uri=https%3A%2F%2Fwww.scopus.com%2Fauthredirect.uri%3FtxGid%3D723f8bda4be8d03a90d37a5f1e445a26&state=forceLogin%7CtxId%3D343759EFCEF0AA9D5E93AEB9A8B1A82A.i-04f6af96501b6f883%3A5&authType=SINGLE_SIGN_IN&prompt=login&client_id=SCOPUS")
    driver.find_element(By.XPATH, "/html/body/div/section/main/form/div[3]/div[2]/button").click()
    driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/div/form/div[1]/input").send_keys("mouad.karim@etu.uae.ac.ma")
    driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/div/form/div[3]/div/button").click()
    driver.find_element(By.XPATH, "/html/body/div/section/main/form/div[2]/div[2]/input").send_keys("AZEaze123@@")
    driver.find_element(By.XPATH, "/html/body/div/section/main/form/div[3]/div[2]/button").click()
    driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div[3]/div/div[2]/div[2]/micro-ui/scopus-homepage/div/div/els-tab/els-tab-panel[1]/div/form/div[1]/div/div[2]/els-input/div/label/input").send_keys(term)

    driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div/div[3]/div/div[2]/div[2]/micro-ui/scopus-homepage/div/div/els-tab/els-tab-panel[1]/div/form/div[2]/div[2]/button").click()
    # url to be scraped
    scopus_url = "https://www.scopus.com/results/results.uri?sid=a79efacd2d76adb4647cff9908724ada&src=s&sot=b&sdt=b&origin=searchbasic&rr=&sl=19&s=TITLE-ABS-KEY("+term+")&searchterm1=data&searchTerms=&connectors=&field1=TITLE_ABS_KEY&fields="

    # collect new titles from pubmed
    time.sleep(4)

    driver.get(scopus_url)

def openCanada():
    openCanada = "https://open.canada.ca/data/en/dataset/fe1dfbb9-0fc3-42ca-b2a9-6ca4c05dbac9"
    driver = webdriver.Chrome()
    driver.get(openCanada)
    links = driver.find_elements(By.CLASS_NAME, "resource-url-analytics")
    for c in links:
        c.click()
        time.sleep(1)
    driver.close()
