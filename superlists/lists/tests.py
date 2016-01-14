from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page
import pytest

# class HomePageTest(TestCase):
#
#     def test_root_url_resolves_to_home_page_view(self):
#         found = resolve('/')
#         self.assertEqual(found.func, home_page)

def test_home():
    found = resolve('/')
    assert found.func == home_page

def test_home():
    found = resolve('/main')
    assert found.func == home_page