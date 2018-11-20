from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Introduction)
        length = len(str(Constants.shown_nums[self.round_number-1]))
        yield (pages.taskPage_ET, {'entry_field': length})
