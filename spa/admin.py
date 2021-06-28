from django.contrib import admin

# Register your models here.
from requests_cache import CachedSession
session = CachedSession('example_cache', backend='memory')
