from discord.ext import commands
from datamanager import DataManager

from spiders_discord import CnnSpider, MinutaSpider, LiveUaMapSpider
from utility import SITES, crawling_processing

SPIDERS = {'minuta': MinutaSpider, 'cnn': CnnSpider, 'liveua': LiveUaMapSpider}


class NewsCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(name="site", help='sites are: liveua, cnn, minuta')
    async def site(self, ctx: commands.Context, site: str) -> None:
        is_new_story, story = crawling_processing(site, SPIDERS[site])
        if site in SPIDERS:
            if is_new_story:
                await ctx.send(f'there is something new on: {site}')
                await ctx.send(story)
                await ctx.send('More on:')
                await ctx.send(f'{SITES[site]}')
                print(f'[INFO]: site is:{site}')
                return
            await ctx.send(f'there is nothing new on {site}')
        else:
            await ctx.send(f"there is no site: {site}, contact maintainer")

    @commands.command(name='lastnews', help='format: >lastnews <site> <number>, will print out number of last news')
    async def last_news(self, ctx: commands.Context, site: str, number: str, queuing: str='newest'):
        print(f'[INFO]: last news sending from {site}')
        site_data = DataManager(site)
        print(site_data)
        news_list = site_data.list_news()
        number = int(number)
        print(news_list)
        news_list = news_list[(len(news_list) - number):]
        print(news_list)
        if len(news_list) < number:
            number = len(news_list)

        if queuing == 'newest':
            for i in range(number):
                await ctx.send(news_list[(i + 1) * -1][-1])
                if i != number:
                    await ctx.send('older:')
        elif queuing == 'oldest':
            for i in range(number):
                await ctx.send(news_list[i][-1])
                if i != number:
                    await ctx.send('next:')
        else:
            raise commands.BadArgument(message='arguments are <site> <number> <queueing> which can be only "newest" or "oldest')
