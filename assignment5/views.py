from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .forms import registrationForm, loginForm, emailannouncement
from .utils import add_student, add_parent, add_teacher
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from twilio.rest import Client
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib import messages
import kickbox
import requests
from urllib.request import urlopen
import simplejson as json
from django.template.loader import get_template
from django.template import RequestContext
from django.shortcuts import render_to_response
from slackclient import SlackClient
import os
import slackweb
from slacker import Slacker
from django.views.decorators.csrf import csrf_protect

img = list()
slackmsg = list()
slack = Slacker('')
slack2 = slackweb.Slack(url="")


# Create your views here.
def home(request):
	return render(request, "home.html")


def event(request):
	data = Event.objects.all()
	stu = {
		"events": data
	}
	print(stu)
	return render(request, "event.html", stu)

@login_required
def eventparent(request):
	data = Event.objects.all()
	stu = {
		"events": data
	}
	print(stu)
	return render(request, "event_parent.html", stu)

@login_required
def eventstudent(request):
	data = Event.objects.all()
	stu = {
		"events": data
	}
	print(stu)
	return render(request, "event_student.html", stu)
	
@login_required
def eventteacher(request):
	data = Event.objects.all()
	stu = {
		"events": data
	}
	print(stu)
	return render(request, "event_teacher.html", stu)
	
def contact(request):
	return render(request, "contactus.html")

@login_required	
def contactteacher(request):
	return render(request, "contactus_teacher.html")
	
@login_required	
def contactparent(request):
	return render(request, "contactus_parent.html")
	
@login_required	
def contactstudent(request):
	return render(request, "contactus_student.html")


def about(request):
	return render(request, "about.html")
	
@login_required	
def aboutteacher(request):
	return render(request, "about_teacher.html")
	
@login_required	
def aboutparent(request):
	return render(request, "about_parent.html")
	
@login_required	
def aboutstudent(request):
	return render(request, "about_student.html")


def register(request):
	if request.method == "POST":
		form = registrationForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			if User.objects.filter(email=form.cleaned_data['email']).exists():
				print("user exist")
				messages.error(request, 'User alredy registered. Try Forgot password')
			elif form.cleaned_data['role'] == 'Student':
				add_student(data)
			elif form.cleaned_data['role'] == 'Teacher':
				add_teacher(data)
			elif form.cleaned_data['role'] == 'Parent':
				add_parent(data)
			else:
				print ('error')
			return redirect('/accounts/login')
	else:
		form = registrationForm()
	return render(request, "register.html", {'form': form})


@login_required
def studentview(request):
	if request.user.is_authenticated():
		email = request.user.email
		student = Student.objects.get(email=email)
		studentid = student.email
		data = Grade.objects.filter(student_id=studentid)
		stu = {
			"grades": data,
			"student": student
		}
	return render(request, "student_home.html", stu)


@login_required
def stuprofileview(request):
	if request.user.is_authenticated():
		email = request.user.email
		student = Student.objects.get(email=email)
		stu = {
			"student": student
		}
	return render(request, "student_profile.html", stu)


@login_required
def stuprofileedit(request):
	if request.user.is_authenticated():
		email = request.user.email
		student = Student.objects.get(email=email)
		stu = {
			"student": student
		}
	return render(request, "student_profileedit.html", stu)


@login_required
def parprofileview(request):
	if request.user.is_authenticated():
		email = request.user.email
		parent = Parent.objects.get(email=email)
		stu = {
			"parent": parent
		}
	return render(request, "parent_profile.html", stu)


@login_required
def parprofileedit(request):
	if request.user.is_authenticated():
		email = request.user.email
		parent = Parent.objects.get(email=email)
		stu = {
			"parent": parent
		}
	return render(request, "parent_profileedit.html", stu)


@login_required
def teaprofileview(request):
	if request.user.is_authenticated():
		email = request.user.email
		teacher = Teacher.objects.get(email=email)
		stu = {
			"teacher": teacher
		}
	return render(request, "teacher_profile.html", stu)


