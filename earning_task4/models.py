from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Danlin Chen'

doc = ''


class Constants(BaseConstants):
    name_in_url = 'earning_task4'
    players_per_group = None

    num_rounds = 30
    shown_nums = [44009047, 6799961, 7632262, 8635336505, 5353545103, 3844782, 763731479137, 74975866, 834422570,
                  76386766615, 687790, 673258270, 4385914, 18289, 557452, 1615686, 437141, 278385090, 297144083,
                  2111331421, 70807264, 43790640, 83238524, 59113466805, 21204783971, 1060614, 36637126, 92434205002,
                  11140255, 73301475]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    nt4_points = models.IntegerField()
    entry_field = models.IntegerField()
    time_out_happened = models.BooleanField()

    def set_nt4_points(self):
        self.nt4_points = self.participant.vars["ET1_correct"] * 10
        if 3 in self.participant.vars["ET1_incorrect"]:
            self.nt4_points -= 10
        self.participant.vars['nt4_points'] = self.nt4_points


