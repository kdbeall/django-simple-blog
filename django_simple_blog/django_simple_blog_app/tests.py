from django.test import TestCase
from .models import Entry

# Create your tests here.


class EntryModelTest(TestCase):
    def test_verbose_name(self):
        self.assertEqual(str(Entry._meta.verbose_name_plural), "entries")
