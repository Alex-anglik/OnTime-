import schedule
import time
import webbrowser


def open_link(link):
    webbrowser.open(link)

def meeting():
    open_link("https://us02web.zoom.us/j/89252729854?pwd=RW5yYm00eFpabExuZVoyZ1FmWjgvUT09")

schedule.every().saturday.at("19:04").do(meeting)

while 1:
    schedule.run_pending()
    time.sleep(1)

