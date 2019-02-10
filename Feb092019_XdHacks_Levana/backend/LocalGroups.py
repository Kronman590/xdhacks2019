from django.db import models
from datetime import datetime

MAX_POST_LENGTH = 300
MAX_NAME_LENGTH = 30
POST_TYPES = (
        ("goal", "Goal"),
        ("sp", "Self Post"),
        ("ch", "Challenge"),
        ("ir", "Information Resources")
    )

class GroupPost(models.Model):

    # type of post
    POST_TYPE = POST_TYPES
    # id of author of the post
    author = models.CharField("name", max_length=MAX_NAME_LENGTH)
    # body of the post
    body = models.CharField("bodyText", max_length=MAX_POST_LENGTH)
    # time posted
    timestamp = datetime