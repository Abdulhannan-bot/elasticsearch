from django.db import models

# Create your models here.



class Sample(models.Model):
  title = models.TextField(null = True)
  description = models.TextField(null = True)


  def __str__(self):
    return str(self.title)

# for i in new_row:
#   Sample.objects.create(title = i[-1], description = i[0])