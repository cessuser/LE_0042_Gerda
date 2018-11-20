from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models


class BonusTask(Page):
    form_model = models.Player
    form_fields = ['bonus_choice']

    def vars_for_template(self):
        self.player.set_match_info()
        return {
            'match_group': ['Klee-Bazille', 'Klee-Boch', 'Klee-Bazille'][self.player.match_group_id-1]
        }

    def before_next_page(self):
        self.player.set_bonus_choice()


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_bonus_subject()
        self.group.set_bt_token()



class SurveyIntro(Page):
    pass


page_sequence = [
    BonusTask,
    ResultsWaitPage,
    SurveyIntro
]
