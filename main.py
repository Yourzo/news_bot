from discord.ext import commands

from cogs.autoNewsCog import AutoNewsCog
from cogs.news_cog import NewsCog
from cogs.errorCog import ErrorCog


TOKEN = 'OTgxODYxMjE3NjA4MDI0MDk0.GLPaMN.m33sog4JVffxhn-wHD1VCXuytutxceHrL-AASw'
DESCR = 'FOR AUTOMATED FROM SITES RUN: >autonews, prefix: ">", this bitch is painfully coded, so bad omg'


class NewsBot(commands.Bot):
    def __init__(self, command_prefix: str) -> None:
        commands.Bot.__init__(self, command_prefix=command_prefix,
                              description=DESCR)
        self.message1 = "[INFO]: NewsBot now online"

        self.add_cog(NewsCog(self))
        self.add_cog(AutoNewsCog(self))
        self.add_cog(ErrorCog(self))

    async def on_ready(self) -> None:
        print(self.message1)


def main() -> None:
    client = NewsBot(command_prefix='>')
    client.run(TOKEN)


if __name__ == "__main__":
    main()
