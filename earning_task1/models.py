from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Danlin Chen'

doc = ''


class Constants(BaseConstants):
    name_in_url = 'earning_task1'
    players_per_group = None

    num_rounds = 30
    shown_nums = [25315315502, 852234173244, 365861298, 34858605, 861381600721, 197654563, 714827076, 23965817244,
                  402264116114, 1736325, 566304, 892502000148, 990047743950, 41335033591, 24888933414, 75594634,
                  139482650, 39277223468, 23720402, 19296538, 643607697, 34914017, 21359770, 214553382965, 387334,
                  39726, 7580001556, 114833508, 775852798, 8848507745]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    nt1_points = models.IntegerField()
    entry_field = models.IntegerField()
    time_out_happened = models.BooleanField()

    def set_nt1_points(self):
        self.nt1_points = self.participant.vars["ET1_correct"] * 10
        if 3 in self.participant.vars["ET1_incorrect"]:
            self.nt1_points -= 10
        self.participant.vars['nt1_points'] = self.nt1_points