@login_required
def teaprofileedit(request):
	if request.user.is_authenticated():
		email = request.user.email
		teacher = Teacher.objects.get(email=email)
		stu = {
			"teacher": teacher
		}
	return render(request, "teacher_profileedit.html", stu)


@login_required
def sprofile(request):
	try:
		if request.user.is_authenticated():
			email = request.user.email
			name = request.POST.get('name', None)
			address = request.POST.get('address', None)
			city = request.POST.get('city', None)
			state = request.POST.get('state', None)
			zipcode = request.POST.get('zipcode', None)
			phone = request.POST.get('phone', None)
			classgrade = request.POST.get('classgrade', None)
			student = Student.objects.get(email=email)
			student.name = name
			student.address = address
			student.city = city
			student.state = state
			student.zipcode = zipcode
			student.email = email
			student.cell_phone = phone
			student.class_grade = classgrade
			student.created_date = timezone.now()
			student.updated_date = timezone.now()
			student.save()
			stu = {
				"student": student
			}
	except Exception as e:
		print ("Please verify the details")
		print (e)
	return render(request, "student_profile.html", stu)


@login_required
def pprofile(request):
	try:
		if request.user.is_authenticated():
			email = request.user.email
			name = request.POST.get('name', None)
			address = request.POST.get('address', None)
			city = request.POST.get('city', None)
			state = request.POST.get('state', None)
			zipcode = request.POST.get('zipcode', None)
			phone = request.POST.get('phone', None)
			parent = Parent.objects.get(email=email)
			parent.name = name
			parent.address = address
			parent.city = city
			parent.state = state
			parent.zipcode = zipcode
			parent.email = email
			parent.cell_phone = phone
			parent.created_date = timezone.now()
			parent.updated_date = timezone.now()
			parent.save()
			stu = {
				"parent": parent
			}
	except Exception as e:
		print ("Please verify the details")
		print (e)
	return render(request, "parent_profile.html", stu)


@login_required
def tprofile(request):
	try:
		if request.user.is_authenticated():
			email = request.user.email
			name = request.POST.get('name', None)
			address = request.POST.get('address', None)
			city = request.POST.get('city', None)
			state = request.POST.get('state', None)
			zipcode = request.POST.get('zipcode', None)
			phone = request.POST.get('phone', None)
			teacher = Teacher.objects.get(email=email)
			teacher.name = name
			teacher.address = address
			teacher.city = city
			teacher.state = state
			teacher.zipcode = zipcode
			teacher.email = email
			teacher.cell_phone = phone
			teacher.created_date = timezone.now()
			teacher.updated_date = timezone.now()
			teacher.save()
			stu = {
				"teacher": teacher
			}
	except Exception as e:
		print ("Please verify the details")
		print (e)
	return render(request, "teacher_profile.html", stu)


@login_required
def stucourseview(request, pk):
	grade = get_object_or_404(Grade, pk=pk)
	course = Course.objects.get(id=grade.course_id_id)
	if request.user.is_authenticated():
		email = request.user.email
		student = Student.objects.get(email=email)
		stu = {
			"course": course,
			"student": student
		}
	return render(request, "student_course.html", stu)


@login_required
def stucsyllabusview(request, pk):
	course = get_object_or_404(Course, pk=pk)
	if request.user.is_authenticated():
		email = request.user.email
		student = Student.objects.get(email=email)
		stu = {
			"course": course,
			"student": student
		}
	return render(request, "student_coursesyllabus.html", stu)


@login_required
def stucscheduleview(request, pk):
	course = get_object_or_404(Course, pk=pk)
	if request.user.is_authenticated():
		email = request.user.email
		student = Student.objects.get(email=email)
		stu = {
			"course": course,
			"student": student
		}
	return render(request, "student_courseschedule.html", stu)


