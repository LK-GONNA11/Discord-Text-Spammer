import os
import time
import platform
import subprocess
import sys

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_spam_settings():
    message = input("Enter message to spam: ")
    try:
        repetitions = int(input("How many times to repeat: "))
        unit = input("Delay unit (s/ms): ").strip().lower()
        delay_input = float(input(f"Enter delay in {unit}: "))
        if repetitions <= 0 or delay_input < 0:
            print("Invalid values.")
            return None, None, None
        delay = delay_input / 1000 if unit == "ms" else delay_input
        return message, repetitions, delay
    except ValueError:
        print("Invalid number.")
        return None, None, None

def choose_browser():
    while True:
        clear_terminal()
        choice = input("Choose browser (chrome/firefox): ").lower()
        if choice in ["chrome", "firefox"]:
            return choice
        else:
            print("Invalid choice. Choose 'chrome' or 'firefox'.")
            time.sleep(1)

def launch_browser(browser):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    try:
        driver = webdriver.Chrome() if browser == "chrome" else webdriver.Firefox()
        clear_terminal()
        driver.get("https://discord.com/login")
        print("Log in to Discord in browser window.")
        input("Press Enter once logged in and on server...")
        return driver
    except Exception as e:
        print(f"Error launching {browser.capitalize()}: {e}")
        return None

def spam_in_browser(driver, message, repetitions, delay):
    from selenium.webdriver.common.keys import Keys
    try:
        clear_terminal()
        print("Spam starts in active text field of Discord page.")
        input("Press Enter to start spamming...")
        for i in range(repetitions):
            driver.switch_to.active_element.send_keys(message)
            driver.switch_to.active_element.send_keys(Keys.RETURN)
            time.sleep(delay)
        clear_terminal()
        print(f"Message '{message}' sent {repetitions} times with {delay} second(s) delay.")
    except Exception as e:
        print(f"Error during spamming: {e}")
        if driver:
            driver.quit()
        exit()

if __name__ == "__main__":
    clear_terminal()
    print("Detected: PC / Non-Termux system")
    browser = choose_browser()
    driver = launch_browser(browser)
    if driver:
        message, reps, delay = get_spam_settings()
        if message:
            spam_in_browser(driver, message, reps, delay)
        input("Press Enter to close browser...")
        driver.quit()
