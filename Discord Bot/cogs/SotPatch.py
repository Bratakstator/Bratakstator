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
	async def scrape(self, ctx):
		print(f'User {ctx.author} in the server "{ctx.guild.name}" requested scrape in {ctx.channel}')
		URL = "https://www.seaofthieves.com/whats-new?filters[]=majorRelease&filters[]=patchNotes"
		page = requests.get(URL)

		soup = BeautifulSoup(page.content, "html.parser")
		results = soup.find(id="content")

		updates = results.find_all("a", class_="list-item__link")
		
		versions = []
		for update in updates:
			link = update["href"]
			versions.append(link)
			
		versions.sort(reverse=True)
		await ctx.send(f"https://www.seaofthieves.com{versions[0]}")
	
def setup(client):
	client.add_cog(SotPatch(client))