@login_required
def stucattendanceview(request, pk):
	course = get_object_or_404(Course, pk=pk)
	if request.user.is_authenticated():
		email = request.user.email
		student = Student.objects.get(email=email)
		data = Grade.objects.filter(course_id=course.id).get(student_id=email)
		print(data)
		stu = {
			"course": course,
			"student": student,
			"grade": data
		}
	return render(request, "student_courseattendance.html", stu)


@login_required
def stucexamsview(request, pk):
	course = get_object_or_404(Course, pk=pk)
	if request.user.is_authenticated():
		email = request.user.email
		student = Student.objects.get(email=email)
		data = Exam.objects.filter(course_id=course.id)
		stu = {
			"course": course,
			"student": student,
			"exams": data
		}
	return render(request, "student_courseexams.html", stu)


@login_required
def stucgradesview(request, pk):
	course = get_object_or_404(Course, pk=pk)
	if request.user.is_authenticated():
		email = request.user.email
		student = Student.objects.get(email=email)
		data = Marks.objects.filter(course_id=course.id).filter(student_id=student.email)
		print(data)
		stu = {
			"course": course,
			"student": student,
			"marks": data
		}
	return render(request, "student_coursemarks.html", stu)


@login_required
def teacherview(request):
	if request.user.is_authenticated():
		email = request.user.email
		teacher = Teacher.objects.get(email=email)
		teacherid = teacher.email
		data = Course.objects.filter(teacher_id=teacherid)
		stu = {
			"courses": data,
			"teacher": teacher
		}
	return render(request, "teacher_home.html", stu)


@login_required
def teachercourseview(request, pk):
	course = get_object_or_404(Course, pk=pk)
	if request.user.is_authenticated():
		email = request.user.email
		teacher = Teacher.objects.get(email=email)
		stu = {
			"course": course,
			"teacher": teacher
		}
	return render(request, "teacher_course.html", stu)


@login_required
def teacsyllabusview(request, pk):
	course = get_object_or_404(Course, pk=pk)
	if request.user.is_authenticated():
		stu = {
			"course": course
		}
	return render(request, "teacher_coursesyllabus.html", stu)


@login_required
def teacscheduleview(request, pk):
	course = get_object_or_404(Course, pk=pk)
	if request.user.is_authenticated():
		stu = {
			"course": course
		}
	return render(request, "teacher_courseschedule.html", stu)


@login_required
def teacexamlistview(request, pk):
	course = get_object_or_404(Course, pk=pk)
	if request.user.is_authenticated():
		data = Exam.objects.filter(course_id=course.id)
		stu = {
			"course": course,
			"exams": data
		}
	return render(request, "teacher_courseexamlist.html", stu)


@login_required
def teacattendanceview(request, pk):
	course = get_object_or_404(Course, pk=pk)
	courseclass = CourseClass.objects.filter(course_id=course.id).values_list('class_name', flat=True).distinct()
	print(courseclass)
	if request.user.is_authenticated():
		stu = {
			"course": course,
			"courseclass": courseclass
		}
	return render(request, "teacher_courseclass.html", stu)


@login_required
def attendanceview(request):
	addcid = request.POST.get('addcid', None)
	classname = request.POST.get('classname', None)
	course = Course.objects.get(id=addcid)
	data = Grade.objects.filter(course_id=addcid)
	function = request.POST.get('dothis', None)
	coursec = CourseClass.objects.filter(course_id=addcid).filter(class_name=classname)
	print(function)
	if function == "view":
		courseclassdata = CourseClass.objects.filter(course_id=addcid).filter(class_name=classname)
		stu = {
			"courseclassobj": courseclassdata,
			"listgrade": data,
			"course": course
		}
		return render(request, "teacher_courseattendance.html", stu)
	else:
		if coursec:
			return redirect('/teacher/course/markattendance/alreadyexists/')
		else:
			for student in data:
				courseclass = CourseClass()
				courseclass.course_id_id = addcid
				courseclass.student_id_id = student.student_id_id
				courseclass.class_name = classname
				courseclass.status = ""
				courseclass.save()
			courseclassdata = CourseClass.objects.filter(course_id=addcid).filter(class_name=classname)
			stu = {
				"courseclassobj": courseclassdata,
				"listgrade": data,
				"course": course
			}
			return render(request, "teacher_courseattendance.html", stu)


