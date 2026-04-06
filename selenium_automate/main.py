from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Create a new instance of the Chrome driver
driver = webdriver.Chrome()

try:
    # 2. Navigate to the web form page
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    print(f"Page title: {driver.title}")

    # Set an implicit wait to help elements be found (optional but recommended)
    driver.implicitly_wait(0.5)

    # 3. Find the "my-text" input box and enter text
    text_box = driver.find_element(by=By.NAME, value="my-text")
    text_box.send_keys("Selenium Automation")

    # 4. Find the submit button and click it
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    submit_button.click()

    # 5. Find the message element and print its text
    message = driver.find_element(by=By.ID, value="message")
    text = message.text
    print(f"Message received: {text}")

    # Optional: Keep the browser open for a few seconds to observe the result
    time.sleep(3)

finally:
    # 6. Close the browser
    driver.quit()
