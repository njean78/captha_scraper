from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
from random import uniform
from time import sleep
from faker import Faker
from scipy.io import wavfile

import sys
import logging
import random
import os
import urllib
import time
import audio
import threading
import argparse

import pyaudio
import wave
import uuid


# use the max amplitude to filter out pauses
AMP_THRESHOLD = 2500
ATTACK_AUDIO = True
ATTACK_IMAGES = False
ATTACK_REDDIT = False
CHROMEDRIVER_PATH = ""
LEVEL = logging.DEBUG

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("--image", action='store_true', help="attack image recaptcha")
group.add_argument("--audio", action='store_true', help="attack audio recaptcha")
parser.add_argument("--driver", action="store", help="specify custom chromedriver path")
parser.add_argument("--reddit", action="store_true", help="run attack against Reddit's recaptcha")
parser.add_argument("--level", action="store", help="set log level", default="debug", choices=("debug", "warning"))

args = parser.parse_args()
ATTACK_IMAGES = args.image
ATTACK_AUDIO = args.audio
ATTACK_REDDIT = args.reddit
CHROMEDRIVER_PATH = args.driver


############################## UTIL FUNCTIONS #############################
def init(task_type):
    global TASK_PATH, TASK_DIR, TASK_NUM, TASK
    TASK_DIR = os.path.join(task_type, "task")
    TASK_NUM = 1

    while os.path.isdir(TASK_DIR+str(TASK_NUM)):
        TASK_NUM += 1
    if not os.path.isdir(TASK_DIR+str(TASK_NUM)):
        os.mkdir(TASK_DIR+str(TASK_NUM))
        logging.info("Making "+ TASK_DIR+str(TASK_NUM))
    TASK = "task"+str(TASK_NUM)
    TASK_PATH = os.path.join(task_type, TASK)


def wait_between(a, b):
    rand = uniform(a, b)
    sleep(rand)


############################## IMAGE RECAPTCHA ##############################
TASK_PATH = "images/taskg"

def get_numbers(wav_file, parent_dir):
    return audio.getNums(parent_dir, [wav_file,])

def type_like_bot(driver, element, string):
    driver.find_element(By.ID, element).send_keys(string)
    wait_between(0.5, 2)

def type_like_human(driver, element, string):
    driver.find_element(By.ID, element).click()
    for c in string:
        driver.find_element(By.ID, element).send_keys(c)
        wait_between(0.0, 0.1)
    wait_between(0.5, 2)

type_style = type_like_bot

# def fill_out_profile(driver):
#     fake = Faker()
#     user = fake.simple_profile()
#     username = user["username"]
#     email = user["mail"].replace("@", str(random.randint(10000, 99999))+"@")
#     password = fake.password()
#     wait_between(1, 2)
#     type_style(driver, "user_reg", username)
#     type_style(driver, "passwd_reg", password)
#     type_style(driver, "passwd2_reg", password)
#     type_style(driver, "email_reg", email)

## https://www.reddit.com/r/learnpython/comments/2dqpaw/pyaudio_how_to_capture_microphone_and_system/


def audioRecord():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 60
    WAVE_OUTPUT_FILENAME = "C:/tmp/%s.wav"%uuid.uuid4()

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index = 0,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return WAVE_OUTPUT_FILENAME

ele.click()
audioRecord()
##############################  MAIN  ##############################
def main():
    logging.basicConfig(stream=sys.stderr, level=LEVEL)
    ## set chrome options, like incognito mode
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-bundled-ppapi-flash")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36")
    chrome_options.add_argument("--disable-plugins-discovery")

    ## start chrome
    driver = webdriver.Chrome(chrome_options=chrome_options)

    ## get rid of the cookies
    driver.delete_all_cookies()
    agent = driver.execute_script("return navigator.userAgent")
    logging.debug("[*] Cookies cleared")
    logging.debug("[ ] Starting driver with user agent %s" % agent)

    logging.info("[*] Starting attack on agenziaentrate.gov recaptcha")
    driver.get("https://telematici.agenziaentrate.gov.it/VerificaPIVA/Scegli.do?parameter=verificaPiva")
    # driver.find_element(By.XPATH, "//*[@id=\"header-bottom-right\"]/span[1]/a").click()
    # logging.debug("[*] Filling out Reddit registration form")
    # fill_out_profile(driver)
    # WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"register-form\"]/div[6]/div/div/div/iframe")))
    #ele = driver.find_element(By.ID, "captchaDiv")
    ele = driver.find_element(By.ID, "audioCaptchaSpan")
    ele.click()
    wave_file = audioRecord()
    driver.delete_all_cookies()

    return ele, wave_file

def guess(wave_file):
    guess_again = True

    while guess_again:
        init("audio")
        guess_str = get_numbers(wave_file, "C:/tmp/")

def puppa():
    #ActionChains(driver).move_to_element(iframeSwitch).perform()
    driver.delete_all_cookies()
    logging.info("[*] Recaptcha located. Engaging")
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "recaptcha-anchor")))
    ele = driver.find_element(By.ID, "recaptcha-anchor")
    #ActionChains(driver).move_to_element(ele).perform()
    ele.click()
    driver.switch_to.default_content()

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[title=\"recaptcha challenge\"]")))
    iframe = driver.find_element(By.CSS_SELECTOR, "iframe[title=\"recaptcha challenge\"]")
    driver.switch_to.frame(iframe)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "rc-imageselect")))

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "recaptcha-audio-button")))
    time.sleep(1)
    driver.find_element(By.ID, "recaptcha-audio-button").click()

    guess_again = True

    while guess_again:
        init("audio")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "audio-source")))
        # Parse table details offline
        body = driver.find_element(By.CSS_SELECTOR, "body").get_attribute('innerHTML').encode("utf8")
        soup = BeautifulSoup(body, 'html.parser')
        link = soup.findAll("a", {"class": "rc-audiochallenge-tdownload-link"})[0]
        urllib.urlretrieve(link["href"], TASK_PATH + "/" + TASK + ".mp3")

        guess_str = get_numbers(TASK_PATH + "/" + TASK, TASK_PATH + "/")
        type_style(driver, "audio-response", guess_str)
        # results.append(guess_str)
        wait_between(0.5, 3)
        driver.find_element(By.ID, "recaptcha-verify-button").click()
        wait_between(1, 2.5)
        try:
            logging.debug("Checking if Google wants us to solve more...")
            driver.switch_to.default_content()
            driver.switch_to.frame(iframeSwitch)
            checkmark_pos = driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-checkmark").get_attribute("style")
            guess_again = not (checkmark_pos == "background-position: 0 -600px")
            driver.switch_to.default_content()
            iframe = driver.find_element(By.CSS_SELECTOR, "iframe[title=\"recaptcha challenge\"]")
            driver.switch_to.frame(iframe)
        except Exception as e:
            print e
            guess_again = False

    input("")
main()
# test_all()