@login_required
def existsview(request):
	return render(request, "teacher_alreadyexists.html")


@login_required
def teacmarkpview(request):
	if request.method == "POST":
		cid = request.POST.get('courseid', None)
		studid = request.POST.get('studid', None)
		classname = request.POST.get('class', None)
		grade = Grade.objects.filter(student_id=studid).get(course_id=cid)
		grade.attandance = grade.attandance + 1
		grade.save()
		course = Course.objects.get(id=cid)
		data = Grade.objects.filter(course_id=course.id)
		studentupdate = CourseClass.objects.filter(course_id=cid).filter(class_name=classname).get(student_id=studid)
		studentupdate.status = 'P'
		studentupdate.save()
		courseclassdata = CourseClass.objects.filter(course_id=cid).filter(class_name=classname)
		stu = {
			"course": course,
			"listgrade": data,
			"courseclassobj": courseclassdata,
		}
	return render(request, "teacher_courseattendance.html", stu)


@login_required
def absmsg(request):
	account_sid = ""
	# Your Auth Token from twilio.com/console
	auth_token = ""
	cid = request.POST.get('courseid', None)
	studid = request.POST.get('studid', None)
	classname = request.POST.get('class', None)
	stuparent = StudentParent.objects.get(student_id=studid)
	print(stuparent)
	parent = Parent.objects.get(email=stuparent.parent_id_id)
	phnnum = parent.cell_phone
	print(phnnum)
	client = Client(account_sid, auth_token)
	message = client.messages.create(
		to=phnnum,
		from_="+14022819608",
		body="Hello your son/daughter is absent today // test sms api")
	print(message.sid)
	request.session['studid'] = studid
	request.session['cid'] = cid
	request.session['classname'] = classname
	return HttpResponseRedirect('/teacher/course/updateattendance/absent')


@login_required
def teacmarkaview(request):
	studid = request.session.get('studid')
	del request.session['studid']
	cid = request.session.get('cid')
	del request.session['cid']
	classname = request.session.get('classname')
	del request.session['classname']
	print(studid)
	print(cid)
	print(classname)
	grade = Grade.objects.filter(student_id=studid).get(course_id=cid)
	grade.attandance = grade.attandance - 1
	grade.save()
	course = Course.objects.get(id=cid)
	listgrade = Grade.objects.filter(course_id=course.id)
	studentupdate = CourseClass.objects.filter(course_id=cid).filter(class_name=classname).get(student_id=studid)
	studentupdate.status = 'A'
	studentupdate.save()
	courseclassobj = CourseClass.objects.filter(course_id=cid).filter(class_name=classname)
	return render(request, "teacher_courseattendance.html", locals())


@login_required
def announce(request, pk):
	try:
		if request.method == "POST":
			course = get_object_or_404(Course, pk=pk)
			grades = Grade.objects.filter(course_id_id=course.id)
			mtext = request.POST.get('mailtext', None)
			recievers = []
			for grade in grades:
				recievers.append(grade.student_id_id)
				print(recievers)
			print(mtext)
			send_mail(
				'Class Announcement',
				mtext,
				'schoolomaha@schools.com',
				recievers
			)
			return redirect('/teacher/home')
		else:
			form = emailannouncement()
	except Exception as e:
		print ("Please verify the details")
		print (e)
	return render(request, "Announce.html", {'form': form})


