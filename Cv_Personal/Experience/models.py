from django.db import models
from datetime import datetime, date

from django import template

register = template.Library()

# Create your models here.

class ExperienceModel(models.Model):

    start_date = models.DateField(default=date(1984, 11, 24), editable=True, blank=True)
    end_date = models.DateField(default=date(1984, 11, 24), editable=True, blank=True)
    empleador = models.CharField(max_length=100)
    resumen = models.CharField(max_length=500)

    @property
    def age_in_months(self):
        if self.end_date == date(1984, 11, 24):
            end_date_today = date.today()
            num_months = (end_date_today.year - self.start_date.year) * 12 + (end_date_today.month - self.start_date.month)
            num_years = num_months//12
            num_months_by_year = num_months % 12
            num_years = num_months//12
            output_string = """{} años, {} meses.""".format(num_years, num_months_by_year)
            return output_string
        else:
            num_months = (self.end_date.year - self.start_date.year) * 12 + (self.end_date.month - self.start_date.month)
            num_years = num_months//12
            num_months_by_year = num_months % 12
            num_years = num_months//12
            output_string = """{} años, {} meses.""".format(num_years, num_months_by_year)
            return output_string
    
    @property
    def end_date_view(self):
        if self.end_date == date(1984, 11, 24):
            return "Actualidad"
        else:
            return self.end_date
    
    @register.filter
    def get_type(value):
        return type(value)



