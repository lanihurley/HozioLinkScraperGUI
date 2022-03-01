"""
Program: HozioLinkScraper.py
Date: 1/17/2022
Author: Lani Hurley
Program scrapes links from webpage
* Must import packages and have breezypythongui file in same folder as file.
* Must have image file HozioLogo.png in same folder as file
*Must Import Python requests, BeautifulSoup, tkinter packages
"""

import requests
from breezypythongui import EasyFrame
from bs4 import BeautifulSoup
from tkinter import *

class HozioLinkScraper(EasyFrame):
	def __init__(self):
		EasyFrame.__init__(self, title="HOZIO, Inc. Web Sraper Tool", background="steel blue")
		# Logo Image
		self.imageLabel = self.addLabel(text="", row=0, column=0, columnspan=3, background="steel blue", sticky="NSEW")
		# Load the image and associate it with the image label
		self.image = PhotoImage(file="HozioLogo.png")
		self.imageLabel["image"] = self.image
		# Label and field for the input and output
		self.addLabel(text = "Enter Website to be Scraped", background="steel blue", row = 4, rowspan=2, column = 0, font="Rajdhani", foreground="white", sticky="W")
		self.inputField = self.addTextField(text = "https://", row = 4, column = 0, width = 50, sticky="E")
		self.outputArea = self.addTextArea(text = "", row = 1, column = 0, columnspan = 3, height= 20, wrap="word")
		# The command button
		self.button = self.addButton(text = "Click to Get Links", row = 4, column = 1, command = self.is_valid)

	def is_valid(self):
		# grab the user input and put it in a variable
		web_page_entered = self.inputField.get()
		# concatenate requests module to get() method and put it in a variable
		response = requests.get(web_page_entered)
		# create variable to hold text of url string components
		web_p = response.text
		# pass it to Beautiful soup to be parsed into individual tags within the html
		soup = BeautifulSoup(web_p, "html.parser")
		# create a variable to hold all "a" tags in html webpage
		all_anchor_tags = soup.find_all(name="a")
		# create variable to hold string data
		links_str = ""
		# create for() loop to search through the parsed text data and retrieve all "a" and "href"
		for anchor_tag in all_anchor_tags:
			link = anchor_tag.get("href") + "\n"
			# create a new variable to hold on to and combine the links into a string to print out
			links_str = links_str + link
			# display the links in outputArea
		self.outputArea.setText(links_str)
		self.outputArea["state"] = "disabled"

# definition of the main() function for program entry
def main():
	HozioLinkScraper().mainloop()
# global call to trigger the main() function
if __name__ == "__main__":
	main()
