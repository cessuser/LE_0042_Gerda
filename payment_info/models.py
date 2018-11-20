from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
author = 'Danlin Chen'

doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class Constants(BaseConstants):
    name_in_url = 'payment_info'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    def set_bonus(self):
        bonus = 0
        for p in self.get_players():
            p.participant.vars['chosen'] = 0
            if p.participant.vars['bt_token'] != 0:
                bonus = p.participant.vars['bt_token']
                p.participant.vars['chosen'] = 1
                break
        for q in self.get_players():
            p.participant.vars['bonus'] = bonus


class Player(BasePlayer):
    def set_payoff(self, val):
        self.payoff = c(int(0.0025 * val)) + c(5)

