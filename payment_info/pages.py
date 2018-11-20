from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class PaymentInfo(Page):

    def vars_for_template(self):
        self.group.set_bonus()
        p1_payoff = self.player.participant.vars['gt1_tokens'] + self.player.participant.vars['gt2_tokens']
        rd1ab = self.player.participant.vars['rd2_period1']
        rd2ab = self.player.participant.vars['rd2_period2']
        rd3ab = self.player.participant.vars['rd2_period3']
        period1 = self.player.participant.vars['rg_tokens_period1'][rd1ab[0]-1] + \
                  self.player.participant.vars['rg_tokens_period1'][rd1ab[1]-1]
        period2 = self.player.participant.vars['rg_tokens_period2'][rd2ab[0]-1] + \
                  self.player.participant.vars['rg_tokens_period2'][rd2ab[1]-1]
        period3 = self.player.participant.vars['rg_tokens_period3'][rd3ab[0]-1] + \
                  self.player.participant.vars['rg_tokens_period3'][rd3ab[1]-1]

        p2_payoff = period1 + period2 + period3
        bonus = 0
        chosen_msg = 'selected'
        for p in self.player.get_others_in_subsession():
            if p.participant.vars['bt_token'] != 0:
                bonus = p.participant.vars['bt_token']

        p3_payoff1 =self.player.participant.vars['nt4_points']
        p3_payoff = p3_payoff1 + self.participant.vars['bt_token'] + 200
        total_payoff = p1_payoff + p2_payoff + p3_payoff
        self.player.set_payoff(total_payoff)
        if self.player.participant.vars['bt_token'] == 0:
          chosen_msg = 'not selected'

        self.player.payoff = total_payoff*0.0025 + 5

        return {
            'p1_payoff': p1_payoff,
            'p2_payoff': p2_payoff,
            'p3_payoff': p3_payoff,
            'total_payoff': total_payoff,
            'rd1a': rd1ab[0],
            'rd1b': rd1ab[1],
            'rd2a': rd2ab[0],
            'rd2b': rd2ab[1],
            'rd3a': rd3ab[0],
            'rd3b': rd3ab[1],
            'p3_bonus': bonus,
            'chosen': chosen_msg,
            'p3_payoff1': p3_payoff1,
            'real_pay': total_payoff * 0.0025 + 5

        }


class ResultWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_bonus()
page_sequence = [
    ResultWaitPage,
    PaymentInfo]
