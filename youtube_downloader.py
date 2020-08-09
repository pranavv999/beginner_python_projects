# Simple YouTube downloader

#Importing tkinter and pytube module
#you need to download pytube module using "pip isntall pytube" if error occures try "pip install pytube3"
import tkinter as tk
from pytube import YouTube

#Initializing Tkinter
root = tk.Tk()

#creating GUI geometry
root.geometry("500x350")

#setting title of GUI
root.title("Youtube Video Downloader")

#Welcoming user
greet = tk.Label(root, text="Welcome to YouTube Video\nDownloader Application", font="verdana 18  bold", fg='red' )
greet.pack(pady=15)

#creating entry widget to ask user for url
myVar = tk.StringVar()
myVar.set("Enter the Link Below")
entry = tk.Entry(root, justify="center", text=myVar )
entry.pack(pady=30)

#Entry widget to get the link
link = tk.StringVar()
entry1 = tk.Entry(root, justify='center', text=link, font='Consolas 12 bold', width=40)
entry1.pack(pady=20)

#creating download function
def download():
	try:
		YouTube(link.get()).streams.first().download()
		myVar.set("Downloading...")
		root.update()
		link.set("Video Downloaded Successfully!")
		myVar.set("Enter the Link Below")

	except:
		link.set("Invalid Link or Network Error")
		root.update()

#creating Download button
button = tk.Button(root, bg='red',text='Download Video', font='italic', command=download)
button.pack(pady=20)

#running main loop
root.mainloop()