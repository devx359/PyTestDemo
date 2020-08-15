from  selenium  import webdriver
import time


def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="E:/PythonWorkspace/PyTestDemo/Drivers/chromedriver_83.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()

def test_action():
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    assert "dashboard" in driver.current_url
    time.sleep(5)


def test_teardown():
    driver.close()
    driver.quit()
    print("Test Completed")


