from rest_framework.decorators import api_view
import os
from django.shortcuts import render
import pandas
import time


@api_view(['GET'])
def index(request):
    path = 'assets/data/output.csv'
    ds = pandas.read_csv(path)
    ti_c = os.path.getctime(path)
    ti_m = os.path.getmtime(path)

    # Converting the time in seconds to a timestamp
    c_ti = time.ctime(ti_c)
    m_ti = time.ctime(ti_m)
    print(m_ti)
    titles=ds["titles"]
    details=ds["details"]
    images=ds["images"]
    data = []
    [ data.append([titles[i],details[i],images[i]]) for i in range(len(titles))]

    return render(request, 'index.html', {"data":data,"date":m_ti})
