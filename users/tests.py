from django.urls import reverse, resolve
from django.test import TestCase

from django.contrib.auth import get_user_model
from .views import SignupView
from .forms import CustomUserCreationForm



class TestModels(TestCase):

     
     def test_create_user(self):
         User = get_user_model()
         user = User.objects.create_user(

          username = "awadh",
          email = "awadh1@gmail.com",
          password = "awadh11"

         )
         self.assertEqual(user.username, "awadh")
         self.assertEqual(user.email, "awadh1@gmail.com")
         self.assertTrue(user.is_active)
         self.assertFalse(user.is_superuser)
         self.assertFalse(user.is_staff)

     def test_create_superuser(self):
          User = get_user_model()
          user = User.objects.create_superuser(
            username = "sam",
            email= "sam@gmail.com",
            password = "123a2a!q"
          )

          self.assertEqual(user.username, "sam")
          self.assertEqual(user.email, "sam@gmail.com")
          self.assertTrue(user.is_active)
          self.assertTrue(user.is_superuser)
          self.assertTrue(user.is_staff)

class SignupPageTests(TestCase):

  def setUp(self):
     url = reverse('signup')
     self.response = self.client.get(url)


  def test_signup_template(self):
    self.assertEqual(self.response.status_code, 200)
    self.assertTemplateUsed(self.response, 'signup.html')
    self.assertContains(self.response, 'Sign Up')


  def test_creation_form(self):
    form = self.response.context.get("form")
    self.assertIsInstance(form, CustomUserCreationForm)
    self.assertContains(self.response, 'csrfmiddlewaretoken')

  def test_signup_resolves_SignupView(self):
    view = resolve('/accounts/signup/')
    self.assertEqual(
      view.func.__name__, SignupView.as_view().__name__
    )
    
