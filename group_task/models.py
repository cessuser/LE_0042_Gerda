from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Danlin Chen'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'group_task'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_gt1_tokens(self):
        for p in self.get_players():
            p.gt1_tokens = 0
            if p.gt1_half_correct == 1 and p.gt2_half_correct == 1:
                p.gt1_tokens = 100
            p.participant.vars['gt1_tokens'] = p.gt1_tokens

    def set_gt2_tokens(self):
        for p in self.get_players():
            p.gt2_tokens = 0
            if p.gt_winner == 1:
                p.gt2_tokens = 100
            p.participant.vars['gt2_tokens'] = p.gt2_tokens

    def set_group_winner(self):
        group_score = [0,0,0]
        for p in self.get_players():
            if p.participant.vars['pt_group_id'] == 1:
                group_score[0] = p.gt1_n_correct + p.gt2_n_correct
            if p.participant.vars['pt_group_id'] == 2:
                group_score[1] = p.gt1_n_correct + p.gt2_n_correct
            if p.participant.vars['pt_group_id'] == 3:
                group_score[2] = p.gt1_n_correct + p.gt2_n_correct

        winner = group_score.index(max(group_score)) + 1
        for p in self.get_players():
            if group_score[0] == group_score[1] == group_score[2] == 1:
                p.gt_winner = 1
            if group_score[0] == group_score[1] == group_score[2] == 0:
                p.gt_winner = 0
            else:
                if p.participant.vars['pt_group_id'] == winner:
                    p.gt_winner = 1
                else:
                    p.gt_winner = 0


    def set_group_n_correct(self):
        for p in self.get_players():
            other = p.get_others_in_group()
            p.gt1_n_correct = 0
            p.gt2_n_correct = 0
            if p.gt1_correct:
                p.gt1_n_correct += 1
            if p.gt2_correct:
                p.gt2_n_correct += 1
            for o in other:
                if o.participant.vars['pt_group_id'] == p.participant.vars['pt_group_id']:
                    if o.gt1_correct:
                        p.gt1_n_correct += 1
                    if o.gt2_correct:
                        p.gt2_n_correct += 1

        group_n_correct = [[p.id, p.participant.vars['combRank'], p.participant.vars['pt_group_id'],p.gt1_n_correct, p.gt2_n_correct] for p in self.get_players()]
        print("groupids: ", group_n_correct)


    def set_gt_half_correct(self):
        for p in self.get_players():
            group_size = p.participant.vars['n_group']
            p.gt1_half_correct = 0
            p.gt2_half_correct = 0
            if group_size == 1:
                if p.gt1_correct:
                    p.gt1_half_correct = 1
                if p.gt2_correct:
                    p.gt2_half_correct = 1
            else:
                if group_size % 2 == 0:
                    if p.gt1_n_correct >= group_size/2:
                        p.gt1_half_correct = 1
                    if p.gt2_n_correct >= group_size/2:
                        p.gt2_half_correct = 1
        group_half = [[p.id, p.gt1_half_correct, p.gt2_half_correct] for p in self.get_players()]
        print("group half: ", group_half)


class Player(BasePlayer):
    gt1_choice = models.StringField(widget= widgets.RadioSelect)
    gt2_choice = models.StringField(widget= widgets.RadioSelect)

    gt1_correct = models.BooleanField()
    gt2_correct = models.BooleanField()

    gt1_n_correct = models.IntegerField()
    gt2_n_correct = models.IntegerField()

    gt1_half_correct = models.IntegerField(min=0,max=1)
    gt2_half_correct = models.IntegerField(min=0,max=1)

    gt_winner = models.IntegerField(min=0, max=1)
    gt1_tokens = models.IntegerField()
    gt2_tokens = models.IntegerField()

    def set_gt_correct(self):
        self.gt1_correct = False
        if self.gt1_choice == 'Klee':
            self.gt1_correct = True
        self.gt2_correct = False
        if self.gt2_choice == 'Boch':
            self.gt2_correct = True

