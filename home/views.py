from django.shortcuts import render,redirect

from Students.forms import junior_round_form

# Create your views here.
def index(request):
    if request.method == 'POST':
        junior_form = junior_round_form(request.POST or None, request.FILES or None)
        if junior_form.is_valid():
            junior_form = junior_form.save()
            return redirect('home')
    else:
        junior_form = junior_round_form()


    return render(request,'index.html',{'junior_form':junior_form})