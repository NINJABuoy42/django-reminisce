from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

# Create your views here.
def home(request):
    return render(request,'home.html')

def yearbook(request):
    sheet_id='1ra5cK1p_oFGZxDwxr0Y1RCjNw-rmZGxECt0Tw1WObiE'
    df=pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv')
    record=df.to_dict(orient='records')
    print(record)
    return render(request,'yearbook.html',{'record':record})