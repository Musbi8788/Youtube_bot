import os
import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

EMAIL_ADD_YOUTUBE = os.getenv("EMAIL_ADD_YOUTUBE")
PASSWORD_YOUTUBE = os.getenv("PASSWORD_YOUTUBE")

SEARCH_KEY = "why lean coding "
SEARCH_TITLE = "Why Learn Coding? - Steve Jobs, Bill Gates, Mark Zuckerberg, Mark Cuban, Elon Musk | Simplilearn"

COMMENT_TEXT = "Keep pushing those keys, fellow programmer! Every bug you fix, every line of code you write, brings you closer to greatness. Remember, even the best coders started where you are today. You've got this! 🚀💻 #KeepCoding"

FILE_PATH = r"C:/Development/chromedriver-win64/chromedriver.exe"

server = Service(executable_path=FILE_PATH)
driver = webdriver.Chrome(service=server)
driver.get("https://www.youtube.com")

try:
    # sign in  with your email account in to subscribe or like a video.

    time.sleep(5)
    sing_in = driver.find_element(By.XPATH, '//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a')
    sing_in.click()

    # the is slow internet wait for 5s to take an action
    time.sleep(5)
    # enter your email address
    email_ac = driver.find_element(By.NAME, "identifier")
    email_ac.send_keys(EMAIL_ADD_YOUTUBE)

    # click on the next button
    time.sleep(5)
    click_next = driver.find_element(By.CSS_SELECTOR, ".TNTaPb div")
    click_next.click()

    # enter your password
    time.sleep(5)
    password = driver.find_element(By.NAME, "Passwd")
    password.send_keys(PASSWORD_YOUTUBE)

    # click the next button
    time.sleep(5)
    click_next = driver.find_element(By.CSS_SELECTOR, ".TNTaPb div")
    click_next.click()

    # make your query search
    time.sleep(5)
    search_bar = driver.find_element(By.NAME, "search_query")
    search_bar.send_keys(SEARCH_KEY)
    search_bar.send_keys(Keys.ENTER)

    # click on the query result that i want to watch!!!
    time.sleep(5)
    search_title = driver.find_element(By.PARTIAL_LINK_TEXT, f"{SEARCH_TITLE}")
    search_title.click()

    # subscribe
    time.sleep(5)
    subscribe = driver.find_element(By.ID, "subscribe-button")
    subscribe.click()

    # like
    like_button = driver.find_element(By.CLASS_NAME, "YtLikeButtonViewModelHost")
    like_button.click()

    # move to the  comment section after 10s
    time.sleep(10)
    move_to= driver.find_element(By.ID,"sections")
    driver.execute_script("arguments[0].scrollIntoView(true);", move_to)


    comment = driver.find_element(By.XPATH, "//div[@id='placeholder-area']")
    time.sleep(3)
    # click the comment textarea
    ActionChains(driver).move_to_element(comment).click().perform()

    # type the comment message  after waiting for  5s.
    time.sleep(5)
    comment_mass = driver.find_element(By.XPATH, '//*[@id="contenteditable-root"]')
    comment_mass.send_keys(COMMENT_TEXT)

    # post the comment
    submit_button = driver.find_element(By.ID, "submit-button")
    submit_button.click()

    print("Happy coding feel free to watch your amazing video!!")

except NoSuchElementException :
    print("NoSuchElementException Retry Again")

except ElementNotInteractableException:
    print("ElementNotInteractableException Rerun")

# EXIST THE WINDOW AFTER 5 MIN
time.sleep(300)
driver.quit()