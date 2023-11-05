from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set the URL of the SharePoint web page
sharepoint_url = str(input("Enter your sharepoint url: "))

# Initialize the web driver (make sure to specify the path to your WebDriver)
driver = webdriver.Chrome(executable_path='path/to/chromedriver')

# Open the SharePoint web page
driver.get(sharepoint_url)

# Navigate to the Network tab in the developer tools
driver.find_element_by_tag_name('body').send_keys(Keys.F12)  # Open developer tools
driver.find_element_by_id('tab-network').click()  # Click on the Network tab

# Allow time for the network tab to load (adjust the time as needed)
driver.implicitly_wait(8)

# Find and extract the URL
network_entries = driver.find_elements_by_css_selector('.netRow')
for entry in network_entries:
    if "videomanifest?provider" in entry.get_attribute("data-url"):
        url = entry.get_attribute("data-url")
        print("URL found:", url)
        break

# Close the browser
driver.quit()
