from django.db import models

import django.contrib.auth.models models


class User(models.User):

    def __init__(self, username, password):
        super().__init__(username, password)


# Create your models here.
