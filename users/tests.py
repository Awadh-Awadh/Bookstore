from django.test import TestCase

from django.contrib.auth import get_user_model



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