# Tests for User Profile functions
from django.test import TestCase
from Feb092019_XdHacks_Levana.backend import UserProfile


class TestUserProfile(TestCase):

    def setUp(self):
        UserProfile.create("clim", "lyang@cdrd.ca", "wiggy123")

    def test_get_username(self):
        result = UserProfile.AppUser.get_username()
        self.assertEqual(result, "clim")
