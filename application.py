from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains


def setup() -> webdriver:
    username = input("Enter your UTORid: ")
    password = input("Enter your UTORid password: ")

    options = Options()
    options.headless = True

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),
                               options=options)
    driver.get("https://ucheck.utoronto.ca")

    username_box = driver.find_element(By.ID, "username")
    username_box.send_keys(username)

    password_box = driver.find_element(By.ID, "password")
    password_box.send_keys(password)

    submit_button = driver.find_element(By.NAME, "_eventId_proceed")
    submit_button.click()

    return driver

def run_questionnaire(driver: webdriver) -> None:

    driver.implicitly_wait(5)

    start_questionnaire = driver.find_element(By.XPATH,
                                              "/html/body/div[1]/div[2]/div/div/div[2]/button/span[1]")
    hover = ActionChains(driver).move_to_element(start_questionnaire)
    hover.perform()
    start_questionnaire.click()

    question_1 = driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[6]/div/div/div/div/div/div/div/div/fieldset/label[2]/span")
    driver.execute_script("arguments[0].scrollIntoView(true);", question_1)
    hover = ActionChains(driver).move_to_element(question_1)
    hover.perform()
    question_1.click()

    question_2 = driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[8]/div/div/div/div/div/div/div/div/fieldset/label[1]/span")
    driver.execute_script("arguments[0].scrollIntoView(true);", question_2)
    hover = ActionChains(driver).move_to_element(question_2)
    hover.perform()
    question_2.click()

    question_3 = driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[10]/div/div/div/div/div/div/div/div/fieldset/label[1]/span")
    driver.execute_script("arguments[0].scrollIntoView(true);", question_3)
    hover = ActionChains(driver).move_to_element(question_3)
    hover.perform()
    question_3.click()

    question_4 = driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[12]/div/div/div/div/div/div/div/div/fieldset/label[1]/span")
    driver.execute_script("arguments[0].scrollIntoView(true);", question_4)
    hover = ActionChains(driver).move_to_element(question_4)
    hover.perform()
    question_4.click()

    question_5 = driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[14]/div/div/div/div/div/div/div/div/fieldset/label[1]/span")
    driver.execute_script("arguments[0].scrollIntoView(true);", question_5)
    hover = ActionChains(driver).move_to_element(question_5)
    hover.perform()
    question_5.click()

    question_6 = driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[16]/div/div/div/div/div/div/div/div/fieldset/label[1]/span")
    driver.execute_script("arguments[0].scrollIntoView(true);", question_6)
    hover = ActionChains(driver).move_to_element(question_6)
    hover.perform()
    question_6.click()

    question_7 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/form/div[18]/div/div/div/div/div/div/div/div/fieldset/label[1]/span")
    driver.execute_script("arguments[0].scrollIntoView(true);", question_7)
    hover = ActionChains(driver).move_to_element(question_7)
    hover.perform()
    question_7.click()

    final_submit = driver.find_element(By.XPATH,
                                       "/html/body/div[1]/div/div/div/div[2]/main/div/div/div/div/div/button/span[1]")
    driver.execute_script("arguments[0].scrollIntoView(true);", final_submit)
    hover = ActionChains(driver).move_to_element(final_submit)
    hover.perform()
    final_submit.click()
    print("UCheck successfully completed.")


if __name__ == "__main__":
    firefox_driver = setup()
    run_questionnaire(firefox_driver)
    firefox_driver.quit()
