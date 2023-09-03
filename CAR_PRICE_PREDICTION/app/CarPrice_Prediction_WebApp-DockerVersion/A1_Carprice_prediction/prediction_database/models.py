from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms

# Create your models here.
class Input(models.Model):
    input_year = models.CharField(
        max_length=4,
        choices= [('1980','1980'),('1981','1981'),('1982','1982'),
                  ('1983','1983'),('1984','1984'),('1985','1985'),
                  ('1986','1986'),('1987','1987'),('1988','1988'),
                  ('1989','1989'),('1990','1990'),('1991','1991'),
                  ('1992','1992'),('1993','1993'),('1994','1994'),
                  ('1995','1995'),('1996','1996'),('1997','1997'),
                  ('1998','1998'),('1999','1999'),('2000','2000'),
                  ('2001','2001'),('2002','2002'),('2003','2003'),
                  ('2004','2004'),('2005','2005'),('2006','2006'),
                  ('2007','2007'),('2008','2008'),('2009','2009'),
                  ('2010','2010'),('2011','2011'),('2012','2012'),
                  ('2013','2013'),('2014','2014'),('2015','2015'),
                  ('2016','2016'),('2017','2017'),('2018','2018'),
                  ('2019','2019'),('2020','2020'),('2021','2021'),
                  ('2022','2022'),('2023','2023'),],
        default='1980'
    )
    input_max_power = models.FloatField(
        null=True,
        default=None,
        # validators=[ # This one lead to Bug!
        #     MinValueValidator(0),
        #     MaxValueValidator(1000)
        # ]
    )
    input_km_driven = models.FloatField(
        null=True,
        default=None,
        # validators=[ # This one lead to Bug!
        #     MinValueValidator(0),
        #     MaxValueValidator(3000000)
        # ]
    )
    

class Output(models.Model):
    output_selling_price = models.CharField(
        max_length=20,
        default='Please SUBMIT Data'
    )

class InputForm(forms.ModelForm):
    class Meta:
        model = Input
        fields = '__all__'
        labels = {
            'input_year': 'YEAR OF CAR',
            'input_km_driven': 'KM DRIVEN',
            'input_max_power': 'MAX POWER',
        }

class OutputForm(forms.ModelForm):
    class Meta:
        model = Output
        fields = '__all__'
        labels = {
            'output_selling_price': 'SELLING PRICE : '
        }