from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Danlin Chen'

doc = """
bonus task of GH
"""


class Constants(BaseConstants):
    name_in_url = 'bonus_task'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        ids = [p.participant.id_in_session for p in self.get_players()]
        subject = random.sample(ids, k=1)[0]
        for p in self.get_players():
            p.bonus_subject = subject

    pass


class Group(BaseGroup):
    def set_bonus_subject(self):
        for p in self.get_players():
            p.bonus_id = False
            p.bonus_income = False
            if p.participant.vars['pt_group_id'] == p.match_group_id:
                p.bonus_id = True
            if p.participant.vars['income2'] == p.match_income:
                p.bonus_income = True


    def set_bt_token(self):
        print("all players??", self.get_players())
        for p in self.get_players():
            if p.participant.id_in_session == p.bonus_subject:
                p.bt_token = p.participant.vars['bonus']
            else:
                p.bt_token = 0
            p.participant.vars['bt_token'] = p.bt_token



class Player(BasePlayer):
    bonus_choice = models.IntegerField(choices=[600, 200], widget=widgets.RadioSelect)
    match_group_id = models.IntegerField()
    match_income = models.IntegerField()
    bonus_subject = models.IntegerField()
    bt_token = models.IntegerField()
    bonus_id = models.BooleanField()
    bonus_income = models.BooleanField()

    def set_match_info(self):
        for other in self.get_others_in_group():
            assert(len(self.get_others_in_group()) == 1)
            self.match_group_id = other.participant.vars['pt_group_id']
            self.match_income = other.participant.vars['income2']

    def set_bonus_choice(self):
        for other in self.get_others_in_group():
            other.participant.vars['bonus'] = self.bonus_choice