@login_required
def parentview(request):
	if request.user.is_authenticated():
		email = request.user.email
		parent = Parent.objects.get(email=email)
		parentid = parent.email
		data = StudentParent.objects.filter(parent_id=parentid)
		print(data)
		stu = {
			"children": data,
			"parent": parent
		}
	return render(request, "parent_home.html", stu)


@login_required
def childcrecordsview(request, pk):
	studentparent = get_object_or_404(StudentParent, pk=pk)
	if request.user.is_authenticated():
		email = studentparent.student_id_id
		data = Grade.objects.filter(student_id=email)
		print(data)
		stu = {
			"grades": data
		}
	return render(request, "parent_childrecord.html", stu)


@login_required
def childcourseview(request, pk):
	grade = get_object_or_404(Grade, pk=pk)
	course = Course.objects.get(id=grade.course_id_id)
	if request.user.is_authenticated():
		stu = {
			"course": course,
			"grade": grade
		}
	return render(request, "child_course.html", stu)


@login_required
def childinvoiceview(request, pk):
	studentparent = get_object_or_404(StudentParent, pk=pk)
	invoice = Invoice.objects.filter(student_id=studentparent.student_id_id)
	print(invoice)
	if request.user.is_authenticated():
		stu = {
			"invoices": invoice
		}
	return render(request, "child_invoice.html", stu)


@login_required
def payinvoice(request, pk):
	invoice = get_object_or_404(Invoice, pk=pk)
	print(invoice)
	if request.user.is_authenticated():
		stu = {
			"invoice": invoice
		}
	return render(request, "pay_invoice.html", stu)


@login_required
def childcsyllabusview(request, pk):
	grade = get_object_or_404(Grade, pk=pk)
	course = Course.objects.get(id=grade.course_id_id)
	if request.user.is_authenticated():
		stu = {
			"course": course,
			"grade": grade
		}
	return render(request, "child_coursesyllabus.html", stu)


@login_required
def childcscheduleview(request, pk):
	grade = get_object_or_404(Grade, pk=pk)
	course = Course.objects.get(id=grade.course_id_id)
	if request.user.is_authenticated():
		stu = {
			"course": course,
			"grade": grade
		}
	return render(request, "child_courseschedule.html", stu)


@login_required
def childcattendanceview(request, pk):
	grade = get_object_or_404(Grade, pk=pk)
	course = Course.objects.get(id=grade.course_id_id)
	if request.user.is_authenticated():
		stu = {
			"course": course,
			"grade": grade
		}
	return render(request, "child_courseattendance.html", stu)


@login_required
def childcexamsview(request, pk):
	grade = get_object_or_404(Grade, pk=pk)
	course = Course.objects.get(id=grade.course_id_id)
	if request.user.is_authenticated():
		data = Exam.objects.filter(course_id=course.id)
		stu = {
			"course": course,
			"grade": grade,
			"exams": data
		}
	return render(request, "child_courseexams.html", stu)


@login_required
def childcgradesview(request, pk):
	grade = get_object_or_404(Grade, pk=pk)
	course = Course.objects.get(id=grade.course_id_id)
	if request.user.is_authenticated():
		data = Marks.objects.filter(course_id=course.id).filter(student_id=grade.student_id_id)
		print(data)
		stu = {
			"course": course,
			"grade": grade,
			"marks": data
		}
	return render(request, "child_coursemarks.html", stu)


def verobcid(request):
	try:
		parent = request.POST.get('parentid', None)
		parentph = Parent.objects.get(email=parent)
		# parent = get_object_or_404(Parent, pk=pk)
		phonenum = parentph.cell_phone
		parentname = parentph.name
		print (phonenum)
		print (parentname)
		account_sid = ""
		auth_token = ""
		client = Client(account_sid, auth_token)

		validation_request = client.validation_requests \
			.create(phonenum,
					friendly_name=parentname)
		verfcode = validation_request.validation_code
		print(verfcode)
		request.session['verfcod'] = verfcode
	except Exception as e:
		print ("Phone number already verified")
		print (e)
		return HttpResponseRedirect('/parent/verify/error')
	# url = reverse('pleasever', kwargs={'verfcode': verfcode})
	return HttpResponseRedirect('/parent/pleaseverify')
