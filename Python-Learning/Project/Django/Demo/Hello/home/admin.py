from django.contrib import admin
from home.models import Contact
from home.models import Register 

# Added for models migration with import Contact (class created in models)
# Home -> App -> From there we are getting models like Contact as a example.

# Register your models here.
admin.site.register(Contact)  ##
admin.site.register(Register)