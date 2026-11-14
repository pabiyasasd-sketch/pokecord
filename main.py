import discord
from discord.ext import commands
from flask import ctx
from config import token
from logic import Pokemon

# Setting up intents for the bot
intents = discord.Intents.default()  # Getting the default settings
intents.messages = True              # Allowing the bot to process messages
intents.message_content = True       # Allowing the bot to read message content
intents.guilds = True                # Allowing the bot to work with servers (guilds)

# Creating a bot with a defined command prefix and activated intents
bot = commands.Bot(command_prefix='!', intents=intents)

# An event that is triggered when the bot is ready to run
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')  # Outputs the bot's name to the console
    await ctx.send("yo whats up")  # Sends a message to the channel indicating that the bot is ready

# The '!go' command
@bot.command()
async def go(ctx):
    author = ctx.author.name  # Getting the name of the message's author
    # Check whether the user already has a Pokémon. If not, then...
    if author not in Pokemon.pokemons.keys():
        pokemon = Pokemon(author)  # Creating a new Pokémon
        await ctx.send(await pokemon.info())  # Sending information about the Pokémon
        image_url = await pokemon.show_img()  # Getting the URL of the Pokémon image
        if image_url:
            embed = discord.Embed()  # Creating an embed message
            embed.set_image(url=image_url)  # Setting up the Pokémon's image
            await ctx.send(embed=embed)  # Sending an embedded message with an image
        else:
            await ctx.send("Failed to upload an image of the pokémon.")
    else:
        await ctx.send("You've already created your own Pokémon.")  # A message that is printed whether a Pokémon has already been created

@bot.command()
async def remove(ctx):
    author = ctx.author.name  # Getting the name of the message's author
    if author in Pokemon.pokemons.keys():
        del Pokemon.pokemons[author]  # Deleting the Pokémon from the dictionary
        await ctx.send("Your Pokémon has been removed.")  # Sending a confirmation message
    else:
        await ctx.send("You don't have a Pokémon to remove.")  # A message that is printed if the user doesn't have a Pokémon
# Running the bot
bot.run(token)
