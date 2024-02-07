from discord.ext import commands, tasks

import utility
from cogs.news_cog import SPIDERS


class AutoNewsCog(commands.Cog):
    """this is cog that on registration in channel will call every
        minute all spiders to check our targets and if there are new changes
        it will send discord message"""
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot
        self.auto_news_chanel = 0

    @tasks.loop(minutes=1, reconnect=True)
    async def check_for_new_stories(self) -> None:
        for site in utility.SITES:
            is_new, data = utility.crawling_processing(site, SPIDERS[site])

            if is_new:
                channel = self.bot.get_channel(id=self.auto_news_chanel)
                print(f'[INFO]: new message at: {site}')
                await channel.send(f'News on: {site}')
                await channel.send(data + '...')
                await channel.send('More on:')
                await channel.send(utility.SITES[site])
            else:
                print(f'[INFO]: called but nothing on {site}')

    @check_for_new_stories.before_loop
    async def before(self) -> None:
        await self.bot.wait_until_ready()
        print('[INFO]: auto news cog ready')

    @commands.command(name='autonews', help='will register given channel for autonews')
    async def auto_news(self, ctx: commands.Context) -> None:
        self.auto_news_chanel = ctx.channel.id
        await ctx.send(f'{ctx.channel.name} has been registered for automated news')
        await self.check_for_new_stories.start()

    @commands.command(name='disablenews', help='will unregister this channel from receiving latest news')
    async def disable_news(self, ctx) -> None:
        self.auto_news = 0
        await ctx.send(f'{ctx.channel.name} have been unregistered from automated news on war')
        await self.check_for_new_stories.stop()
