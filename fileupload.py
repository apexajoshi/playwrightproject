import pathlib
from tkinter import dialog

from playwright.sync_api import sync_playwright, Locator


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()
        context = browser.new_context()



        #page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")

        page.goto("https://cgi-lib.berkeley.edu/ex/fup.html")

       # page.set_input_files("input#filesToUpload",  "auth.json")

       # page.wait_for_timeout(5000)

        #FOR REMOVE FILES
       # page.set_input_files("input#filesToUpload", [])

       # page.wait_for_timeout(5000)

        #multiple files upload

       # page.set_input_files('input#filesToUpload', ['auth.json', 'state.json'])

      #  page.wait_for_timeout(5000)
        # FOR REMOVE multiple FILES
      #  page.set_input_files("input#filesToUpload", [])

        page.wait_for_timeout(5000)

        # make runtime file and upload it
      #  page.set_input_files('input#filesToUpload', files= [
       #             {"name": "test.txt", "mimeType": "text/plain", "buffer": b"this is a test"}
        #        ],)

        page.set_input_files("input[name = 'upfile']", FIle=[
            {"name": "test.txt", "mimeType": "text/plain", "buffer": b"this is a test"}
        ], )
        page. click("input[value ='Press']")
        page.wait_for_timeout(10000)




       # page.wait_for_timeout(5000)
       # browser.close()




if __name__ == '__main__':
    main()
