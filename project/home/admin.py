from django.contrib import admin
from .models import Books, Contact

# Register your models here.
admin.site.register(Books)
admin.site.register(Contact)


admin.site.site_header = 'My Custom Admin Header'

# Change the site title
admin.site.site_title = 'My Custom Admin Title'

# Change the index title
admin.site.index_title = 'My Custom Admin Index Title'