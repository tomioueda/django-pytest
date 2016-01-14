# External Libraries
import pytest

# DJANGO LIBRARIES
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page


# TEST CASES ##########################################
def test_root_url_resolves_to_home_page_view():
    found = resolve('/')
    assert found.func == home_page

def test_home_page_returns_correct_html():
    request = HttpRequest()
    response = home_page(request)
    expected_html = render_to_string('home.html')
    assert response.content.decode() == expected_html
