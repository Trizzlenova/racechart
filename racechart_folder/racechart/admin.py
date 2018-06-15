from django.contrib import admin
from .models import Driver, Team, Race, Standing, Result

admin.site.register(Driver)
admin.site.register(Team)
admin.site.register(Race)
admin.site.register(Standing)
admin.site.register(Result)

