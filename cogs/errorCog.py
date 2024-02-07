from discord.ext import commands
import discord

class ErrorCog(commands.Cog, name='Error'):
    '''Cog in charge of the error handling functions.'''

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        '''Event that takes place when there is an error in a command.
    
        Keyword arguments:
        error -- error message '''

        error = getattr(error, 'original', error)
        
        # Wrong command
        if isinstance(error, commands.CommandNotFound):
            message = f'"{ctx.message.content[1:]}" is not a valid command'
            return await ctx.send(message)

        # Bot lacks permissions.
        elif isinstance(error, commands.BotMissingPermissions):
            permissions = '\n'.join([f'> {permission}' for permission in error.missing_perms])
            message = f'I am missing the following permissions required to run the command `{ctx.command}`.\n{permissions}'
            try:
                return await ctx.send(message)
            except discord.Forbidden:
                try:
                    return await ctx.author.send(message)
                except discord.Forbidden:
                    return
        
        elif isinstance(error, commands.BadArgument):
            message = f'"{ctx.message.content}" has unknown arguments'
            return await ctx.send(message + error.message)