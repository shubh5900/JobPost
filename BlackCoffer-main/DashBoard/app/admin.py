from django.contrib import admin

# Register your models here.
from .models import Manager
from .models import JobList
from .models import Candidates

admin. site. register(Manager)
admin.site.register(JobList)
admin.site.register(Candidates)
