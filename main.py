from dotenv import load_dotenv
from discord import commands
import discord
import xincraft
import os


class Main(discord.Cog):
    def __init__(self, bot):
        load_dotenv()
        key = os.getenv("XINCRAFT_KEY")
        self.client = xincraft.AsyncClient(key)
        self.bot = bot

    @commands.slash_command(guild_ids=[924110379355897876])
    async def stats(self, ctx, user: str):
        data = await self.client.get_user(user)
        embed = discord.Embed(title=f"{user}'s stats", color=0xFFD700)
        overall = data.stats.overall
        solos = data.stats.solos
        duos = data.stats.doubles
        trios = data.stats.trios
        fours = data.stats.fours
        cosmetics = data.cosmetics
        embed.add_field(
            name="Overall",
            value=f"""
            • Wins: `{overall.wins}`
            • Losses: `{overall.losses}`
            • Kills: `{overall.kills}`
            • Deaths: `{overall.deaths}`
            • Draws: `{overall.draws}`
            • Winstreak: `{overall.ws}`
            • Best winstreak: `{overall.bestws}`
            • KDR: `{round(overall.kills / overall.deaths, 2)}`
            • Tokens: `{data.tokens}`
            • ELO: `{data.elo}`
            """
        )
        embed.add_field(
            name="Solos",
            value=f"""
            • Wins: `{solos.wins}`
            • Losses: `{solos.losses}`
            • Kills: `{solos.kills}`
            • Deaths: `{solos.deaths}`
            • Draws: `{solos.draws}`
            • Winstreak: `{solos.ws}`
            • Best winstreak: `{solos.bestws}`
            • KDR: `{round(solos.kills / solos.deaths, 2)}`
            """
        )
        embed.add_field(
            name="Duos",
            value=f"""
            • Wins: `{duos.wins}`
            • Losses: `{duos.losses}`
            • Kills: `{duos.kills}`
            • Deaths: `{duos.deaths}`
            • Draws: `{duos.draws}`
            • Winstreak: `{duos.ws}`
            • Best winstreak: `{duos.bestws}`
            • KDR: `{round(duos.kills / duos.deaths, 2)}`
            """
        )
        embed.add_field(
            name="Trios",
            value=f"""
            • Wins: `{trios.wins}`
            • Losses: `{trios.losses}`
            • Kills: `{trios.kills}`
            • Deaths: `{trios.deaths}`
            • Draws: `{trios.draws}`
            • Winstreak: `{trios.ws}`
            • Best winstreak: `{trios.bestws}`
            • KDR: `{round(trios.kills / trios.deaths, 2)}`
            """
        )
        embed.add_field(
            name="Fours",
            value=f"""
            • Wins: `{fours.wins}`
            • Losses: `{fours.losses}`
            • Kills: `{fours.kills}`
            • Deaths: `{fours.deaths}`
            • Draws: `{fours.draws}`
            • Winstreak: `{fours.ws}`
            • Best winstreak: `{fours.bestws}`
            • KDR: `{round(fours.kills / fours.deaths, 2)}`
            """
        )
        embed.add_field(
            name="Socials",
            value=f"""
            • YouTube: `{data.youtube}`
            • Discord: `{data.discord}`
            • Twitch: `{data.twitch}`
            """
        )
        await ctx.respond(embed=embed)


def setup(bot: discord.Bot):
    bot.add_cog(Main(bot))