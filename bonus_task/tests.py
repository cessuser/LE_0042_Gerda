from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.player.id_in_group % 2 == 0:
            yield (pages.BonusTask, {'bonus_choice': 600})
        if self.player.id_in_group % 2 == 1:
            yield (pages.BonusTask, {'bonus_choice': 200})
        yield (pages.SurveyIntro)