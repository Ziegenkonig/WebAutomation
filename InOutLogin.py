#Just a test that covers the following techniques:
# - Logging into a website with python
# - Navigating through a website with python
# - Scraping information off of a page with python
# - Displaying scraped information

#This is reeeaaalll nice
import mechanicalsoup

#Our initial entry, taking us to the login page.
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://www.inoutboard.com/Login.aspx", verify=False)

#Filling out username and password.
browser.select_form('#PageForm')
browser["UserNameInput"] = "******"
browser["PasswordInput"] = "******"

#Submitting/Logging In with provided info.
browser.submit_selected()

#Submitting the page to lead us to the change status page,
browser.select_form('#Form1')
browser.submit_selected('ChangeStatusButton')

#Changing our status and submitting the change.
browser.select_form('#PageForm')
browser["ddlStatusCode"] = "15259"
browser.submit_selected()
print('Status Successfully Updated!')