# Capstone_Project_2

Overview
----------------
This Python program is designed for automating functional tests on a web application using the Selenium WebDriver library. The test cases cover scenarios related to the "Forgot Password" functionality and validations on the Admin page, including header and menu options.

Prerequisites
-----------------
Python installed on your machine (https://www.python.org/downloads/)
Selenium WebDriver library installed (You can install it using pip install selenium)
Mozilla Firefox browser installed (or update the webdriver.Chrome() line in the code to use a different browser)

Project Structure
--------------------------
The project consists of the following files:
main.py: The main Python script containing the test automation code.
Data.py: A module containing data used by the test cases, such as URLs, usernames, and passwords.
Locators.py: A module containing locators (XPaths, CSS selectors, etc.) for the web elements used in the test cases.
Usage
Clone the repository to your local machine.
Open a terminal or command prompt and navigate to the project directory.

Run the tests using the command: 
------------------------------------------------------------
python -m pytest main.py --html=log.html

Note: Make sure to update the browser driver path in the webdriver.Chrome() line if you are using a different browser.

Test Cases
---------------
Test Case 1: Forgot Password link validation
Launches the web application and clicks on the "Forgot Password" link.
Enters a username and clicks the "Reset Password" button.
Verifies the success message.
Test Case 2: Header Validation on Admin Page
Logs in as an admin user.
Navigates to the Admin page and validates the page title.
Validates the presence of specified options on the Admin page.
Logs out successfully.
Test Case 3: Main Menu Validation on Admin Page
Logs in as an admin user.
Validates the presence of specified menu items on the Admin page.
Logs out successfully.

Customization
-----------------------------
Update the browser type in the self.driver = webdriver.Chrome() line to use a different browser.
Modify data in the Data.py file to match your test environment.
Adjust locators in the Locators.py file if the web application's structure changes.

