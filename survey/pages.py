from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants
from . import  models


class Demographics(Page):
    form_model = 'player'
    form_fields = ['q1',
                   'q2',
                   'q3',
                   'q4',
                   'q5',
                   'q6']

class Demographics2(Page):
    form_model = models.Player
    form_fields = ['q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13']

class Demographics3(Page):
    form_model = models.Player
    form_fields = ['q14', 'q15', 'q16', 'q17']

class Demographics4(Page):
    form_model = models.Player
    form_fields = ['q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27']


class EndofSurvey(Page):
    pass

page_sequence = [
    Demographics,
    Demographics2,
    Demographics3,
    Demographics4,
    EndofSurvey
]
