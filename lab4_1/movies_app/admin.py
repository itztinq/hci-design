from django.contrib import admin

from movies_app.models import ProductionCompany, Movie

admin.site.register(ProductionCompany)
admin.site.register(Movie)