import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Comment
# Create your tests here.


class CommentMethodTests(TestCase):

    def test_was_published_recently_with_future_comment(self):
        time = timezone.now() + datetime.timedelta(days=5)
        future_comment = Comment(pub_date=time)
        self.assertEqual(future_comment.was_published_recently(), False)

    def test_was_published_recently_with_old_comment(self):
        time = timezone.now() - datetime.timedelta(days=5)
        old_comment = Comment(pub_date=time)
        self.assertEqual(old_comment.was_published_recently(), False)

    def test_was_published_recently_with_recent_comment(self):
        time = timezone.now() - datetime.timedelta(minutes=5)
        recent_comment = Comment(pub_date=time)
        self.assertEqual(recent_comment.was_published_recently(), True)
