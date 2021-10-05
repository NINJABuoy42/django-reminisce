from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

# Create your views here.
def home(request):
    return render(request,'home.html')

def yearbook(request):
    sheet_id='1SQTDlT49uR_aShPF2J96tm0D83u8KAfdqAW1a6vnJ2o'
    df=pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv')
    record=df.to_dict(orient='record')
    return render(request,'yearbook.html',{'record':record})


def profile(request):
    sheet_id='1SQTDlT49uR_aShPF2J96tm0D83u8KAfdqAW1a6vnJ2o'
    df=pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv')
    profile=df.to_dict(orient='profile')
    #print(df)
    return render(request,'profile.html',{'profile':profile})
