from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Danlin Chen'

doc = ''


class Constants(BaseConstants):
    name_in_url = 'earning_task3'
    players_per_group = None

    num_rounds = 30
    shown_nums1 = [567774545, 96567103, 20471794622381, 6472898373857, 285892403, 27858988, 62789362, 9609488,
                   67718193432, 72702141, 72741516879, 901789, 8084740920, 154310620417, 2227455294, 51526287390391,
                   8112452568888, 85254819, 363035970691, 6041622624879, 838625282, 17715110391939, 752934788,
                   5974380505, 42975891876364, 16521225488, 38805090497, 98600450725932, 7441749086699, 1311473]
    shown_nums2 = [326461976, 280716, 4745582556, 90667414, 785375273, 29374518, 719704, 552068472, 431760626, 26565295,
                   715234, 755503, 9882042, 791032178, 634667839, 9287586508, 536743, 431253, 70182422, 919701,
                   685615249, 4583602, 6682347, 5867590293, 4204709904, 6837289, 46526369, 4298337, 686174, 39552118]



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    nt3_points = models.IntegerField()
    entry_field = models.IntegerField()
    time_out_happened = models.BooleanField()

    def set_shown_num(self):
        if self.participant.vars['income2'] in [800, 600]:
            return Constants.shown_nums1
        else:
            return Constants.shown_nums2

    def set_nt3_points(self):
        self.nt3_points = self.participant.vars["ET1_correct"] * 10
        if 3 in self.participant.vars["ET1_incorrect"]:
            self.nt1_points -= 10
        self.participant.vars['nt3_points'] = self.nt3_points


