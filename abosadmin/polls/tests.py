import datetime
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone

from polls.models import Question


class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions
        whose pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for quetions whose
        pub_date is within the last day
        """
        time = timezone.now()
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(
        question_text=question_text,
        pub_date=time)


class QuestionViewTests(TestCase):

    def test_index_view_with_no_questions(self):
        """
        if no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_a_past_question(self):
        create_question(question_text='Past Question.', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past Question.>']
        )

    def test_index_view_with_a_future_question(self):
        create_question(question_text='future question.', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(
            response,
            "No polls are available.",
            status_code=200)
        self.assertQuerysetEqual(
            response.context['latest_question_list'], [])

    def test_index_view_with_future_question_and_past_question(self):
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(
            response,
            ""
        )


# Create your tests here.
