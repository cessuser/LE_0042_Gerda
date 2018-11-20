from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Danlin Chen'
class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1
    age = [i for i in range(16, 100)]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    q1 = models.IntegerField(
        label='What is your age?',
        choices=Constants.age)

    q2 = models.StringField(
        choices=['Male', 'Female', 'Other'],
        label='What is your gender?',
        widget=widgets.RadioSelect)

    q3 = models.StringField(
        choices=['Yes', 'No'],
        label='Have you participated in Economics or Psychology experiments before?',
        widget=widgets.RadioSelect
    )

    q4 = models.StringField(
        choices=['Humanities','Mathematical', 'Physical, and Life Sciences','Medical Sciences',
                 'Economics or PPE (Politics, Philosophy, and Economics)','Other Social Sciences '],
        label='Field of study:',
        widget=widgets.RadioSelect
    )
    q5 = models.StringField(
        choices=['Graduate', 'Undergraduate'],
        label='Degree:',
        widget=widgets.RadioSelect
    )
    q6 = models.StringField(
        choices=['1','2','3','4','5+'],
        label = 'Which year are you in your program?'
    )
    q7 = models.StringField(
        choices=['0 - I avoid taking risks', '1','2','3','4','5','6','7','8','9', '10 - I take risks', 'Prefer not to say'],
        label='How do you see yourself: Are you in general a person who takes risks or do you try to avoid taking risks?',
        widget=widgets.RadioSelectHorizontal
    )
    q8 = models.StringField(
        label='Generally speaking, would you say that most people can be trusted or that you can’t be too careful in dealing with people?',
        choices =['0 - You can’t be too careful', '1','2','3','4','5','6','7','8','9', '10 - Most people can be trusted', 'Prefer not to say'],
        widget=widgets.RadioSelectHorizontal
    )
    q9 = models.StringField(
        label='“If I help someone I expect some help in return”.',
        choices= ['Agree strongly','Agree','Neither agree nor disagree','Disagree','Disagree strongly','Prefer not to say'],
        widget=widgets.RadioSelect
    )
    q10 = models.StringField(
        label='“It is important that every person in the world should be treated equally. Everyone should have equal opportunities in life”.',
        choices=['Agree strongly','Agree','Neither agree nor disagree','Disagree','Disagree strongly','Prefer not to say'],
        widget=widgets.RadioSelect
    )
    q11 = models.StringField(
        label='“The government should redistribute income from the better off to those who are less well off”.',
        choices=['Agree strongly','Agree','Neither agree nor disagree','Disagree','Disagree strongly','Prefer not to say'],
        widget=widgets.RadioSelect
    )
    q12 = models.StringField(
        label='“The government should spend more money on welfare benefits for the poor, even if it leads to higher taxes”.',
        choices=['Agree strongly','Agree','Neither agree nor disagree','Disagree','Disagree strongly','Prefer not to say'],
        widget=widgets.RadioSelect
    )
    q13 = models.StringField(
        label='In politics people sometimes talk of “left” and “right”. Where would you place yourself on this scale, where 0 means the left and 10 means the right?',
        choices=['0 - Left', '1','2','3','4','5','6','7','8','9', '10 - Right','Prefer not to say'],
        widget=widgets.RadioSelectHorizontal
    )
    q14 = models.StringField(
        label='Which participant pays the highest amount of taxes in absolute terms in Scheme 1?',
        choices=['Participant 1', 'Participant 2', 'Participant 3', 'Participant 4'],
        widget=widgets.RadioSelect
    )
    q15 = models.StringField(
        label='Which participant benefits the most in absolute terms from Scheme 1?',
        choices=['Participant 1', 'Participant 2', 'Participant 3', 'Participant 4'],
        widget=widgets.RadioSelect
    )
    q16 = models.StringField(
        label='What is the total sum of taxes paid by participants in Scheme 2?',
        choices=['600', '800', '1000', '1200'],
        widget=widgets.RadioSelect
    )
    q17 = models.StringField(
        label='Now suppose that participant 2 had lost the competition and would have started the round with earnings of '
              '360 tokens instead of 400 tokens. What do you think would happen to the transfers in both schemes?',
        choices=['They will remain the same.', 'They will become smaller for everyone.',
                 'They will only become smaller for participant 2.'],
        widget=widgets.RadioSelect
    )
    q18 = models.StringField(
        label='You were assigned to the ________ group during the experiment.',
        choices=['Klee-Bazille','Kandinsky-Boch','Klee-Boch'],
        widget=widgets.RadioSelect
    )
    q19 = models.StringField(
        label='Klee-Bazille group',
        choices = ['1 - Not at all','2','3','4','5','6','7 - Very much'],
        widget = widgets.RadioSelectHorizontal
    )
    q20 = models.StringField(
        label='Klee-Boch group',
        choices=['1 - Not at all','2','3','4','5','6','7 - Very much'],
        widget=widgets.RadioSelectHorizontal
    )
    q21 = models.StringField(
        label='Kandinsky-Boch group',
        choices=['1 - Not at all', '2', '3', '4', '5', '6', '7 - Very much'],
        widget=widgets.RadioSelectHorizontal
    )
    q22 = models.StringField(
        label='In Part 2 of the experiment, you were asked to choose your preferred tax and transfer scheme. '
                'How would you describe the strategy you used?',
        choices=['Try to maximize my number of tokens.','Try to maximize the number of tokens for the entire decision group.',
                 'Try to maximize the number of tokens for my group members within the decision group.',
                 'Try to maximize the number of tokens for the poorest group member.', 'Other.'],
        widget=widgets.RadioSelect
    )
    q23 = models.StringField(
        label='Klee',
        choices=['1 - Not at all familiar', '2','3','4','5','6','7','8','9', '10 - Very familiar'],
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    q24 = models.StringField(
        label='Kandinsky',
        choices=['1 - Not at all familiar', '2','3','4','5','6','7','8','9', '10 - Very familiar'],
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    q25 = models.StringField(
        label='Boch',
        choices=['1 - Not at all familiar', '2','3','4','5','6','7','8','9', '10 - Very familiar'],
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    q26 = models.StringField(
        label='Bazille',
        choices=['1 - Not at all familiar', '2','3','4','5','6','7','8','9', '10 - Very familiar'],
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    q27 = models.StringField(
        label='What do you think the experiment was about?',
        widget=widgets.TextInput()
    )
