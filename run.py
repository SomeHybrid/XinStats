from dotenv import load_dotenv
import discord
import os
import maincog

bot = discord.Bot()
load_dotenv()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="XinCraft Stats"))
    print("----- XinStats -----")
    print("Bot Information:")
    print(f"Bot User ID: {bot.user.id}")
    print(f"Bot Name {bot.user.name}")
    print("--------------------")

maincog.setup(bot)
bot.run(os.getenv("DISCORD_TOKEN"))