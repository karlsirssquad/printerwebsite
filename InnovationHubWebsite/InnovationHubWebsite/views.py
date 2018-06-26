from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.

#HomePage Views
def HomePage(request):
    context = {'Quota' : '00:31:23'}
    return render(request, 'HomePage.html', context)


#Schedule Views
def Schedule(request):
    context = {'Quota' : '00:31:23'}
    return render(request, 'SchedulePage.html', context)


#Submit Views
def Submission(request):
    context = {'Quota' : '00:31:23'}
    return render(request, 'SubmitFile.html', context)

def Preview(request):
    return HttpResponse("Preview your model")

def SubmissionForm(request):
    return HttpResponse("Submission Form")

def Success(request):
    return HttpResponse("Submission Success")

def Fail(request):
    return HttpResponse("Submission Fail")


#Account Views
def AccountData(request):
    context = {'Quota' : '00:31:23'}
    return render(request, 'AccountData.html', context)

def EditAccount(request):
    return HttpResponse("Account Editor")

def Login(request):
    return HttpResponse("Login to Account")

def layout(request):
    context = {'Quota' : '00:31:23'}
    return render(request, 'layout.html', context)


#The Carl Segment
def CarlPage(request):
    context = {'Quota' : '00:31:23'}
    return render(request, 'CarlSegment.html', context)


#Featured Prints
def Featured(request):
    context = {'Quota' : '00:31:23'}
    return render(request, 'FeaturedPrints.html', context)


#Raw Data Views
def Data(request):
    context = {}
    return render(request, 'RawData.html', context)
