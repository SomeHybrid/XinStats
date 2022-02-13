from dotenv import load_dotenv
import discord
import os
import main
import xincraft

bot = discord.Bot()
load_dotenv()
client = xincraft.AsyncClient(os.getenv("XINCRAFT_KEY"))

@bot.event
async def on_ready():
    print("----- XinStats -----")
    print("Bot Information:")
    print(f"Bot User ID: {bot.user.id}")
    print(f"Bot Name {bot.user.name}")
    print("--------------------")

main.setup(bot)
bot.run(os.getenv("DISCORD_TOKEN"))