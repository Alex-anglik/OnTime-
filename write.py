import csv 
from tkinter import *



with open('data.csv', 'w+') as file:
    data = csv.writer(file)
    data.writerow(['timings','meetingid','meetingpswd'])
    num = int(input("how many meetings do you want to plan?"))
    for i in range(num):
        time = input('what time is the meeting you want to attend?')
        id= input("what is the meeting id?")
        pswd=input("what is the password to that meeting?")
        data.writerow([time,id,pswd])

