from selenium.webdriver.common.by import By
from Utils import WebElementUtil


class EditorsPage:

    def __init__(self, obj1):

        global driver
        driver=obj1
        self.elem = WebElementUtil.ElementsUtil(driver, By.XPATH)
        self.users_css = ".user-info"
        self.editor_xpath="//a[@data-value='editors']"
        self.page_2_xpath="//a[@title='Go to page 2']"
        self.page2_selected_xpath="//div[@class='s-pagination--item is-selected']"
        self.user_rows="//div[@class='grid--item user-info  user-hover']"
        self.username_css=".user-details a"
        self.edits_css=".user-tags"
        self.location_css=".user-location"

    def goto_page2_click(self):
        self.elem.WaitForElementClickable(self.page_2_xpath, 60)
        self.elem.click(By.XPATH, self.page_2_xpath)

    def validate_page2_selected(self):
        self.elem.WaitForElementDisplayed(self.page2_selected_xpath, 60)
        self.elem.get_text(By.XPATH, self.page2_selected_xpath)


    def get_editor_max_edits(self):
        '''Finding all user rows from Page 2'''
        user_rows = driver.find_elements(By.CSS_SELECTOR,self.users_css )

        '''Initialize variables to store max edits count, usernames, and locations'''
        max_edits = 0
        max_edits_usernames = []
        max_edits_locations = []

        '''Iterating over each user row to find the user with max_edit count'''
        for row in user_rows:
            username_element = row.find_element(By.CSS_SELECTOR, self.username_css)
            username = username_element.text
            tags_element = row.find_element(By.CSS_SELECTOR,self.edits_css )
            tags = tags_element.text
            if "edits" in tags:
                edits = int(tags.split(' ')[0])
                if edits > max_edits:
                    max_edits_usernames.append(username)
                    max_edits_locations.append(row.find_element(By.CSS_SELECTOR,self.location_css ).text.strip())
                    max_edits = edits
                elif edits == max_edits:
                    '''If current user has the same max edits as previous users, add them to the list'''
                    max_edits_usernames.append(username)
                    max_edits_locations.append(row.find_element(By.CSS_SELECTOR, self.location_css).text.strip())

        '''Print the result of users with Max edits count on Page 2'''
        print("Users with the maximum edits count on Page 2:")
        for i in range(len(max_edits_usernames)):
            print("Username:", max_edits_usernames[i])
            print("Location:", max_edits_locations[i])
            print("Edits Count:", max_edits)

