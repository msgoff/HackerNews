from django.shortcuts import render
import requests,re,io,json
import pandas as pd



#from django_user_agents.utils import get_user_agent
from datetime import datetime
from REC.models import stories, comments
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import numpy as np
from django.db.models import Q
#from .forms import feedbackForm
pd.options.mode.chained_assignment = None 
from django.shortcuts import redirect
import os
from time import time
import requests

def index(request,id=None):
    filtering=int(time())-9999999
    lst=[pd.Series(x) for x in stories.objects.filter(score__gte=5).exclude(kids=u'').values()[:1000]]
    df=pd.concat(lst,axis=1).T
    df['domain']=df.url
    df['time_stamp']=df.time
    df=df[['time','score','title','by','url','ID','domain','descendants','time_stamp','kids']]
    df.time=df.time.apply(lambda x: datetime.now()-datetime.fromtimestamp(float(x)) or '')
    df=df.sort_values('score')
    col=df.columns
    user_agent=request.META["HTTP_USER_AGENT"]
    context={'instance':df.iterrows(),'user_agent':user_agent,'col':col}
    return render(request,'index.html',context)


def cmmnts(request,id=None):
    lst=[pd.Series(x) for x in comments.objects.values()[:2000]]


    df=pd.concat(lst,axis=1).T
    df=df[['ID','by','text']]
    col=df.columns
    
    context={'instance':df.iterrows(),'col':col}
    return render(request,'comments.html',context)