def phvererror(request):
	return render(request, "pherror.html")
def pleasever(request):
	if request.session.has_key('verfcod'):
		verfcod = request.session.get('verfcod')
		del request.session['verfcod']
	return render(request, "pleasever.html", locals())


# return render(request, "pleasever.html", verfcode)
@login_required
def teacupdatemarksview(request, pk):
	print(request)
	if request.user.is_authenticated():
		exam = get_object_or_404(Exam, pk=pk)
		courseid = exam.course_id
		grade = Grade.objects.filter(course_id=courseid)
		print(grade)
		stu = {
			"students": grade,
			"exam": exam,
		}
	return render(request, "teacher_updatemarks.html", stu)


@login_required
def teacexamsview(request, pk):
	course = get_object_or_404(Course, pk=pk)
	if request.user.is_authenticated():
		data = Exam.objects.filter(course_id=course.id)
		stu = {
			"course": course,
			"exams": data
		}
	return render(request, "teacher_courseexams.html", stu)


@login_required
def teacpostmarksview(request):
	try:
		mark = request.POST.get('marks', None)
		feedback = request.POST.get('feedback', None)
		studentid = request.POST.get('studentid1', None)
		courseid = request.POST.get('courseid1', None)
		examid = request.POST.get('examid', None)
		print(mark)
		print(feedback)
		print(studentid)
		print(courseid)
		print(examid)
		marks = Marks()
		marks.marks = mark
		marks.feedback = feedback
		marks.student_id_id = studentid
		marks.course_id_id = courseid
		marks.exam_id_id = examid
		marks.save()
		exam = Exam.objects.get(id=examid)
		grade = Grade.objects.filter(course_id=courseid)
		print(grade)
		stu = {
			"students": grade,
			"exam": exam,
		}
	except Exception as e:
		print ("Please verify the details")
		print (e)
	return render(request, "teacher_updatemarks.html", stu)


def insta(request):
	photos = "https://api.instagram.com/v1/users/self/media/recent/?access_token="
	print(photos)
	response = urlopen(photos)
	string = response.read().decode('utf-8')
	json_obj = json.loads(string)
	img = []
	for i in range(0, 11):
		img.append(json_obj['data'][i]['images']['low_resolution']['url'])
	for j in range(0, 11):
		print(img[j])
	stu = {
		"img1": img[0],
		"img2": img[1],
		"img3": img[2],
		"img4": img[3],
		"img5": img[4],
		"img6": img[5],
		"img7": img[6],
		"img8": img[7],
		"img9": img[8],
		"img10": img[9],
		"img11": img[10]
	}
	return render_to_response('gallery.html', stu)
@login_required	
def instateacher(request):
	photos = "https://api.instagram.com/v1/users/self/media/recent/?access_token="
	print(photos)
	response = urlopen(photos)
	string = response.read().decode('utf-8')
	json_obj = json.loads(string)
	img = []
	for i in range(0, 11):
		img.append(json_obj['data'][i]['images']['low_resolution']['url'])
	for j in range(0, 11):
		print(img[j])
	stu = {
		"img1": img[0],
		"img2": img[1],
		"img3": img[2],
		"img4": img[3],
		"img5": img[4],
		"img6": img[5],
		"img7": img[6],
		"img8": img[7],
		"img9": img[8],
		"img10": img[9],
		"img11": img[10]
	}
	return render_to_response('gallery_teacher.html', stu)
