from selenium import webdriver
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
    	self.fail('Finish the test!')

        # She is invited to enter a to do item

        # She types 'Buy peacock feathers' into a text box

        # When she hits enter, the page updates and the page lists her task as an item in the todo list

        # There is a text box asking her to add another item.
        # She enters 'use peackcok deathers to make a fly'

        # The page updates again and shows both items on her list

        # Kelly wonders whether the site will remember her list and sees the site has a unique url for her request

        # She visits the url and sees her items still there

        # Kelly ends her session

if __name__ == '__main__':
	unittest.main()