# Tests for User Profile functions
from Feb092019_XdHacks_Levana.backend import UserProfile
import unittest

class TestUserProfile(unittest.TestCase):

    def test_get_username(self):
        user = UserProfile("clim", "lyang@cdrd.ca", "wiggy123")
        result = user.get_username()



