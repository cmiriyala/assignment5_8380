from django.db import models
from django.utils import timezone

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	zipcode = models.CharField(max_length=10)
	email = models.EmailField(max_length=200,primary_key=True)
	cell_phone = models.CharField(max_length=12)
	class_grade = models.CharField(max_length=10)
	created_date = models.DateTimeField(
		default=timezone.now)
	updated_date = models.DateTimeField(auto_now_add=True)

	def created(self):
		self.created_date = timezone.now()
		self.save()

	def updated(self):
		self.updated_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name

class Parent(models.Model):
		name = models.CharField(max_length=50)
		address = models.CharField(max_length=200)
		city = models.CharField(max_length=50)
		state = models.CharField(max_length=50)
		zipcode = models.CharField(max_length=10)
		email = models.EmailField(max_length=200,primary_key=True)
		cell_phone = models.CharField(max_length=50)
		created_date = models.DateTimeField(
			default=timezone.now)
		updated_date = models.DateTimeField(auto_now_add=True)

		def created(self):
			self.created_date = timezone.now()
			self.save()

		def updated(self):
			self.updated_date = timezone.now()
			self.save()

		def __str__(self):
			return self.name

class StudentParent(models.Model):
	student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
	parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE)
	created_date = models.DateTimeField(
		default=timezone.now)
	updated_date = models.DateTimeField(auto_now_add=True)

	def created(self):
		self.created_date = timezone.now()
		self.save()

	def updated(self):
		self.updated_date = timezone.now()
		self.save()

	#def __str__(self):
	 #   return self.student_id


class Teacher(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	zipcode = models.CharField(max_length=10)
	email = models.EmailField(max_length=200,primary_key=True)
	cell_phone = models.CharField(max_length=50)
	created_date = models.DateTimeField(
		default=timezone.now)
	updated_date = models.DateTimeField(auto_now_add=True)

	def created(self):
		self.created_date = timezone.now()
		self.save()

	def updated(self):
		self.updated_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name

class Login_role(models.Model):
	user_email = models.CharField(max_length=50,primary_key=True)
	prefered_name = models.CharField(max_length=50)
	level = models.CharField(max_length=50)
	created_date = models.DateTimeField(
		default=timezone.now)
	updated_date = models.DateTimeField(auto_now_add=True)

	def created(self):
		self.created_date = timezone.now()
		self.save()

	def updated(self):
		self.updated_date = timezone.now()
		self.save()
	def __str__(self):
		return self.user_email
class Course(models.Model):
	course_name = models.CharField(max_length=50)
	description = models.TextField(max_length=250)
	syllabus = models.TextField(max_length=800)
	schedule = models.TextField(max_length=200)
	teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	announcement = models.TextField(max_length=400)
	created_date = models.DateTimeField(
		default=timezone.now)
	updated_date = models.DateTimeField(auto_now_add=True)

	def created(self):
		self.created_date = timezone.now()
		self.save()

	def updated(self):
		self.updated_date = timezone.now()
		self.save()
	def __str__(self):
		return self.course_name
		

class CourseClass(models.Model):
	student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
	course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
	class_name = models.CharField(max_length=50)
	status= models.CharField(max_length=1)
	created_date = models.DateTimeField(
		default=timezone.now)
	updated_date = models.DateTimeField(auto_now_add=True)

	def created(self):
		self.created_date = timezone.now()
		self.save()

	def updated(self):
		self.updated_date = timezone.now()
		self.save()

	#def __str__(self):
	 #   return self.student_id
	 
class Exam(models.Model):
	course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
	exam_name = models.TextField(max_length=50)
	exam_details = models.TextField(max_length=500)
	created_date = models.DateTimeField(
		default=timezone.now)
	updated_date = models.DateTimeField(auto_now_add=True)

	def created(self):
		self.created_date = timezone.now()
		self.save()

	def updated(self):
		self.updated_date = timezone.now()
		self.save()

	def __str__(self):
		return self.exam_details

class Marks(models.Model):
		student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
		course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
		marks = models.IntegerField()
		feedback = models.CharField(max_length=200)
		exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)
		created_date = models.DateTimeField(
			default=timezone.now)
		updated_date = models.DateTimeField(auto_now_add=True)

		def created(self):
			self.created_date = timezone.now()
			self.save()

		def updated(self):
			self.updated_date = timezone.now()
			self.save()
	   # def __str__(self):
		#    return self.student_id



class Grade(models.Model):
	student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
	course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
	grade = models.CharField(max_length=50)
	teacher_comment = models.CharField(max_length=200)
	attandance = models.IntegerField()
	created_date = models.DateTimeField(
		default=timezone.now)
	updated_date = models.DateTimeField(auto_now_add=True)

	def created(self):
		self.created_date = timezone.now()
		self.save()

	def updated(self):
		self.updated_date = timezone.now()
		self.save()

   # def __str__(self):
	#    return 'Grade: {} {}'.format(self.student_id, self.Student.name)
class Event(models.Model):
	event_name = models.CharField(max_length=50)
	event_description = models.TextField(max_length=200)
	created_date = models.DateTimeField(
		default=timezone.now)
	updated_date = models.DateTimeField(auto_now_add=True)

	def created(self):
		self.created_date = timezone.now()
		self.save()

	def updated(self):
		self.updated_date = timezone.now()
		self.save()

	def __str__(self):
		return self.event_name
class Event_registration(models.Model):
	event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
	parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE)
	created_date = models.DateTimeField(
		default=timezone.now)
	updated_date = models.DateTimeField(auto_now_add=True)

	def created(self):
		self.created_date = timezone.now()
		self.save()

	def updated(self):
		self.updated_date = timezone.now()
		self.save()

class Invoice(models.Model):
	student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
	parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	invoice = models.TextField(max_length=200)
	amount = models.DecimalField(max_digits=6, decimal_places=2)
	due_date= models.CharField(max_length=50)
	status= models.CharField(max_length=20)
	#status = models.CharField(max_length=20)
	created_date = models.DateTimeField(
		default=timezone.now)
	updated_date = models.DateTimeField(auto_now_add=True)

	def created(self):
		self.created_date = timezone.now()
		self.save()

	def updated(self):
		self.updated_date = timezone.now()
		self.save()

	def __str__(self):
		return self.invoice

