# -*- coding: utf-8 -*-
# <standard imports>
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from otree_tools.models import fields

author = 'Danlin Chen'

doc = """
Project: Greda 
"""


class Constants(BaseConstants):
    name_in_url = 'paint_task1'
    players_per_group = None
    num_rounds = 1

    test_majority_payment = c(25)
    test_winner_payment = c(25)


class Subsession(BaseSubsession):
    def creating_session(self):

        if self.round_number == 1:
            pt1_a_order = []  # the order of authors
            pt1_p_order_klee = ['1', '2', '3', '4', '5']
            pt1_p_order_kand = ['1', '2', '3', '4', '5']
            random.shuffle(pt1_p_order_klee)
            random.shuffle(pt1_p_order_kand)
            pt1_pics_src = []
            for i in range(0, 5):
                if random.sample(['klee', 'kandinsky'], k= 2)[0] == 'klee': # the author of paintA is klee
                    pt1_a_order.append(['klee', 'kandinsky'])
                    paintA = pt1_p_order_klee[i] + '_a.jpg'
                    paintB = pt1_p_order_kand[i] + '_b.jpg'
                    pt1_pics_src.append([paintA, paintB])
                else:
                    pt1_a_order.append(['kandinsky', 'klee'])
                    paintB = pt1_p_order_klee[i] + '_a.jpg'
                    paintA = pt1_p_order_kand[i] + '_b.jpg'
                    pt1_pics_src.append([paintA, paintB])

            print("pta: ", pt1_a_order)
            print("ptp klee: ", pt1_p_order_klee)
            print("ptp kand: ", pt1_p_order_kand)

            self.session.vars['pt1_orders'] = {
                'pta_order': pt1_a_order,
                'ptp_order_klee': pt1_p_order_klee,
                'ptp_order_kand': pt1_p_order_kand,
                'pics_src': pt1_pics_src,
            }
            print("Subsession: pics_src ", pt1_pics_src)

class Group(BaseGroup):

    def set_painter_rank(self):
        kand_score = [[p.id, p.kandinsky_score, p.sum_pt1_duration] for p in self.get_players()]
        score_sort = sorted(kand_score, key=lambda x: (x[1], x[2]))
        player_rank_id = [var[0] for var in score_sort]

        print("Group: ", score_sort)

        for player in self.get_players():
            player.pt1_Rank = player_rank_id.index(player.id) + 1
            player.participant.vars['pt1_Rank'] = player.pt1_Rank

        ranks = [[p.id, p.pt1_Rank] for p in self.get_players()]
        print("pt1 player rank: ", ranks)


class Player(BasePlayer):
    # time
    time_loaded = models.FloatField()
    time_finished = models.FloatField()
    pt1_time1 = models.FloatField()
    pt1_time2 = models.FloatField()
    pt1_time3 = models.FloatField()
    pt1_time4 = models.FloatField()
    pt1_time5 = models.FloatField()

    sum_pt1_duration = models.FloatField()
    pt1_a_order = models.StringField()
    pt1_p_klee = models.StringField()
    pt1_p_kand = models.StringField()

    pt1_Rank = models.IntegerField()

    def set_orders(self):
        self.pt1_a_order = ''
        self.pt1_p_kand = ''
        self.pt1_p_klee = ''
        for i in range(0,5):
            painters = self.session.vars['pt1_orders']['pta_order'][i]
            self.pt1_a_order += '[' + painters[0] + ', ' + painters[1] + '] '
            self.pt1_p_klee += self.session.vars['pt1_orders']['ptp_order_klee'][i] + ' '
            self.pt1_p_kand += self.session.vars['pt1_orders']['ptp_order_kand'][i] + ' '

    def sum_duration(self):
        self.sum_pt1_duration = self.pt1_time1 + self.pt1_time2 + self.pt1_time3 + self.pt1_time4 + self.pt1_time5
        self.sum_pt1_duration = round(self.sum_pt1_duration, 2)

    # Pair fields:
    pt1_pair1 = models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelect()
    )
    pt1_pair2 = models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelect()
    )
    pt1_pair3 = models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelect()
    )
    pt1_pair4 = models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelect()
    )
    pt1_pair5 = models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelect()
    )

    kandinsky_score = models.IntegerField()
    painter_membership = models.CharField()

    def set_kandinsky_score(self):
        choices = [self.pt1_pair1, self.pt1_pair2, self.pt1_pair3, self.pt1_pair4, self.pt1_pair5]
        pta = self.session.vars['pt1_orders']['pta_order']
        self.kandinsky_score = 0
        for i in range(0,5):
            kand = 'A'
            if self.session.vars['pt1_orders']['pta_order'][i][0] == 'klee':
                kand = 'B'
            if choices[i] == kand:
                self.kandinsky_score += 1







