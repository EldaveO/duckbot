from discord.ext import commands

class Cloud(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def correct_cloud(self, message):
        """Corrections for cloud"""

        if message.author == self.bot.user:
            return

        if "cloud" in message.content.lower():
            r = int(random.randint(0, 1))
            if r == 0:
                correction = "magic sky box*"
            elif r == 1:
                correction = "someone else's computer*"
            await message.channel.send(correction)
