from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Danlin Chen'

doc = ''


class Constants(BaseConstants):
    name_in_url = 'earning_task2'
    players_per_group = None

    num_rounds = 30
    shown_nums1 = [12439852861343, 2599939616, 2253592569121, 108474539569, 6143459, 69190348419597, 893820055240,
                   608111745932, 695333341, 690850376, 801760039508, 1608828, 3097203092, 7759748123, 43843452871,
                   819192777456, 463386, 479192018459, 254489402847, 82371974395799, 1021900796, 466636753, 319172448,
                   74850949, 258685026195, 771056988439, 45168063, 7250400334863, 688942, 5817474496]
    shown_nums2 = [2678026339, 705153, 2581895, 4642522, 5291418287, 203964, 6456339775, 38214391, 144859536, 161882759,
                   166072002, 2423962, 60140350, 150271827, 920765064, 34442755, 418353376, 3314243329, 730867239,
                   5676456, 51161429, 915286, 570982, 84869, 3498772183, 7422815, 407364, 8442727673, 34420013, 113584]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    nt2_points = models.IntegerField()
    entry_field = models.IntegerField()
    time_out_happened = models.BooleanField()

    def set_shown_num(self):
        if self.participant.vars['income1'] in [800,600]:
            return Constants.shown_nums1
        else:
            return Constants.shown_nums2

    def set_nt2_points(self):
        self.nt2_points = self.participant.vars["ET1_correct"] * 10
        if 3 in self.participant.vars["ET1_incorrect"]:
            self.nt1_points -= 10
        self.participant.vars['nt2_points'] = self.nt2_points


