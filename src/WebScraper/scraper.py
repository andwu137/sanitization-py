from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get(
    "https://www.canada.ca/en/revenue-agency/services/forms-publications/forms.html"
)
time.sleep(1)
select = Select(driver.find_element(By.TAG_NAME, "select"))

select.select_by_value("-1")

table = driver.find_element(By.ID, "wb-auto-4")
forms = table.find_elements(By.TAG_NAME, "a")
with open("CRA_FORMS.csv", "w") as csvfile:
    for form in forms:
        csvfile.write(f"{form.text}\n")
