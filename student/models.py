from django.db import models

# Create your models 
class stud(models.Model):
  naam=models.CharField(max_length=100,null=False,blank=False)
  roll=models.IntegerField(unique=True)
  sem=models.IntegerField()

  def _str_(self):
      return str(self.roll) 