#Just a test that covers the following techniques:
# - Logging into a website with python
# - Navigating through a website with python
# - Scraping information off of a page with python
# - Displaying scraped information
#This will be repurposed with Indeed beautifully. Many possiblities.

#This is reeeaaalll nice
import mechanicalsoup

#Our initial entry, taking us to the login page.
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://www.inoutboard.com/Login.aspx")

#Filling out username and password.
browser.select_form('#PageForm')
browser["UserNameInput"] = "******"
browser["PasswordInput"] = "******"

#Submitting/Logging In with provided info.
browser.submit_selected()

#Following the link of a tab on the page
browser.follow_link( browser.get_current_page().select('#header_tdPeople')[0].a.attrs['href'] )

#Getting all rows
rows = browser.get_current_page().select('tr.AlternatingItemStyle') + browser.get_current_page().select('tr.ItemStyle')

#Getting all links from every row
links = []
for row in rows:
	links = links + row.select('a')

#Prints every first and last name and the associated href
for link in links:
	if link.attrs['href'].startswith('../Profile'):
		print link.span.text + ' --> ' + link.attrs['href']