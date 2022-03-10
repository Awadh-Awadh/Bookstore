from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView

# Create your tests here.

class TestHomePage(SimpleTestCase):



  def setUp(self):
    url = reverse('home')
    self.response = self.client.get(url)



  def test_simple_homepage_testcase(self):
    self.assertTrue(self.response.status_code, 200)


  def test_homepage_url_name(self):
    self.assertTrue(self.response.status_code, 200)


  def test_template_used(self):
    self.assertTemplateUsed(self.response, 'home.html' )

  def test_homepage_url_resolve_HomePageView(self):
    view = resolve('/')
    self.assertEqual(
      view.func.__name__, HomePageView.as_view().__name__
    )
