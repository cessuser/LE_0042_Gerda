from otree.api import Currency as c, currency_range

from . import pages
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):

    def play_round(self):

        yield (pages.Demographics, {
            'q1': 22,
            'q2': 'Female',
            'q3': 'Yes',
            'q4': 'Mathematical',
            'q5': 'Graduate',
            'q6': '1'

        })
        yield (pages.Demographics2, {
            'q7': '1',
            'q8': '1',
            'q9': 'Agree',
            'q10': 'Agree',
            'q11': 'Agree',
            'q12': 'Agree',
            'q13': '2'

        })
        yield (pages.Demographics3, {
            'q14': 'Participant 1',
            'q15': 'Participant 2',
            'q16': '1000',
            'q17': 'They will remain the same.',

        })
        yield (pages.Demographics4, {
            'q18': 'Klee-Boch',
            'q19': '2',
            'q20': '2',
            'q21': '3',
            'q22': 'Try to maximize my number of tokens.',
            'q23': '2',
            'q24': '2',
            'q25': '2',
            'q26': '3',
            'q27': 'a'

        })