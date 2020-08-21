import pytest
from selenium import webdriver
import time
from .custom_waits import deal_of_the_day_is_red
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from operator import itemgetter


def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="E:/PythonWorkspace/PyTestDemo/Drivers/chromedriver_83.exe")
    driver.maximize_window()
    #driver.implicitly_wait(10)  # seconds
    #driver.set_page_load_timeout(20)

def test_who():
    pytest.skip('skippping 1')


def test_youtubeSearch():
    pytest.skip('skippping youtube')
    driver.get("https://www.amazon.in/")

    WebDriverWait(driver,10).until(
        expected_conditions.element_to_be_clickable((By.XPATH,"//input[@id='twotabsearchtextbox']"))
    )

    driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("iphone")
    driver.find_element_by_xpath("//input[@type='submit'and  @value='Go']").click()
    #explicit wait
    WebDriverWait(driver,10).until(
        expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='s-main-slot s-result-list s-search-results sg-row']/div[@data-uuid]"))
    )
    """
    #custom explicit wait ****************************
    WebDriverWait(driver,10).until(
        deal_of_the_day_is_red("//div[@class='s-main-slot s-result-list s-search-results sg-row']/div[@data-uuid]/descendant::span[@class='a-badge-label']")

    )
    """

    ll=driver.find_elements_by_xpath("//div[@class='s-main-slot s-result-list s-search-results sg-row']/div[@data-uuid]")
    masterlist=[]
    for ele in ll :
        title=ele.find_element_by_xpath("./descendant::span[@class='a-size-medium a-color-base a-text-normal']").text
        link=ele.find_element_by_xpath("./descendant::span[@class='a-size-medium a-color-base a-text-normal']/..").get_attribute("href")
        price = ele.find_element_by_xpath("./descendant::span[@class='a-price-whole']").text
        try:
            eta = ele.find_element_by_xpath("./descendant::span[contains(@aria-label,'Get it by')]/span[2]").text
        except NoSuchElementException:
            print("ETA not provided")
            eta= "NA"
        dict1 = {}
        dict1['title']=title
        dict1['price']=price
        dict1['eta']=eta
        dict1['link']=link
        #print(dict1)
        #print(title,price,eta,link)
        masterlist.append(dict1)
    #@@@@@@@@@@   SORTING @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    sortedList = sorted(masterlist,key=itemgetter("price"),reverse=True)  #Sorting by itemgetter by dictionary key **********************************************
    #sortedList = sorted(masterlist, key=lambda i : i["price"],reverse=True)  # Sorting by lambda by dictionary key **********************************************

    for x in sortedList:
        print(x['title'],x['price'])


def test_broker():
    raise Exception("something is wrong")
def test_success():
    assert True
def test_failure():
    assert False
    








def test_teardown():
    driver.quit()
