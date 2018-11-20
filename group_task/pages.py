from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models
import random


class Introduction(Page):
    pass


class test1(Page):
    form_fields = ['gt1_choice']
    form_model = models.Player

    def gt1_choice_choices(self):
        choices = ['Klee', 'Kandinsky']
        random.shuffle(choices)
        return choices



class test2(Page):
    form_fields = ['gt2_choice']
    form_model = models.Player

    def gt2_choice_choices(self):
        choices = ['Boch', 'Bazille']
        random.shuffle(choices)
        return choices

    def before_next_page(self):
        self.player.set_gt_correct()


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_group_n_correct()
        self.group.set_gt_half_correct()
        self.group.set_group_winner()
        self.group.set_gt1_tokens()
        self.group.set_gt2_tokens()



class Results(Page):
    pass


page_sequence = [
    Introduction,
    test1,
    test2,
    ResultsWaitPage,
    Results
]
