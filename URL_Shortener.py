from tkinter import *
import pyshorteners

  # Function for short URL and set value in textbox
def convert():
      s = pyshorteners.Shortener().tinyurl.short(url.get())
      shorturl.set(s)
root = Tk()
root.title(" URL Shortner")
root.geometry("400x350")
root.resizable(False, False)
root.config(background="#e6e5e5")
  # Declare variables
url = StringVar()
shorturl = StringVar()
  # Design labels
Label(root, text="*** Welcome to URL Shortner \nBy Tanay Choubey ***", bg="#e6e5e5", fg="black", font=('lato black', 12, 'bold')).place(x=80, y=10)

  # Accepting URL as a Input
Label(root, text="Enter URL Here ", bg="#e6e5e5", fg="black", font="verdana 10 bold"
              , padx=2, pady=2).place(x=7, y=100)
Entry(root, textvariable=url, font="verdana 12", width=30).place(x=7, y=120)
  # Creating button to give a call for convert function
Button(root, text="Convert", bg="#e6e5e5", fg="red", font="verdana 12 "
          , command=convert, relief=GROOVE).place(x=7, y=180)
  # Displaying shortened URL
Label(root, text="Shortened URL - Copy & Paste in browser", bg="#e6e5e5", fg="black"
              , font="verdana 10 bold", padx=2, pady=2).place(x=7, y=250)
Entry(root, textvariable=shorturl, width=35, font="verdana 12").place(x=7, y=270)

root.mainloop()