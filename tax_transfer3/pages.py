from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models
import random


class MyPage(Page):
    def vars_for_template(self):
        return{
            "group_by_id" : self.player.participant.vars['pt_group_id']
        }


class WaitOther(WaitPage):
    body_text = 'We are calculating your tokens. Please wait.'

    def is_displayed(self):
        return self.round_number == 1

    def after_all_players_arrive(self):
        self.group.set_rank_income3()


class Results_ET(Page):
    def is_displayed(self):
        return self.round_number == 1


class Period3(Page):
    form_model = models.Player
    form_fields = ['dv']

    def dv_choices(self):
        choices = [[1, 'Scheme 1: 20% taxes and 100 tokens for each participant'],
                   [2, 'Scheme 2: 40% taxes and 200 tokens for each participant']]

        random.shuffle(choices)
        return choices

    def vars_for_template(self):
        if self.round_number == 1:
            self.player.participant.vars['competition_period3'] = []
            self.player.participant.vars['dv_period3'] = []
            self.player.participant.vars['rg_tokens_period3'] = []

        self.player.set_info(self.round_number)
        income = self.player.income3
        group_members_info = self.player.find_group_members_info(self.round_number)
        self.player.set_competition()
        if self.player.income3 == 400:
            competition_msg = ['You have performed well in the competition. Your earnings of 400 tokens have therefore not been reduced. ',
                               'You have not performed well in the competition. Your earnings have therefore been reduced to 360 tokens. ']
            if self.player.competition == 1:
                income = 360


        else:
            competition_msg = [group_members_info[1]+'has performed well in the competition. Their earnings of 400 have therefore not been reduced. ',
                               group_members_info[1]+'has not performed well in the competition. Their earnings have therefore been reduced to 360 tokens. ']

        lst = [200,400,600,800]
        if self.player.competition == 1:
            group_members_info[0][1][1] = 360
        lst.remove(self.player.income3)
        random.shuffle(lst)
        new_group_info = [0,0,0]
        new_group_info[0] = group_members_info[0][int((lst[0]-200)/200)]
        new_group_info[1] = group_members_info[0][int((lst[1]-200)/200)]
        new_group_info[2] = group_members_info[0][int((lst[2]-200)/200)]

        random.shuffle(group_members_info[0])

        print('*****************new*********** ', new_group_info)
        return{
            'income': income,
            'group': self.player.pt_group_id,
            'member1_group': new_group_info[0][0],
            'member1_tokens': new_group_info[0][1],
            'member2_group': new_group_info[1][0],
            'member2_tokens': new_group_info[1][1],
            'member3_group': new_group_info[2][0],
            'member3_tokens': new_group_info[2][1],
            '400token_group': group_members_info[1],
            'competition_msg': competition_msg[self.player.competition],
            'round_num': self.round_number
        }
    def before_next_page(self):
        self.player.participant.vars['dv_period3'].append(self.player.dv)


class ResultsWaitPage(WaitPage):
    body_text = "The computer will randomly select two rounds from this period to compute your payoffs. " \
                "You will find out your payoff at the end of the experiment."
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def after_all_players_arrive(self):
        self.group.set_rg_tokens()
        self.group.set_rgab_tokens()


class MyPage(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

page_sequence = [
    WaitOther,
    Results_ET,
    Period3,
    ResultsWaitPage,
    MyPage
]
