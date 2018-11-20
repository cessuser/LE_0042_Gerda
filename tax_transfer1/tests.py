from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Results_ET)
        if self.player.id_in_group % 2 == 0:
            yield (pages.Period1, {'dv': 1})
        if self.player.id_in_group % 2 == 1:
            yield (pages.Period1, {'dv': 2})
        if self.round_number == Constants.num_rounds:
            yield (pages.MyPage)