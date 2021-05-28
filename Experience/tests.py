from django.test import TestCase
from datetime import date
# Create your tests here.
start_date = date(2019, 11, 1)
end_date = date(2021, 6, 4)
def age_in_months(end_date, start_date):
    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    num_years = num_months//12
    num_months_by_year = num_months % 12
    return (num_years, num_months_by_year )

print('>> ', age_in_months(end_date, start_date))

#print(end_date.year)