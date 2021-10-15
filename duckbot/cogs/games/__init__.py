from .aoe import AgeOfEmpires
from .coin_flip import CoinFlip
from .dice import Dice
from .discord_activity import DiscordActivity


def setup(bot):
    bot.add_cog(Dice(bot))
    bot.add_cog(AgeOfEmpires(bot))
    bot.add_cog(CoinFlip(bot))
    bot.add_cog(DiscordActivity(bot))
