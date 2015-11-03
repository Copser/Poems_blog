from django.test import TestCase
from models import Post


# Create your tests here.
class PostTests(TestCase):

    """Docstring for PostTests. """
    def test_str(self):
        my_title = Post(
            title='Ovo je blog Profesora i pesnika Pere Skovo-a')
        self.assertEquals(
            str(my_title),
            'Ovo je blog Profesora i pesnika Pere Skovo-a',
        )
