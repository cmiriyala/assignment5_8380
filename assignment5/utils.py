from .models import Student, Teacher, Parent, Login_role
from django.core.mail import send_mail
from django.contrib.auth.models import User

from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)

from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)

def add_student(data):
    name = data['name']
    password = data['password']
    address = data['address']
    city = data['city']
    state = data['state']
    zipcode = data['zipcode']
    email = data['email']
    cell_phone = data['cell_phone']
    class_grade = 'NA'
    student = Student.objects.create(name=name,address=address,city=city,state=state,zipcode=zipcode,email=email,cell_phone=cell_phone, class_grade=class_grade)
    student.save()
    print('student added')
    add_login_data(email,name,data['role'],password)


def add_teacher(data):
    name = data['name']
    password = data['password']
    address = data['address']
    city = data['city']
    state = data['state']
    zipcode = data['zipcode']
    email = data['email']
    cell_phone = data['cell_phone']
    teacher = Teacher.objects.create(name=name,address=address,city=city,state=state,zipcode=zipcode,email=email,cell_phone=cell_phone)
    teacher.save()
    print('teacher added')
    add_login_data(email,name,data['role'],password)

def add_parent(data):
    name = data['name']
    password = data['password']
    address = data['address']
    city = data['city']
    state = data['state']
    zipcode = data['zipcode']
    email = data['email']
    cell_phone = data['cell_phone']
    parent = Parent.objects.create(name=name, address=address, city=city, state=state, zipcode=zipcode, email=email,cell_phone=cell_phone)
    parent.save()
    print('parent added')
    add_login_data(email,name,data['role'],password)

def add_login_data(email,name,role,password):
    new_login = Login_role.objects.create(user_email=email,prefered_name=name,level=role)
    new_login.save()
    UserModel = get_user_model()
    new_user = UserModel.objects.create(username=email,password=make_password(password), email=email)
    new_user.save()
    print ('Login details added')

#def login_data(data):
 #   print ('Login success')
  #  userid=data['Username']
   # print (userid)

#def sendmailthis(data):
 #   mailtextdata = data['mailtext']
  #  recievers = []
   # for studnets in Student.objects.all():
 #       recievers.append(studnets.email)
#
  #  print(mailtextdata)
   # print(recievers)
    #send_mail(
     #   'Class Announcement',
      #  mailtextdata,
       # 'schoolomaha@schools.com',
        #recievers
    #)