from django.core.management.base import BaseCommand
import random

from polls.models import Question, Choice
from django.utils import timezone

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    print("Delete Address instances")
    Choice.objects.all().delete()
    Question.objects.all().delete()


def create_question():
    """Creates an address object combining different elements from the list"""
    print("Creating question")
    question_text_1 = "Question 1"
    choice_text_1 = "Choice 1"
    choice_text_2 = "Choice 2"
    choice_text_3 = "Choice 3"

    question = Question(question_text=question_text_1, pub_date=timezone.now())
    question.save()

    question.choice_set.create(choice_text=choice_text_1, votes=0)
    question.choice_set.create(choice_text=choice_text_2, votes=0)
    question.choice_set.create(choice_text=choice_text_3, votes=0)
    return question


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    create_question()
