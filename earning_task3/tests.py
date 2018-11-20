from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Introduction)
        if self.player.participant.vars['income2'] in [800, 600]:
            length = len(str(Constants.shown_nums1[self.round_number - 1]))
            yield (pages.taskPage_ET, {'entry_field': length})
        if self.player.participant.vars['income2'] in [400, 200]:
            length = len(str(Constants.shown_nums2[self.round_number - 1]))
            yield (pages.taskPage_ET, {'entry_field': length})
