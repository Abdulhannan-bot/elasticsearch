from django.contrib import admin

# Register your models here.

from .models import *

class SampleAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'description']

admin.site.register(Sample, SampleAdmin)


# import csv
# rows = []
# with open("dataset.csv", 'r') as file:
#     csvreader = csv.reader(file)
#     header = next(csvreader)
#     for row in csvreader:
#         rows.append(row)
# print(header)
# print(rows)