from django.contrib import admin

# Register your models here.
from .models import Donate
from .models import Feedback
from .models import Pets


admin.site.register(Donate)
admin.site.register(Feedback)
admin.site.register(Pets)
