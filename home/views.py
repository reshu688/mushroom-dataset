from django.shortcuts import render
from joblib import load
import pickle
import sklearn

# Create your views here.

model = pickle.load(open("model.pkl",'rb'))

def homepage(req):
    return render(req,"home.html")

def prediction(req):
    cap_diameter = int(req.POST.get('cap-diameter'))
    cap_shape = int(req.POST.get('cap-shape'))
    gill_attachment = int(req.POST.get('gill-attachment'))
    gill_color = int(req.POST.get('gill-color'))
    stem_height = float(req.POST.get('stem-height'))
    stem_width = float(req.POST.get('stem-width'))
    stem_color = int(req.POST.get('stem-color'))
    season = req.POST.get('season')
    instance=[[cap_diameter,cap_shape,gill_attachment,gill_color,stem_height,stem_width,stem_color,season]]
    print(instance)
    prediction=model.predict(instance)
    return render(req,"result.html",{'value':prediction})