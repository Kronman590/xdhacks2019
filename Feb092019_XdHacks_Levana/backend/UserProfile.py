from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator


# user profile and related functions
class AppUser:

    # TODO: finish making objects to initialize user class
    # makes new user objects
    def __init__(self, name, email, password):
        self.app_user = UserManager.obj.create_user(name, email=email, password=password)
        # initialize empty list of goals
        self.user_goals = []
        # self.calendar = initialize user calendar
        # self.localGroups = find local groups

    def get_username(self):
        return User.get_username(self.app_user())

    # TODO:
    def get_email(self):
        return ""