@login_required	
def instaparent(request):
	photos = "https://api.instagram.com/v1/users/self/media/recent/?access_token="
	print(photos)
	response = urlopen(photos)
	string = response.read().decode('utf-8')
	json_obj = json.loads(string)
	img = []
	for i in range(0, 11):
		img.append(json_obj['data'][i]['images']['low_resolution']['url'])
	for j in range(0, 11):
		print(img[j])
	stu = {
		"img1": img[0],
		"img2": img[1],
		"img3": img[2],
		"img4": img[3],
		"img5": img[4],
		"img6": img[5],
		"img7": img[6],
		"img8": img[7],
		"img9": img[8],
		"img10": img[9],
		"img11": img[10]
	}
	return render_to_response('gallery_parent.html', stu)
@login_required	
def instastudent(request):
	photos = "https://api.instagram.com/v1/users/self/media/recent/?access_token="
	print(photos)
	response = urlopen(photos)
	string = response.read().decode('utf-8')
	json_obj = json.loads(string)
	img = []
	for i in range(0, 11):
		img.append(json_obj['data'][i]['images']['low_resolution']['url'])
	for j in range(0, 11):
		print(img[j])
	stu = {
		"img1": img[0],
		"img2": img[1],
		"img3": img[2],
		"img4": img[3],
		"img5": img[4],
		"img6": img[5],
		"img7": img[6],
		"img8": img[7],
		"img9": img[8],
		"img10": img[9],
		"img11": img[10]
	}
	return render_to_response('gallery_student.html', stu)


@csrf_protect
@login_required
def slack1(request):
	updatepost = request.POST.get('postupdate', None)
	slack2.notify(text=updatepost, channel="#team4-8380", username="hunterB9", icon_emoji=":sushi:")
	return HttpResponseRedirect('/teacher/slack/viewmsg')


@csrf_protect
@login_required
def slackviewmessage(request):
	url = "https://slack.com/api/channels.history?token=&channel="
	response = urlopen(url)
	string = response.read().decode('utf-8')
	json_obj = json.loads(string)
	# print(json_obj)
	print(json_obj['messages'][0]['text'])
	slackmsg = []
	for i in range(0, 7):
		slackmsg.append(json_obj['messages'][i]['text'])
	for j in range(0, 7):
		print (slackmsg[j])
	stu = {
		"slackmsg1": slackmsg[0],
		"slackmsg2": slackmsg[1],
		"slackmsg3": slackmsg[2],
		"slackmsg4": slackmsg[3],
		"slackmsg5": slackmsg[4],
	}

	return render(request, 'slack.html', stu)


@login_required
def slackviewmessagestu(request):
	url = "https://slack.com/api/channels.history?token=&channel="
	response = urlopen(url)
	string = response.read().decode('utf-8')
	json_obj = json.loads(string)
	# print(json_obj)
	print(json_obj['messages'][0]['text'])
	slackmsg = []
	for i in range(0, 7):
		slackmsg.append(json_obj['messages'][i]['text'])
	for j in range(0, 7):
		print (slackmsg[j])
	stu = {
		"slackmsg1": slackmsg[0],
		"slackmsg2": slackmsg[1],
		"slackmsg3": slackmsg[2],
		"slackmsg4": slackmsg[3],
		"slackmsg5": slackmsg[4],
	}

	return render(request, 'slack_stu.html', stu)


@login_required
def postupdate(request):
	return render(request, "postupdate.html")
def rsvp(request):
	if request.user.is_authenticated():
		evid=request.POST.get('eveid', None)
		evname=request.POST.get('evename', None)
		email = request.user.email
		parent = Parent.objects.get(email=email)
		print(evid)
		stu = {
			"parent": parent,
			"eventid":evid,
			"ename":evname
		}
		return render(request, "postrsvp.html",stu)
def addrsvp(request):
	evid = request.POST.get('eid', None)
	pid=request.POST.get('address', None)
	print(evid)
	print(pid)
	rsvp=Event_registration()
	rsvp.parent_id_id=pid
	rsvp.event_id_id=evid
	rsvp.save()
	return redirect('/parent/home')
def handler404(request):
    response = render_to_response('404.html', {},
                              context_instance=RequestContext(request))
    response.status_code = 404
    return response