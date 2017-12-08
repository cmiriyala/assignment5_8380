"""A5S0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.auth import views
from assignment5.views import *


urlpatterns = [
url(r'^$',include('assignment5.urls')),
    url(r'^admin/', admin.site.urls),
#url(r'^event/',include('assignment5.urls')),
url(r'^event/$',event),
url(r'^event/parent/$',eventparent),
url(r'^event/teacher/$',eventteacher),
url(r'^event/student/$',eventstudent),
url(r'^about/$',about),
url(r'^about/parent/$',aboutparent),
url(r'^about/teacher/$',aboutteacher),
url(r'^about/student/$',aboutstudent),
url(r'^contact/$',contact),
url(r'^contact/parent/$',contactparent),
url(r'^contact/teacher/$',contactteacher),
url(r'^contact/student/$',contactstudent),
url(r'^register/$',register),
url(r'^gallery/$',insta),
url(r'^gallery/parent/$',instaparent),
url(r'^gallery/teacher/$',instateacher),
url(r'^gallery/student/$',instastudent),
#url(r'^login/$',"assignment5.views.login"), url(r'^accounts/login/$', views.login, name='login'),
url(r'^accounts/',include('assignment5.urls') ),
url(r'^student/home$',studentview),
url(r'^student/profile/view/$',stuprofileview,name='studentprofile'),
url(r'^student/profile/edit/$',stuprofileedit,name='editstuprofile'),
url(r'^student/profile/$',sprofile,name='sprofile'),
url(r'^parent/profile/view/$',parprofileview,name='parentprofile'),
url(r'^parent/profile/edit/$',parprofileedit,name='editparprofile'),
url(r'^parent/profile/$',pprofile,name='pprofile'),
url(r'^teacher/profile/view/$',teaprofileview,name='teacherprofile'),
url(r'^teacher/profile/edit/$',teaprofileedit,name='editteaprofile'),
url(r'^teacher/profile/$',tprofile,name='tprofile'),
url(r'^student/course/(?P<pk>\d+)/view/$',stucourseview,name='studentcourse'),
url(r'^teacher/course/(?P<pk>\d+)/view/$',teachercourseview,name='teachercourse'),
url(r'^student/course/(?P<pk>\d+)/syllabus/$',stucsyllabusview,name='studentcsyllabus'),
url(r'^student/course/(?P<pk>\d+)/schedule/$',stucscheduleview,name='studentcschedule'),
url(r'^teacher/course/(?P<pk>\d+)/syllabus/$',teacsyllabusview,name='teachercsyllabus'),
url(r'^teacher/course/(?P<pk>\d+)/schedule/$',teacscheduleview,name='teachercschedule'),
url(r'^student/course/(?P<pk>\d+)/attendance/$',stucattendanceview,name='studentcattendance'),
url(r'^student/course/(?P<pk>\d+)/exams/$',stucexamsview,name='studentcexams'),
url(r'^student/course/(?P<pk>\d+)/grades/$',stucgradesview,name='studentcmarks'),
url(r'^teacher/course/(?P<pk>\d+)/examlist/$',teacexamlistview,name='teachercexamlist'),
url(r'^teacher/course/(?P<pk>\d+)/attendance/$',teacattendanceview,name='updateattendance'),
url(r'^teacher/course/markattendance/$',attendanceview,name='attendance'),
url(r'^teacher/course/updateattendance/present/$',teacmarkpview,name='present'),
url(r'^teacher/course/updateattendance/absent/$',teacmarkaview,name='absent'),
url(r'^teacher/course/markattendance/alreadyexists/$',existsview,name='exists'),
url(r'^teacher/upate/absent$',absmsg,name='absentmsg'),
url(r'^teacher/course/(?P<pk>\d+)/updatemarks/$',teacupdatemarksview,name='teacupdatemarks'),
url(r'^teacher/course/postmarks/$',teacpostmarksview,name='postmarks'),
url(r'^teacher/home$',teacherview,name='teacherview'),
url(r'^parent/home$',parentview,name='parent'),
url(r'^teacher/(?P<pk>\d+)/announce$',announce,name='announce'),
url(r'^parent/home/(?P<pk>\d+)/childcrecords/$',childcrecordsview,name='childcrecords'),
url(r'^parent/home/(?P<pk>\d+)/childinvoice/$',childinvoiceview,name='childinvoice'),
url(r'^parent/home/(?P<pk>\d+)/payinvoice/$',payinvoice,name='childinvoicepay'),
url(r'^parent/home/(?P<pk>\d+)/childcrecords/view/$',childcourseview,name='childcourse'),
url(r'^parent/home/(?P<pk>\d+)/childcrecords/syllabus/$',childcsyllabusview,name='childcsyllabus'),
url(r'^parent/home/(?P<pk>\d+)/childcrecords/schedule/$',childcscheduleview,name='childcschedule'),
url(r'^parent/home/(?P<pk>\d+)/attendance/$',childcattendanceview,name='childcattendance'),
url(r'^parent/home/(?P<pk>\d+)/exams/$',childcexamsview,name='childcexams'),
url(r'^parent/home/(?P<pk>\d+)/grades/$',childcgradesview,name='childcmarks'),
url(r'^parent/phonever$',verobcid,name='phverify'),
url(r'^parent/pleaseverify$',pleasever,name='pleasever'),
url(r'^teacher/course/(?P<pk>\d+)/exams/$',teacexamsview,name='teachercexams'),
url(r'^teacher/slack/$',slack1,name='slack1'),
url(r'^teacher/slack/viewmsg$',slackviewmessage,name='slackviewmessage'),
url(r'^teacher/postupdate$',postupdate,name='postupdate'),
url(r'^student/slack/viewmsg$',slackviewmessagestu,name='slackviewmessagestu'),
url(r'^parent/verify/error$',phvererror,name='phvererror'),
url(r'^parent/event/rsvp$',rsvp,name='rsvp'),
url(r'^parent/event/rsvp/save$',addrsvp,name='addrsvp'),




]
