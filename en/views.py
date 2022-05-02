
import base64
import io
from django.shortcuts import redirect, render
from PIL import Image  


# Create your views here.
#using bytesio() to save temporarily to render without saving it into db to render it out
def index(request):
    if request.method == 'POST':
        avatar = request.FILES['avatar']
        img = Image.open(avatar) 
        data = io.BytesIO()
        img.save(data, "JPEG")
        encoded_img = base64.b64encode(data.getvalue())
        decoded_img = encoded_img.decode('utf-8')
        img_data = f"data:image/jpeg;base64,{decoded_img}"
        name = request.POST.get('name')
        passion = request.POST.get('passion')
        email = request.POST.get('email')
        mobile = request.POST.get('number')
        address = request.POST.get('address')
        edutitle = request.POST.get('edutitle')
        timeedu = request.POST.get('timeedu')
        scoreedu =  request.POST.get('scoreedu')
        expti = request.POST.get('expti')
        expyr = request.POST.get('expyr')
        expde = request.POST.get('expde')
        expti1 = request.POST.get('expti1')
        expyr1 = request.POST.get('expyr1')
        expde1 = request.POST.get('expde1')
        skill1 = request.POST.get('skill1')
        skill2 = request.POST.get('skill2')
        skill3 = request.POST.get('skill3')
        skill4 = request.POST.get('skill4')
        context = {'avatar' : img_data , 'name':name ,"passion" : passion , "email":email ,"mobile":mobile , "address" :address ,"edutitle":edutitle ,"timeedu":timeedu,"scoreedu":scoreedu ,"expti":expti, "expyr":expyr ,"expde":expde , "expti1":expti1 , "expyr1" :expyr1 ,"expde1" : expde1 , "skill1" : skill1 , "skill2": skill2 , "skill3":skill3 , "skill4":skill4 } 
        return render(request , 'ghar.html' , context )

    return render(request , 'cv.html' )
