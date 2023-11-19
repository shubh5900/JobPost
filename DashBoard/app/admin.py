from django.contrib import admin

# Register your models here.
from .models import Manager
from .models import JobList
from .models import Candidates
from .models import ApplyCondidate

admin. site. register(Manager)
admin.site.register(JobList)
admin.site.register(Candidates)
admin.site.register(ApplyCondidate)
