from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import numpy as np

author = 'Danlin Chen'

doc = """
tax and transfer period 2
"""


class Constants(BaseConstants):
    name_in_url = 'tax_transfer2'
    players_per_group = None
    num_rounds = 8


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def set_income2_by_rank(self, quartiles_lst, rank):
        if 0 <= rank < quartiles_lst[0]:
            return 800
        if quartiles_lst[0] <= rank < quartiles_lst[1]:
            return 600
        if quartiles_lst[1] <= rank < quartiles_lst[2]:
            return 400
        else:
            return 200

    def set_rank_income2(self):
        group1 = [[p.id,p.participant.vars['nt2_points']] for p in self.get_players() if p.participant.vars['pt_group_id'] == 1]
        group2 = [[p.id, p.participant.vars['nt2_points']] for p in self.get_players() if p.participant.vars['pt_group_id'] == 2]
        group3 = [[p.id, p.participant.vars['nt2_points']] for p in self.get_players() if p.participant.vars['pt_group_id'] == 3]

        group1 = sorted(group1, key=lambda x: x[1], reverse=True)
        group2 = sorted(group2, key=lambda x: x[1], reverse=True)
        group3 = sorted(group3, key=lambda x: x[1], reverse=True)

        group1 = [sort_p[0] for sort_p in group1]
        group2 = [sort_p[0] for sort_p in group2]
        group3 = [sort_p[0] for sort_p in group3]

        quartiles_group1 = [(len(group1) + 1) // 4, (len(group1)+1) // 2, (len(group1)+1)*3 // 4]
        quartiles_group2 = [(len(group2) + 1) // 4, (len(group2) + 1) // 2, (len(group2) + 1) * 3 // 4]
        quartiles_group3 = [(len(group3) + 1) // 4, (len(group3) + 1) // 2, (len(group3) + 1) * 3 // 4]

        for p in self.get_players():
            if p.id in group1:
                p.nt2_rank = group1.index(p.id) + 1
                p.participant.vars['nt2_rank'] = p.nt2_rank
                if p.participant.vars['n_group'] <= 3:
                    p.income2 = 800 - 200 * (p.nt2_rank-1)
                else:
                    p.income2 = self.set_income2_by_rank(quartiles_group1, p.nt2_rank-1)
                p.participant.vars['income2'] = p.income2
                p.participant.vars['income2'] = p.income2
            if p.id in group2:
                p.nt2_rank = group2.index(p.id) + 1
                p.participant.vars['nt2_rank'] = p.nt2_rank
                if p.participant.vars['n_group'] <= 3:
                    p.income2 = 800 - 200 * (p.nt2_rank-1)
                else:
                    p.income2 = self.set_income2_by_rank(quartiles_group2, p.nt2_rank-1)
                p.participant.vars['income2'] = p.income2
                p.participant.vars['income2'] = p.income2
            if p.id in group3:
                p.nt2_rank = group3.index(p.id) + 1
                p.participant.vars['nt2_rank'] = p.nt2_rank
                if p.participant.vars['n_group'] <= 3:
                    p.income2 = 800 - 200 * (p.nt2_rank-1)
                else:
                    p.income2 = self.set_income2_by_rank(quartiles_group3, p.nt2_rank-1)
                p.participant.vars['income2'] = p.income2
                p.participant.vars['income2'] = p.income2
        self.set_round_group()
# set the decsion group for all 8 rounds
# find the median of nt2_dif
# set rd1, ..., rd7, rd8
# set rd1a and rd1b among rd1, .., rd7, rd8

    def set_round_group(self):
        nt2_dif_lst = []
        rd_period2 = []

        for r in range(0, Constants.num_rounds):
            rd_period2.append([random.sample([800, 400, 600, 200], k=1)[0]
                               for num_g in range(0, len(self.get_players()) // 4)])
        rd1a_period2 = random.randint(1, Constants.num_rounds)
        rd1b_period2 = random.randint(1, Constants.num_rounds)

        for round in range(0, Constants.num_rounds):
            for p in self.get_players():
                if round == 0:
                    p.participant.vars['decgroup_period2'] = []
                    p.participant.vars['identity_period2'] = []
                    p.participant.vars['rd_period2'] = rd_period2
                    p.participant.vars['rd2_period2'] = [rd1a_period2, rd1b_period2]

            groups800_600 = [[], [], []]
            groups400 = []
            groups400.append(
                [p for p in self.get_players() if p.participant.vars['pt_group_id'] == 1 and p.income2 == 400])
            groups400.append(
                [p for p in self.get_players() if p.participant.vars['pt_group_id'] == 2 and p.income2 == 400])
            groups400.append(
                [p for p in self.get_players() if p.participant.vars['pt_group_id'] == 3 and p.income2 == 400])

            groups200 = []
            groups200.append(
                [p for p in self.get_players() if p.participant.vars['pt_group_id'] == 1 and p.income2 == 200])
            groups200.append(
                [p for p in self.get_players() if p.participant.vars['pt_group_id'] == 2 and p.income2 == 200])
            groups200.append(
                [p for p in self.get_players() if p.participant.vars['pt_group_id'] == 3 and p.income2 == 200])

            rest_400 = []
            rest_200 = []
            for pt_group in range(0, 3):
                cur_group400 = groups400[pt_group]
                cur_group200 = groups200[pt_group]
                lst_400_same = [random.randint(0, 1) for num in range(0, len(cur_group400))]
                groups800_600[pt_group].append(
                    [p for p in self.get_players() if
                     p.income2 == 800 and p.participant.vars['pt_group_id'] == pt_group + 1])
                groups800_600[pt_group].append(
                    [p for p in self.get_players() if
                     p.income2 == 600 and p.participant.vars['pt_group_id'] == pt_group + 1])

                pairs = []
                for p_800_600 in range(0, len(groups800_600[pt_group][0])):
                    if lst_400_same[p_800_600] == 1:
                        pairs.append([groups800_600[pt_group][0][p_800_600], groups800_600[pt_group][1][p_800_600],
                                      cur_group400[0], 0])
                        groups400[pt_group].remove(cur_group400[0])
                    else:
                        pairs.append([groups800_600[pt_group][0][p_800_600], groups800_600[pt_group][1][p_800_600], 0,
                                      cur_group200[0]])
                        groups200[pt_group].remove(cur_group200[0])
                for left_400 in cur_group400:
                    rest_400.append(left_400)
                for left_200 in cur_group200:
                    rest_200.append(left_200)

                groups800_600[pt_group] = pairs

            final_groups = []
            random.shuffle(rest_400)
            random.shuffle(rest_200)
            for pt_group in groups800_600:
                for dg in pt_group:
                    vacant = dg.index(0)
                    if vacant == 2:
                        dg[vacant] = rest_400[0]
                        rest_400.remove(rest_400[0])
                    if vacant == 3:
                        dg[vacant] = rest_200[0]
                        rest_200.remove(rest_200[0])

                    final_groups.append(dg)

            random.shuffle(final_groups)
            difs = []
            print("******Round ", round, "****************final_groups: ", final_groups)
            for dg_index in range(0, len(final_groups)):
                cur_group = final_groups[dg_index]
                cur_group_id = cur_group[0].participant.vars['pt_group_id']

                cur_400_id = cur_group[2].participant.vars['pt_group_id']
                cur_200_id = cur_group[3].participant.vars['pt_group_id']

                identity = 0
                difs.append(cur_group[2].participant.vars['nt2_points'] - cur_group[3].participant.vars['nt2_points'])
                if cur_group_id == cur_400_id:
                    if cur_400_id == cur_200_id:
                        identity = 1
                    else:
                        if cur_group_id == 1:
                            identity = 2
                        if cur_group_id != 1 and cur_200_id == 1:
                            identity = 2
                        if cur_group_id != 1 and cur_200_id != 1:
                            identity = 3
                if cur_group_id != cur_400_id and cur_group_id == cur_200_id:
                    if cur_group_id == 1:
                        identity = 4
                    if cur_group_id != 1 and cur_400_id == 1:
                        identity = 4
                    if cur_group_id != 1 and cur_400_id != 1:
                        identity = 5
                print('cur_group: ', cur_group)
                print(
                "######Current group id: ", cur_group_id, ' 400id ', cur_400_id, ' 200id ', cur_200_id, 'identity ',
                identity)
                for member in cur_group:
                    member.participant.vars['decgroup_period2'].append(dg_index + 1)
                    member.participant.vars['identity_period2'].append(identity)
                if round == 7:
                    for member in cur_group:
                        print('member: ', member.participant.vars['decgroup_period2'],
                              member.participant.vars['identity_period2'])
            for dif in difs:
                nt2_dif_lst.append(dif)
        nt_dif_median = np.median(nt2_dif_lst)
        for p in self.get_players():
            p.participant.vars['nt2_dif_median'] = nt_dif_median

    def set_rg_tokens(self):
        for r in range(0,Constants.num_rounds):
            for p in self.get_players():
                cur_decgroup = p.participant.vars['decgroup_period2'][r]
                cur_rd = p.participant.vars['rd_period2'][r][cur_decgroup-1]
                cur_dv = None
                tokens = 0
                cur_comp = p.participant.vars['competition_period2'][r]
                if p.income2 == 400 and cur_comp == 1:
                    tokens -= 40
                if p.income2 == cur_rd:
                    cur_dv = p.participant.vars['dv_period2'][r]
                    if cur_dv == 1:
                        tokens = p.income2 - p.income2 * 0.2 + 100
                    if cur_dv == 2:
                        tokens = p.income2 - p.income2 * 0.4 + 200
                else:
                    for q in p.get_others_in_subsession():
                        if cur_decgroup == q.participant.vars['decgroup_period2'][r]:
                            if q.income2 == cur_rd:
                                cur_dv = q.participant.vars['dv_period2'][r]
                                if cur_dv == 1:
                                    tokens = p.income2 - p.income2 * 0.2 + 100
                                if cur_dv == 2:
                                    tokens = p.income2 - p.income2 * 0.4 + 200
                                break
                p.participant.vars['rg_tokens_period2'].append(tokens)
        for p in self.get_players():
            p.rg1_tokens = p.participant.vars['rg_tokens_period2'][0]
            p.rg2_tokens = p.participant.vars['rg_tokens_period2'][1]
            p.rg3_tokens = p.participant.vars['rg_tokens_period2'][2]
            p.rg4_tokens = p.participant.vars['rg_tokens_period2'][3]
            p.rg5_tokens = p.participant.vars['rg_tokens_period2'][4]
            p.rg6_tokens = p.participant.vars['rg_tokens_period2'][5]
            p.rg7_tokens = p.participant.vars['rg_tokens_period2'][6]
            p.rg8_tokens = p.participant.vars['rg_tokens_period2'][7]

    def set_rgab_tokens(self):
        for p in self.get_players():
            rd1a = p.participant.vars['rd2_period2'][0]
            rd1b = p.participant.vars['rd2_period2'][1]
            p.participant.vars['period2_payoff'] = p.participant.vars['rg_tokens_period2'][rd1a-1] \
                                                  + p.participant.vars['rg_tokens_period2'][rd1b-1]


class Player(BasePlayer):
    pt_group_id = models.StringField()
    income2 = models.IntegerField()
    nt2_rank = models.IntegerField()

    decgroup = models.IntegerField()
    nt_dif = models.IntegerField()
    competition = models.IntegerField()
    nt_dif_median = models.IntegerField()

    dv = models.IntegerField(widget=widgets.RadioSelect)
    rd = models.IntegerField()
    rd1a_period2 = models.IntegerField()
    rd1b_period2 = models.IntegerField()

    rg1_tokens = models.FloatField()
    rg2_tokens = models.FloatField()
    rg3_tokens = models.FloatField()
    rg4_tokens = models.FloatField()
    rg5_tokens = models.FloatField()
    rg6_tokens = models.FloatField()
    rg7_tokens = models.FloatField()
    rg8_tokens = models.FloatField()

    identity = models.IntegerField()

    def set_nt2_points(self):
        self.nt2_points = self.participant.vars["ET1_correct"] * 10
        if 3 in self.participant.vars["ET1_incorrect"]:
            self.nt2_points -= 10
        self.participant.vars['nt2_points'] = self.nt2_points

    def set_info(self, round_var):
        self.decgroup = self.participant.vars['decgroup_period2'][round_var-1]
        print("player: ", self.id_in_group, ' ', self.decgroup, " group lst: ", self.participant.vars['decgroup_period2'])
        self.income2 = self.participant.vars['income2']
        self.rd = self.participant.vars['rd_period2'][round_var-1][self.decgroup-1]
        self.rd1a_period2 = self.participant.vars['rd2_period2'][0]
        self.rd1b_period2 = self.participant.vars['rd2_period2'][1]
        self.identity = self.participant.vars['identity_period2'][round_var-1]
        self.pt_group_id = ['Klee-Bazille', 'Klee-Boch', 'Kandinsky-Boch'][self.participant.vars['pt_group_id'] - 1]

# Find the group memebers' information [income2, group_id]
# Compare dif of this round: token 400's raw pts - token 200's raw pts > dif median?

    def find_group_members_info(self, round_var):
        result = [0, 0, 0, 0]
        dif = 0
        group_id_400token = ''

        if self.income2 == 400:
            dif += self.participant.vars['nt2_points']
            group_id_400token = self.pt_group_id + '*'
        if self.income2 == 200:
            dif -= self.participant.vars['nt2_points']

        result[int((self.income2 - 200) / 200)] = [self.pt_group_id, self.income2, self.participant.vars['nt2_points']]
        for other in self.get_others_in_subsession():
            if other.participant.vars['decgroup_period2'][round_var - 1] == self.decgroup:
                income = other.participant.vars['income2']
                if income == 400:
                    result[1] = [['Klee-Bazille', 'Klee-Boch', 'Kandinsky-Boch'][
                                     other.participant.vars['pt_group_id'] - 1] + '*',
                                 income,
                                 other.participant.vars['nt2_points']]
                else:
                    result[int((income - 200) / 200)] = [
                        ['Klee-Bazille', 'Klee-Boch', 'Kandinsky-Boch'][other.participant.vars['pt_group_id'] - 1],
                        income,
                        other.participant.vars['nt2_points']]
                # Define the dif in this dec group
                if income == 400:
                    dif += other.participant.vars['nt2_points']
                    group_id_400token = ['Klee-Bazille', 'Klee-Boch', 'Kandinsky-Boch'][
                                            other.participant.vars['pt_group_id'] - 1] + '*'
                if income == 200:
                    dif -= other.participant.vars['nt2_points']

        self.nt_dif = dif
        print("members: ", result)
        return [result, group_id_400token]

    def set_competition(self):
        self.nt_dif_median = self.participant.vars['nt2_dif_median']
        if self.nt_dif > self.participant.vars['nt2_dif_median']:
            self.competition = 0
        else:
            self.competition = 1
        self.participant.vars['competition_period2'].append(self.competition)
