from dotenv import load_dotenv
from discord import commands
import discord
import xincraft
import os
import aiohttp
import redis

load_dotenv()


class Main(discord.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = xincraft.AsyncClient(os.getenv("XINCRAFT_KEY"))
        self.db = redis.Redis()

    @commands.slash_command()
    async def stats(self, ctx, username: str = "linked  "):
        try:
            if username == "linked  ":
                try:
                    username = self.db[str(ctx.author.id)].decode("utf-8")
                    data = await self.client.get_user(username)
                except KeyError:
                    embed = discord.Embed(title="Error!", description="You have not linked your account!", color=0xFF0000)
                    await ctx.respond(embed=embed, ephemeral=True)
                    return
            else:
                data = await self.client.get_user(username)
        except aiohttp.client_exceptions.ContentTypeError as e:
            embed = discord.Embed(title="Error!", description="This user does not exist!", color=0xFF0000)
            await ctx.respond(embed=embed, ephemeral=True)
            return

        try:
            overall = data.stats.overall
            solos = data.stats.solos
            duos = data.stats.doubles
            trios = data.stats.trios
            fours = data.stats.fours
            cosmetics = data.cosmetics
            embed = discord.Embed(title=f"{username}'s stats", color=0xFFD700)
            embed.add_field(
                name="Overall",
                value=f"""
                • Wins: `{int(overall.wins)}`
                • Losses: `{int(overall.losses)}`
                • Draws: `{int(overall.draws)}`
                • Kills: `{int(overall.kills)}`
                • Deaths: `{int(overall.deaths)}`
                • Goals: `{int(overall.goals)}`
                • Best winstreak: `{int(overall.bestws)}`
                • Winstreak: `{int(overall.ws)}`
                • KDR: `{round(overall.kdr, 2)}`
                • WLR: `{round(overall.wlr, 2)}`
                """
            )
            embed.add_field(
                name="Solos",
                value=f"""
                • Wins: `{int(solos.wins)}`
                • Losses: `{int(solos.losses)}`
                • Draws: `{int(solos.draws)}`
                • Kills: `{int(solos.kills)}`
                • Deaths: `{int(solos.deaths)}`
                • Goals: `{int(solos.goals)}`
                • Best winstreak: `{int(solos.bestws)}`
                • Winstreak: `{int(solos.ws)}`
                • KDR: `{round(solos.kdr, 2)}`
                • WLR: `{round(solos.wlr, 2)}`
                """
            )
            embed.add_field(
                name="Duos",
                value=f"""
                • Wins: `{int(duos.wins)}`
                • Losses: `{int(duos.losses)}`
                • Draws: `{int(duos.draws)}`
                • Kills: `{int(duos.kills)}`
                • Deaths: `{int(duos.deaths)}`
                • Goals: `{int(duos.goals)}`
                • Best winstreak: `{int(duos.bestws)}`
                • Winstreak: `{int(duos.ws)}`
                • KDR: `{round(duos.kdr, 2)}`
                • WLR: `{round(duos.wlr, 2)}`
                """
            )
            embed.add_field(
                name="Trios",
                value=f"""
                • Wins: `{int(trios.wins)}`
                • Losses: `{int(trios.losses)}`
                • Draws: `{int(trios.draws)}`
                • Kills: `{int(trios.kills)}`
                • Deaths: `{int(trios.deaths)}`
                • Goals: `{int(trios.goals)}`
                • Best winstreak: `{int(trios.bestws)}`
                • Winstreak: `{int(trios.ws)}`
                • KDR: `{round(trios.kdr, 2)}`
                • WLR: `{round(trios.wlr, 2)}`
                """
            )
            embed.add_field(
                name="Fours",
                value=f"""
                • Wins: `{int(fours.wins)}`
                • Losses: `{int(fours.losses)}`
                • Draws: `{int(fours.draws)}`
                • Kills: `{int(fours.kills)}`
                • Deaths: `{int(fours.deaths)}`
                • Goals: `{int(fours.goals)}`
                • Best winstreak: `{int(fours.bestws)}`
                • Winstreak: `{int(fours.ws)}`
                • KDR: `{round(fours.kdr, 2)}`
                • WLR: `{round(fours.wlr, 2)}`
                """
            )
            if cosmetics.character == "":
                cosmetics.character = "None"
            embed.add_field(
                name="Cosmetics",
                value=f"""
                • Title: `{cosmetics.title}`
                • Character: `{cosmetics.character}`
                """
            )
            embed.set_footer(
                text="Made by SomeHybrid#1179",
                icon_url="https://cdn.discordapp.com/avatars/670274727088095244/c6084274746f5b0e35df6bee22782562.webp?size=64"
            )
        except AttributeError:
            embed = discord.Embed(title="Error!", description="This user has not logged on to XinCraft!", color=0xFF0000)

        await ctx.respond(embed=embed, ephemeral=True)

    @commands.slash_command()
    async def invite(self, ctx):
        embed = discord.Embed(title="Invite",
                              description="Invite me [here!](https://discord.com/api/oauth2/authorize?client_id=699595050161537046&permissions=2048&scope=bot%20applications.commands)")
        await ctx.respond(embed=embed, ephemeral=True)

    @commands.slash_command()
    async def link(self, ctx, username: str):
        try:
            data = await self.client.get_user(username)
            data.stats
            self.db[str(ctx.author.id)] = username
            embed = discord.Embed(title="Linking", description=f"You have linked your discord account to {username}!", color=0xFFD700)
        except aiohttp.client_exceptions.ContentTypeError:
            embed = discord.Embed(title="Error!", description="This user does not exist!", color=0xFF0000)
        except AttributeError:
            embed = discord.Embed(title="Error!", description="This user has not logged on to XinCraft!", color=0xFF0000)

        await ctx.respond(embed=embed, ephemeral=True)

def setup(bot: discord.Bot):
    bot.add_cog(Main(bot))
