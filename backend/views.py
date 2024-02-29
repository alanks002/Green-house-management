from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from backend.models import singledb, State, City



# Create your views here.
def green_main_view(request):
    return render(request,'index_back.html')

def add_single(request):
    data = State.objects.all()
    return render(request,'add_single.html',{"data":data})

def post_single(request):
    if request.method=="POST":
        a=request.POST.get("Title")
        b = request.FILES["Profile"]
        c= request.POST.get("Icon")
        d= request.POST.get("State")
        obj=singledb(Title=a,Profile=b, Icon=c ,State=d)
        obj.save()
        return redirect(add_single)

def single_table(request):
    data=singledb.objects.all()
    return render(request,'single_table.html',{"data":data})

def single_update(request, c_id):
    if request.method=="POST":
        a = request.POST.get("Title")
        c = request.POST.get("Icon")
        d=request.POST.get("State")

        try:
            img = request.FILES["Profile"]
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = singledb.objects.get(id=c_id).Profile
    singledb.objects.filter(id=c_id).update(Title=a,Profile=file,Icon=c,State=d)
    return redirect(add_single)

def single_edit(request, c_id):
    data=Statedb.objects.all()
    vdata=singledb.objects.get(id=c_id)
    return render(request,'single_edit.html',{"vdata":vdata,"data":data})

def single_delete(request, c_id):
    vdata=singledb.objects.filter(id=c_id)
    vdata.delete()
    return redirect(single_table)

def state_view(request):
    return render(request,'state.html',)

def city_view(request):
    return render(request,'city.html')
def add_state(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        State.objects.create(name=name)
    return redirect(state_view)

def add_city(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        state_id = request.POST.get('state')
        state = State.objects.get(pk=state_id)
        City.objects.create(name=name, state=state)
        return redirect(add_city)  # Redirect to the same page after adding a city

    states = State.objects.all()
    return render(request, 'city.html', {'states': states})