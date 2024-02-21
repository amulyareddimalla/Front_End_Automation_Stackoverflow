from selenium.webdriver.common.by import By
from Utils.readProperties import ReadConfig
from Utils import WebElementUtil


class HomePage:

    def __init__(self, obj1):

        global driver
        driver=obj1
        self.elem = WebElementUtil.ElementsUtil(driver, By.XPATH)
        self.menu_item_xpath = "//a[@role='menuitem']//span"
        self.questions_click_xpath="//span[contains(text(),'Questions')]"


    def get_web_link(self):
        readconfig = ReadConfig()  # create object without any argument
        self.baseURL = readconfig.getApplicationURL()
        driver.get(self.baseURL)

    def menu_item_click(self):
        self.elem.WaitForElementDisplayed(self.menu_item_xpath, 60)
        self.elem.click(By.XPATH, self.menu_item_xpath)

    def questions_click(self):
        self.elem.WaitForElementDisplayed(self.questions_click_xpath, 60)
        self.elem.get_text(By.XPATH,self.questions_click_xpath)



