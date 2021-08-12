from django.shortcuts import render,redirect
from app.models import Student
from app.forms import StudentForm,UserRegisterForm
from django.core.mail import send_mail
from cryptography.fernet import Fernet
key=Fernet.generate_key()
fernet=Fernet(key)

def add_data(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        p_form = StudentForm(request.POST)
        if u_form.is_valid() and p_form.is_valid() :
            email=request.POST.get('email')
            user=u_form.save()
            #encrypted
            user.email=fernet.encrypt(email.encode())
            user.set_password(user.password)
            user.save()
            em=user.email
            print('email_encrypted',em)
            contact=request.POST.get('contact')
            stu=p_form.save(commit=False)
            stu.user=user
            stu.contact=fernet.encrypt(contact.encode())
           
            stu.save()
            ph=stu.contact
            print('phone_encrypted',ph)
            #decrypted
            phone=fernet.decrypt(stu.contact).decode()
            print('phone_no_decrypted',phone)
            a=fernet.decrypt(user.email).decode()
            print('email_decrypted',a)
            subjects="thanks for registration"
            message='hey.....'+str(a)+',this your email id....'+str(phone)+'.......this is your phone number'
            # a=fernet.decrypt(user.email).decode()
            print('###############',a)
            
            to=a
            print("------------",to)
            send_mail(
                subjects,
                message,
                'swamypotharaveni@gmail.com',
                [to],
                fail_silently=False,
)
            
            return redirect('list')
    else:
        u_form = UserRegisterForm()
        p_form = StudentForm()

    context = {

        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'home.html', context)



        
        
    
        
   

            
            
        
    

