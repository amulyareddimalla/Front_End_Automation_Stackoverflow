from Pages.EditorsPage import EditorsPage
from Pages.HomePage import HomePage
from Pages.SearchPage import SearchPage
from Utils.BaseClass import BaseClass


class TestcaseOne(BaseClass):
    log = BaseClass.getLogger()

    def test_e2e(self):

        ''' Creating Objects for each Page '''
        homePage = HomePage(self.driver)
        searchPage=SearchPage(self.driver)
        editorsPage=EditorsPage(self.driver)
        homePage.get_web_link()
        self.log.info("Navigated to Application URL")
        homePage.menu_item_click()
        self.log.info("Clicked on Menu Item")
        homePage.questions_click()
        self.log.info("Clicked on Browse Questions Section")
        searchPage.Users_click()
        self.log.info("Clicked on Users on the left section")
        searchPage.Editors_click()
        self.log.info("Clicked on Editors")
        editorsPage.goto_page2_click()
        self.log.info("Navigated to Page 2")
        editorsPage.validate_page2_selected()
        self.log.info("Validated if Page 2 is selected")
        editorsPage.get_editor_max_edits()
        self.log.info("Captured all the users/single user having Maximum Edits Count in Page 2")





