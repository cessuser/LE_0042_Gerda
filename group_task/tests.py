from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Introduction)
        if self.player.id_in_group % 4 == 0:
            yield (pages.test1, {'gt1_choice': 'Klee'})
            yield (pages.test2, {'gt2_choice': 'Boch'})
        if self.player.id_in_group % 4 == 1:
            yield (pages.test1, {'gt1_choice': 'Klee'})
            yield (pages.test2, {'gt2_choice': 'Bazille'})
        if self.player.id_in_group % 4 == 2:
            yield (pages.test1, {'gt1_choice': 'Kandinsky'})
            yield (pages.test2, {'gt2_choice': 'Boch'})
        if self.player.id_in_group % 4 == 3:
            yield (pages.test1, {'gt1_choice': 'Kandinsky'})
            yield (pages.test2, {'gt2_choice': 'Bazille'})
        yield (pages.Results)