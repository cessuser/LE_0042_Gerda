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
Project: Gerda 
"""


class Constants(BaseConstants):
    name_in_url = 'paint_task2'
    players_per_group = None
    num_rounds = 1

    test_majority_payment = c(25)
    test_winner_payment = c(25)


class Subsession(BaseSubsession):
    def creating_session(self):

        if self.round_number == 1:
            pt2_a_order = []  # the order of authors
            pt2_p_order_bazille = ['6', '7', '8', '9', '10']
            pt2_p_order_boch = ['6', '7', '8', '9', '10']
            random.shuffle(pt2_p_order_bazille)
            random.shuffle(pt2_p_order_boch)
            pt2_pics_src = []
            for i in range(0, 5):
                if random.sample(['bazille', 'boch'], k= 2)[0] == 'bazille': # the author of paintA is bazille
                    pt2_a_order.append(['bazille', 'boch'])
                    paintA = pt2_p_order_bazille[i] + '_a.jpg'
                    paintB = pt2_p_order_boch[i] + '_b.jpg'
                    pt2_pics_src.append([paintA, paintB])
                else:
                    pt2_a_order.append(['boch', 'bazille'])
                    paintB = pt2_p_order_bazille[i] + '_a.jpg'
                    paintA = pt2_p_order_boch[i] + '_b.jpg'
                    pt2_pics_src.append([paintA, paintB])

            # print("pta: ", pt2_a_order)
            # print("ptp bazille: ", pt2_p_order_bazille)
            # print("ptp boch: ", pt2_p_order_boch)
            #
            self.session.vars['pt2_orders'] = {
                'pta_order': pt2_a_order,
                'ptp_order_bazille': pt2_p_order_bazille,
                'ptp_order_boch': pt2_p_order_boch,
                'pics_src': pt2_pics_src,
            }
            # print("Subsession: pics_src ", pt2_pics_src)

class Group(BaseGroup):

    def set_painter_rank(self):
        boch_score = [[p.id, p.boch_score, p.sum_pt2_duration] for p in self.get_players()]
        score_sort = sorted(boch_score, key=lambda x: (x[1], x[2]))
        player_rank_id = [var[0] for var in score_sort]

        for player in self.get_players():
            player.pt2_Rank = player_rank_id.index(player.id) + 1
            player.participant.vars['pt2_Rank'] = player.pt2_Rank

    def set_comb_rank(self):
        for player in self.get_players():
            player.combRank = player.participant.vars['pt1_Rank'] + player.pt2_Rank
            player.participant.vars['combRank'] = player.combRank


    def set_pt_group_id(self):
        comb_lst = [[p.id, p.combRank] for p in self.get_players()]
        sort_comb = sorted(comb_lst, key=lambda x: x[1])
        player_ids = [var[0] for var in sort_comb]

        klee_bazille = []
        kand_boch = []
        klee_boch = []
        divisible = len(self.get_players()) % 3
        size = len(self.get_players()) // 3
        if divisible == 0: # divisible by 3, [2,2,2]
            klee_bazille = player_ids[0:size]
            klee_boch = player_ids[size:size * 2]
            kand_boch = player_ids[size*2:size * 3]

        if divisible == 1: # num_players mod 3 = 1, separate to [kl-ba:3,kl-bo:2,ka-bo:2]
            klee_bazille = player_ids[0:size+1]
            klee_boch = player_ids[size+1:size*2+1]
            kand_boch = player_ids[size*2+1:size*3+1]

        if divisible == 2: # num_players mod 3 = 2, separate to [kl-ba:3,kl-bo:2,ka-bo:3]
            klee_bazille = player_ids[0:size+1]
            klee_boch = player_ids[size+1: size*2+1]
            kand_boch = player_ids[size*2+1:size*3+2]


        for player in self.get_players():
            if player.id in klee_bazille:
                player.pt_group_id = 1
                player.n_group = len(klee_bazille)
            if player.id in klee_boch:
                player.pt_group_id = 2
                player.n_group = len(klee_boch)
            if player.id in kand_boch:
                player.pt_group_id = 3
                player.n_group = len(kand_boch)
            player.participant.vars['pt_group_id'] = player.pt_group_id
            player.participant.vars['n_group'] = player.n_group


        ranks1 = [[p.id, p.participant.vars['pt1_Rank']] for p in self.get_players()]
        ranks2 = [[p.id, p.participant.vars['pt2_Rank']] for p in self.get_players()]
        ids = [[p.id, p.participant.vars['pt_group_id']] for p in self.get_players()]
        ngroup= [[p.id, p.participant.vars['n_group']] for p in self.get_players()]
        combranks = [[p.id, p.combRank] for p in self.get_players()]
        print("divisible: ", len(self.get_players()) % 3)
        print("rank1: ", ranks1)
        print("rank2: ", ranks2)
        print("combRanks: ", combranks)
        print("klee bazille: ", klee_bazille)
        print("klee_boch: ", klee_boch)
        print("kand_boch: ", kand_boch)
        print("ids: ", ids)
        print("ngroup: ", ngroup)

class Player(BasePlayer):
    # time
    time_loaded = models.FloatField()
    time_finished = models.FloatField()
    pt2_time1 = models.FloatField()
    pt2_time2 = models.FloatField()
    pt2_time3 = models.FloatField()
    pt2_time4 = models.FloatField()
    pt2_time5 = models.FloatField()

    sum_pt2_duration = models.FloatField()
    pt2_a_order = models.StringField()
    pt2_p_bazille = models.StringField()
    pt2_p_boch = models.StringField()

    pt2_Rank = models.IntegerField()
    combRank = models.IntegerField()
    pt_group_id = models.IntegerField()
    n_group = models.IntegerField()


    def set_orders(self):
        self.pt2_a_order = ''
        self.pt2_p_boch = ''
        self.pt2_p_bazille = ''
        for i in range(0,5):
            painters = self.session.vars['pt2_orders']['pta_order'][i]
            self.pt2_a_order += '[' + painters[0] + ', ' + painters[1] + '] '
            self.pt2_p_bazille += self.session.vars['pt2_orders']['ptp_order_bazille'][i] + ' '
            self.pt2_p_boch += self.session.vars['pt2_orders']['ptp_order_boch'][i] + ' '

    def sum_duration(self):
        self.sum_pt2_duration = self.pt2_time1 + self.pt2_time2 + self.pt2_time3 + self.pt2_time4 + self.pt2_time5
        self.sum_pt2_duration = round(self.sum_pt2_duration, 2)

    # Pair fields:
    pt2_pair1 = models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelect()
    )
    pt2_pair2 = models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelect()
    )
    pt2_pair3 = models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelect()
    )
    pt2_pair4 = models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelect()
    )
    pt2_pair5 = models.StringField(
        choices=['A', 'B'],
        widget=widgets.RadioSelect()
    )

    boch_score = models.IntegerField()
    painter_membership = models.CharField()

    def set_boch_score(self):
        choices = [self.pt2_pair1, self.pt2_pair2, self.pt2_pair3, self.pt2_pair4, self.pt2_pair5]
        pta = self.session.vars['pt2_orders']['pta_order']
        self.boch_score = 0
        for i in range(0,5):
            boch = 'A'
            if self.session.vars['pt2_orders']['pta_order'][i][0] == 'bazille':
                boch = 'B'
            if choices[i] == boch:
                self.boch_score += 1






