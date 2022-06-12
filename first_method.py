import time
import pyautogui
import pandas as pd
import datetime
import subprocess 


def sign_in(meetingid, pswd):
    subprocess.call(['/usr/bin/open', "/Applications/zoom.us.app"])

    time.sleep(5)

    join_btn = pyautogui.locateCenterOnScreen('join_button.png')
    print(join_btn)
    pyautogui.moveTo(join_btn.x/2, join_btn.y/2,)
    pyautogui.click()

    time.sleep(1)
    meeting_id_btn= pyautogui.locateCenterOnScreen('meeting_id_button.png', confidence=0.9)
 
    print(meeting_id_btn)
    pyautogui.moveTo(meeting_id_btn.x/2, meeting_id_btn.y/2)
    pyautogui.click()
    pyautogui.write(meetingid)

    blank_buttons=pyautogui.locateAllOnScreen('blank_button.png', confidence=0.9)
#    for buttons in blank_buttons:
 #       button_x, button_y=buttons
 #       pyautogui.moveTo(button_x/2, button_y/2)
 #       pyautogui.click()
 #       time.sleep(1.5)

    last_join_button= pyautogui.locateCenterOnScreen('last_join_buttton.png')
    pyautogui.moveTo(last_join_button.x/2,last_join_button.y/2)
    pyautogui.click()

    # meeting_pswd_btn= pyautogui.locateOnScreen("meeting_password_button.png", confidence=0.9)
 #   pyautogui.moveTo(meeting_pswd_btn.x/2, meetin_pswd_btn.y/2)
 #   pyautogui.click()
 #   pyautogui.write(pswd)
 #   pyautogui.press('enter')

df = pd.read_csv('data.csv')

while True:
    now= datetime.datetime.now().strftime("%H:%M")

    if now in str(df['timings']):
        row= df.loc[df['timings']==now]
        m_id = str(row.iloc[0,1])
        m_pswd = str(row.iloc[0,2])
        
        sign_in(m_id, m_pswd)
        time.sleep(40)