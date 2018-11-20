# -*- coding: utf-8 -*-
# <standard imports>
from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Pair1(Page):
    form_model = models.Player
    form_fields = ['pt2_pair1']

    def vars_for_template(self):
        self.player.set_orders()
        if not self.player.time_loaded:
            self.player.time_loaded = time.time()
        return {
            'pics_srcA': "paint_task2/" + self.session.vars['pt2_orders']['pics_src'][0][0],
            'pics_srcB': "paint_task2/" + self.session.vars['pt2_orders']['pics_src'][0][1]
        }

    def before_next_page(self):

        self.player.boch_score = 0
        self.player.time_finished = time.time()
        self.player.pt2_time1= round(self.player.time_finished - self.player.time_loaded,2)

class Pair2(Page):
    form_model = models.Player
    form_fields = ['pt2_pair2']

    def vars_for_template(self):
        self.player.time_loaded = time.time()
        return {
            'pics_srcA': "paint_task2/" + self.session.vars['pt2_orders']['pics_src'][1][0],
            'pics_srcB': "paint_task2/" + self.session.vars['pt2_orders']['pics_src'][1][1]
        }

    def before_next_page(self):
        self.player.time_finished = time.time()
        self.player.pt2_time2 = round(self.player.time_finished - self.player.time_loaded,2)


class Pair3(Page):
    form_model = models.Player
    form_fields = ['pt2_pair3']

    def vars_for_template(self):
        self.player.time_loaded = time.time()
        return {
            'pics_srcA': "paint_task2/" + self.session.vars['pt2_orders']['pics_src'][2][0],
            'pics_srcB': "paint_task2/" + self.session.vars['pt2_orders']['pics_src'][2][1]
        }

    def before_next_page(self):
        self.player.time_finished = time.time()
        self.player.pt2_time3 = round(self.player.time_finished - self.player.time_loaded,2)

class Pair4(Page):
    form_model = models.Player
    form_fields = ['pt2_pair4']

    def vars_for_template(self):
        self.player.time_loaded = time.time()
        return {
            'pics_srcA': "paint_task2/" + self.session.vars['pt2_orders']['pics_src'][3][0],
            'pics_srcB': "paint_task2/" + self.session.vars['pt2_orders']['pics_src'][3][1]
        }

    def before_next_page(self):
        self.player.time_finished = time.time()
        self.player.pt2_time4 = round(self.player.time_finished - self.player.time_loaded,2)

class Pair5(Page):
    form_model = models.Player
    form_fields = ['pt2_pair5']

    def vars_for_template(self):
        self.player.time_loaded = time.time()
        return {
            'pics_srcA': "paint_task2/" + self.session.vars['pt2_orders']['pics_src'][4][0],
            'pics_srcB': "paint_task2/" + self.session.vars['pt2_orders']['pics_src'][4][1]
        }

    def before_next_page(self):
        self.player.time_finished = time.time()
        self.player.pt2_time5 = round(self.player.time_finished - self.player.time_loaded,2)
        self.player.sum_duration()
        self.player.set_boch_score()

class WaitAll(WaitPage):
    def after_all_players_arrive(self):
        print("finish reading the ins")


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_painter_rank()
        self.group.set_comb_rank()
        self.group.set_pt_group_id()

class Result(Page):
    def vars_for_template(self):
        pt1 = 'Klee'
        pt2 = 'Bazille'
        groupID = self.player.pt_group_id
        if groupID == 2:
            pt1 = 'Klee'
            pt2 = 'Boch'
        if groupID == 3:
            pt1 = 'Kandinsky'
            pt2 = 'Boch'

        return {
            'group1': pt1,
            'group2': pt2,
            'group': pt1 + '-' + pt2,
            'n_group': self.player.n_group
        }

page_sequence = [
    Pair1,
    Pair2,
    Pair3,
    Pair4,
    Pair5,
    ResultsWaitPage,
    Result
]
