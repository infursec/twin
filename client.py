import requests


def get_connect_data(a):
	print("gc", a)
	config_file = open("config.txt","r")
	host = config_file.read().split(" ")[0]
	print("host")
	a = requests.get("http://{}:5000/getpasses/{}".format(host,a))
	print(a.text)
	if a.text == "-1":
		print("This password is incorrect! Please try again later")
		


def do_login():
	print("Logging in...")
	a = input("Please enter your password")
	print("Password is: ", a)
	get_connect_data(a)





print("Welcome to the our system. Please enter action:")
print("1. Start")
print("2. Exit")
print("3. Setup")
sel = input("Enter your option: (1/2)")
if sel == "1":
	do_login()
elif sel == "2":
	print("Goodbye")
elif sel == "3":
	print("")