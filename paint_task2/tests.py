from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.player.id_in_group % 3 == 0:
            yield (pages.Pair1, {'pt2_pair1': 'A'})
            yield (pages.Pair2, {'pt2_pair2': 'A'})
            yield (pages.Pair3, {'pt2_pair3': 'A'})
            yield (pages.Pair4, {'pt2_pair4': 'A'})
            yield (pages.Pair5, {'pt2_pair5': 'A'})
        if self.player.id_in_group % 3 == 1:
            yield (pages.Pair1, {'pt2_pair1': 'B'})
            yield (pages.Pair2, {'pt2_pair2': 'A'})
            yield (pages.Pair3, {'pt2_pair3': 'B'})
            yield (pages.Pair4, {'pt2_pair4': 'A'})
            yield (pages.Pair5, {'pt2_pair5': 'B'})
        if self.player.id_in_group % 3 == 2:
            yield (pages.Pair1, {'pt2_pair1': 'B'})
            yield (pages.Pair2, {'pt2_pair2': 'B'})
            yield (pages.Pair3, {'pt2_pair3': 'B'})
            yield (pages.Pair4, {'pt2_pair4': 'B'})
            yield (pages.Pair5, {'pt2_pair5': 'B'})
        yield (pages.Result)