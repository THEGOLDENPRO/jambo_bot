import asyncio
import GoldyBot
from GoldyBot.utility.commands import *

class JamboUtils(GoldyBot.Extenstion):

    def __init__(self, package_module=None):
        super().__init__(self, package_module_name=package_module)

    def loader(self):
        @GoldyBot.command(slash_cmd_only=True)
        async def purge(self:JamboUtils, ctx):
            pass

        @purge.sub_command(required_roles=["bot_admin"], help_des="Admin command to delete every single message on this server!")
        async def everything(self:JamboUtils, ctx:GoldyBot.InteractionToCtx):
            view = await GoldyBot.utility.views.confirm.yes_or_no(ctx)
            member = GoldyBot.Member(ctx)

            are_you_sure_embed = GoldyBot.utility.goldy.embed.Embed(title="⚠ Warning", 
            description=f"**{mention(member)} Are you sure you would like to purge everything?**",
            colour=GoldyBot.utility.goldy.colours.YELLOW)

            await send(ctx, embed=are_you_sure_embed, view=view)
            await view.wait()

            if view.value == True:
                guild = GoldyBot.utility.guilds.guild.Guild(ctx.guild)

                for channel in await guild.get_channels(ctx):
                    if channel.channel.type == GoldyBot.nextcord.ChannelType.text:
                        await channel.purge(amount=None)
                    
                message = await send(ctx, "Done!")

        @purge.sub_command(required_roles=["bot_admin"], help_des="Admin command to delete a number of messages in this channel!")
        async def messages(self:JamboUtils, ctx:GoldyBot.InteractionToCtx, amount:str):
            channel = GoldyBot.objects.Channel(ctx)
            await channel.purge(amount=int(amount))
                
            msg = await send(ctx, "Done!")