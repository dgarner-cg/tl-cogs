from .jailed import Jail

def setup(bot):
    bot.add_cog(Jail(bot))