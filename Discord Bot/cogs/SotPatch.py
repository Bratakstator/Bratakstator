#For the code to work with discord
import discord
from discord.ext import commands

#For webscraping
import requests
from bs4 import BeautifulSoup

class SotPatch(commands.Cog):

	def __init__(self, client):
		self.client = client
	
	@commands.command()
	async def scrape(self, ctx): # When '.scape' is called the bot will go through the sea of thieves website for the newest patch note (temporary fix, will be automated soon)
		print(f'User {ctx.author} in the server "{ctx.guild.name}" requested scrape in {ctx.channel}')
		URL = "https://www.seaofthieves.com/whats-new?filters[]=majorRelease&filters[]=patchNotes" # link to sea of thieves patch notes page
		page = requests.get(URL)

		soup = BeautifulSoup(page.content, "html.parser")
		results = soup.find(id="content") # Looks for all HTML lines containing the class 'content'

		updates = results.find_all("a", class_="list-item__link") # Looks for all a lines in the HTML code with the class 'list-item__link'
		
		versions = [] # Creates a list for all patch notes on the website
		for update in updates:
			link = update["href"] # Looks for the links in the HTML files found in the previous search
			versions.append(link) # Appends the links in the list
			
		versions.sort(reverse=True) # Sorts the links from highest to lowest number (newest patch has the highest number)
		await ctx.send(f"https://www.seaofthieves.com{versions[0]}") # Prints out the first item in the list.
	
def setup(client):
	client.add_cog(SotPatch(client))
