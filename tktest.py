import tkinter as tk
from tkinter import *
import requests
from tkinter import messagebox as mbox
window = tk.Tk()
 

def action_go():
	passw = entry.get()
	action_go1(passw)

def action_go1(a):
	config_file = open("config.txt","r")
	host = config_file.read().split(" ")[0]
	ans = requests.get("http://{}:5000/getpasses/{}".format(host,a)) #request to key server
	if ans.text == "-1":
		print("This password is incorrect! Please try again later")
		mbox.showerror("Ошибка", "Неверный пароль")
	else:
		print("STR", str(a))
		if str(a) == "111111":
			#dvoynoe dno
			tmpl = "{}:\nLogin:{}\nPass:{}\nHost:{}\n"
			splitted = ans.text.split(" ")
			createNewWindow(tmpl.format(splitted[2], splitted[3],splitted[4],splitted[5]))
		else:
			print("Standart access")
			splitted = ans.text.split(" ")
			tmpl = "{}:\nLogin:{}\nPass:{}\nHost:{}\n"
			createNewWindow(tmpl.format(splitted[0], splitted[1],splitted[2],splitted[3]))
def createNewWindow(data):
	newWindow = tk.Toplevel(window)
	labelExample = tk.Label(newWindow, text = "Data is:")
	text = Text(width=25, height=5,wrap=WORD)
	text.insert(1.0,data)
	labelExample.pack()
	text.pack()

		
button = tk.Button(
    text="Нажми на меня!",
    width=15,
    height=5,
    command=action_go
)
quitb = tk.Button(text="Выйти", 
                   fg="red",
                   command=quit)
greeting = tk.Label(text="Введите пароль и нажмите кнопку ниже")
entry = tk.Entry(width=50)
greeting.pack()
entry.pack()
button.pack()
quitb.pack()
window.mainloop()
