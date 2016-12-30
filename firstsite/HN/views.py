from django.shortcuts import render
import requests,re,io,json
import pandas as pd
import psycopg2


#from django_user_agents.utils import get_user_agent
from datetime import datetime

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


def connection():
        con = psycopg2.connect("dbname='' user='' host='' password=''")
        return con

con=connection()

def index(request):
	cur=con.cursor()
	cur.execute("""select id,by,score,title,url from hn_stories where score > 5 order by score desc limit 250 """)
	instance=cur.fetchall()
	return render(request,'index.html',{'instance':instance})


