from __future__ import annotations

from core import Parrot
from .economy import economy

def setup(bot: Parrot):
    bot.add_cog(economy(bot))