
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        edutitle = request.POST['edutitle']
        timeedu = request.POST['timeedu']
        scoreedu =  request.POST['scoreedu']
        expti = request.POST['expti']
        expyr = request.POST['expyr']
        expde = request.POST['expde']
        expti1 = request.POST['expti1']
        expyr1 = request.POST['expyr1']
        expde1 = request.POST['expde1']
        skill1 = request.POST['skill1']
        skill2 = request.POST['skill2']
        skill3 = request.POST['skill3']
        skill4 = request.POST['skill4']
        context = {'name':name , "email":email ,"mobile":mobile , "address" :address ,"edutitle":edutitle ,"timeedu":timeedu,"scoreedu":scoreedu ,"expti":expti, "expyr":expyr ,"expde":expde , "expti1":expti1 , "expyr1" :expyr1 ,"expde1" : expde1 , "skill1" : skill1 , "skill2": skill2 , "skill3":skill3 , "skill4":skill4 } 
        return render(request , 'ghar.html' , context )

    return render(request , 'cv.html' )


def ghar(request):
    return render(request , 'ghar.html')

def cv(request):
    return render(request , 'cv.html')