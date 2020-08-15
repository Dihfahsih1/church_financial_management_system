from django import forms
from .models import *


class SpendForm(forms.ModelForm):
    class Meta:
        model=Spend
        fields=('Date','PaymentMadeTo','ReasonForPayment','Amount','AmountInWords')

class SundryForm(forms.ModelForm):
    class Meta:
        model=Sundry
        fields=('Date','PaymentMadeTo','Amount','AmountInWords','ReasonForPayment')

class SalaryForm(forms.ModelForm):
    class Meta:
        model=Salary
        fields = ('Date','Name','Month','Amount','AmountInWords')

class StaffDetailsForm(forms.ModelForm):
    class Meta:
        model=StaffDetails
        fields=('image','FistName','SecondName','Salary','Role','Duties','Sex','Contact')

class OfferingsForm(forms.ModelForm):
    class Meta:
        model=Offerings
        fields = ('Date','DayOfTheWeek','TotalOffering','AmountInWords')
class PledgesForm(forms.ModelForm):
    class Meta:
        model=Pledges
        fields = ('Date','DayOfTheWeek','PledgeMadeBy','Reason','Amount','AmountInWords')
class TithesForm(forms.ModelForm):
    class Meta:
        model=Tithes
        fields = ('Date','DayOfTheWeek','TitheMadeBy','Amount','AmountInWords')