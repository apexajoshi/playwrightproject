import pathlib
from tkinter import dialog

from playwright.sync_api import sync_playwright, Locator


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()
        context = browser.new_context()



        page.goto("https://the-internet.herokuapp.com/javascript_alerts")



      #  page.on("dialog", lambda dialog:   dialog.accept("My name is apexa"))
       # page.wait_for_timeout(5000)
       # page.on("dialog", lambda dialog:print(dialog.message))
       # print(dialog.message)



        page.click("//button[text()='Click for JS Alert']")
        result = page.text_content("#result")
        print(result)


        page.click("//button[text()='Click for JS Confirm']")
        result = page.text_content("#result")
        print(result)

        page.locator("//button[text()='Click for JS Prompt']").click()  # Will hang here
        result = page.text_content("#result")

        print(result)


       # page.wait_for_timeout(5000)
       # browser.close()




if __name__ == '__main__':
    main()
