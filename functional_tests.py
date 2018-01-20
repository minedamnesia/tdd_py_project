from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
    	self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
	    # Kelly has heard about a new online todo app.  She checks out its homepage
        self.browser.get('http://localhost:8000')

       # She looks for the page title and header mentioning todo lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types 'Buy peacock feathers' into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates and the page lists her task as an item in the todo list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # There is a text box asking her to add another item.
        # She enters 'use peackcok deathers to make a fly'
        self.fail('Finish the test!')

        # The page updates again and shows both items on her list

        # Kelly wonders whether the site will remember her list and sees the site has a unique url for her request

        # She visits the url and sees her items still there

        # Kelly ends her session

if __name__ == '__main__':
	unittest.main()