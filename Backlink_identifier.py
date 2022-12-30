from msilib import MSIMODIFY_REPLACE
import requests
from bs4 import BeautifulSoup
import tkinter
from urllib import request
from urllib.request import Request, urlopen
import pyperclip

list1 = ["youtube.com/channel/","discord.gg/", "youtube.com/watch?v=","imgur.com/"]
leng = {"imgur.com/":7, "pastebin.com/":8,"reddit.com/":5,"tinyurl.com/":8,"bit.ly/":7,"youtube.com/channel/":24, "youtube.com/watch?v=":11,"discord.gg/":8,"vimeo.com/":9,"imgflip.com/i/":6,"drive.google.com/file/d/":44}
click = 0
fin = ""
def isvalid(url,site):
	request = requests.get(url)
	if not site in list1:
		if request.status_code == 200:
			return True
		else:
			return False
	else:
		#print("here")
		response = Request(url,headers={"User-Agent": "Mozilla/5.0"})
		response = urlopen(response)
		if "youtube" in site and "watch" in site:
			for line_number, line in enumerate(response):
			#	print(line_number,line)
				if line_number == 25:
					fin = str(line)
					break
			if "errorScreen" in fin:
				return False
			else:return True
		elif "youtube" in site and "channel" in site:
			
			for line_number, line in enumerate(response):
			#	print(line_number)
				#print(line)
				if line_number == 25:
					fin = str(line)
					break
			if "channel does not exist" in fin:
				return False
			else:return True
		elif "discord" in site:
			for line_number, line in enumerate(response):
				if line_number == 7:
					fin = str(line)
					break
			if "Join" in fin:
				return True
			else:return False
		elif "imgur" in site:
			for line_number, line in enumerate(response):
				if line_number == 0:
					fin = str(line)
					break
			if "image:width" in fin:
				return True
			else:return False
			
def myClick():
	global click
	global mybutton
	global fin
	click +=1
	if click ==1:
		mybutton.destroy()
		copy = tkinter.Button(root,text = "Copy Link",command=myCopy,bg = 'darkblue',fg = "white",width = 7,height = 3,font=("Comic Sans MS", 14))#.grid(row=8,column=1)
		copy.grid(row=7,column=1)
		bkl = e.get()
		fin = checker(bkl)
		mylabel = tkinter.Label(root, text = fin,bg = "cyan",font=("Comic Sans MS", 26))
		mylabel.grid(row = 9,column=1)

	

			#print(request.text)
		#	try:
   		##		invite = await bot.fetch_invite(URL_OR_ID_HERE)
   		##		await ctx.send("Sorry, that invite was invalid or has expired.")



		#	else:return False
			
def checker(backlink):
	backlink = str(backlink).strip()
	keys = [k for k, v in leng.items() if v == len(backlink)]
	for i in range(len(keys)):
		url = "https://www."+ keys[i] + backlink
		if isvalid(url,keys[i]):
			return url
	return "Invalid backlink"

def myCopy():
	global fin
	pyperclip.copy(fin)


root = tkinter.Tk()
root.configure(background='cyan')
main = tkinter.Label(root,text = "Backlink Detector",bg="cyan",fg = "darkblue",font=("Comic Sans MS", 44))#.grid(row = 3,column = 1)
text1 = tkinter.Label(root,text = "Enter Backlink",bg="cyan",font=("Comic Sans MS", 32))#.grid(row = 3,column = 1)
e = tkinter.Entry(root,width=50,borderwidth = 5,font=("Comic Sans MS", 	24))#.grid(row = 6,column = 1)
mybutton = tkinter.Button(root,text = "Submit",command=myClick,bg = 'darkblue',fg = "white",width = 7,height = 3,font=("Comic Sans MS", 14))#.grid(row=8,column=1)
text2 = tkinter.Label(root,text = "",bg="cyan",font=("Comic Sans MS", 32))#.grid(row = 3,column = 1)
text3 = tkinter.Label(root,text = "",bg="cyan",font=("Comic Sans MS", 32))

main.grid(row=0,column=1)
text1.grid(row = 3,column=1)
e.grid(row = 5, column= 1)
text2.grid(row=6,column=1)
text3.grid(row=8,column=1)
mybutton.grid(row = 7,column=1)

#text1.grid(row=0,column=1)
root.mainloop()