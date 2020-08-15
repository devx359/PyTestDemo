

class  deal_of_the_day_is_red():
    def __init__(self,locator):
        self.locator = locator

    def __call__(self,driver):
        element = driver.find_element_by_xpath(self.locator)
        color=element.get_attribute("data-a-badge-color")
        if color=="sx-lightning-deal-red":
            print("color matched #############")
            return True
        else:
            return False