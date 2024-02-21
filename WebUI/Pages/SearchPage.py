
from selenium.webdriver.common.by import By
from Utils import WebElementUtil

class SearchPage:

    def __init__(self, obj1):

        global driver
        driver=obj1
        self.elem = WebElementUtil.ElementsUtil(driver, By.XPATH)
        self.users_xpath = "//span[contains(text(),'Users')]"
        self.editor_xpath="//a[@data-value='editors']"

    def Users_click(self):
        self.elem.WaitForElementDisplayed(self.users_xpath, 60)
        self.elem.click(By.XPATH, self.users_xpath)

    def Editors_click(self):
        self.elem.WaitForElementDisplayed(self.editor_xpath, 60)
        self.elem.click(By.XPATH, self.editor_xpath)






