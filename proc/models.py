from django.db import models

# Create your models here.

class Student(models.Model):
    email=models.CharField( max_length=50, verbose_name="Email")
    password=models.CharField(max_length=50, verbose_name="Password")
    name=models.CharField(max_length=50, verbose_name="Name")
    age=models.IntegerField(verbose_name="Age")
    gender=models.CharField(max_length=5, verbose_name="Gender")
    major=models.CharField(max_length=50, verbose_name="Major")
    street=models.CharField(max_length=50, verbose_name="Street")
    zipcode = models.CharField(max_length=50, verbose_name="Zipcode")

class Zipcode(models.Model):
    zipcode=models.CharField(max_length=50, verbose_name="Zipcode" )
    city=models.CharField(max_length=50, verbose_name="City")
    state=models.CharField(max_length=50, verbose_name="State")

class Professor(models.Model):
    email=models.CharField( max_length=50, verbose_name="Email")
    password=models.CharField(max_length=50, verbose_name="Password")
    name=models.CharField(max_length=50, verbose_name="Name")
    age=models.IntegerField(verbose_name="Age")
    gender=models.CharField(max_length=5, verbose_name="Gender")
    office_address=models.CharField(max_length=50, verbose_name="Office Address")
    department = models.CharField(max_length=50, verbose_name="Department ID")
    title=models.CharField(max_length=50, verbose_name="Title")

class Department(models.Model):
    dept_id=models.CharField(max_length=50, verbose_name="Dept ID")
    dept_name=models.CharField(max_length=50, verbose_name="Dept Name")
    dept_head=models.CharField(max_length=50, verbose_name="Dept Head")


class Course(models.Model):
    course_id=models.CharField(max_length=50, verbose_name="Course ID")
    course_name=models.CharField(max_length=50, verbose_name="Course Name")
    course_description=models.CharField(max_length=50, verbose_name="Course Description")

class Sections(models.Model):
    course_id = models.CharField(max_length=50, verbose_name="Course ID")
    sec_no = models.CharField(max_length=50, verbose_name="Section No")
    section_type = models.CharField(max_length=50, verbose_name="Section Type")
    limit = models.CharField(max_length=50, verbose_name="Limit")
    teaching_team_id = models.CharField(max_length=50, verbose_name="Teaching Team ID")

class Enrolls(models.Model):
    student_email = models.CharField(max_length=50, verbose_name="Student Email")
    course_id = models.CharField(max_length=50, verbose_name="Course ID")
    section_no = models.CharField(max_length=50, verbose_name="Section No")


class Prof_teams(models.Model):
    teaching_team_id = models.CharField(max_length=50, verbose_name="Teaching Team ID")


class Prof_team_members(models.Model):
    prof_email = models.CharField(max_length=50, verbose_name="Professor Email")
    teaching_team_id = models.CharField(max_length=50, verbose_name="Teaching Team ID")

class Homework(models.Model):
    course_id = models.CharField(max_length=50, verbose_name="Course")
    sec_no = models.CharField(max_length=50, verbose_name="Section No")
    hw_no = models.CharField(max_length=50, verbose_name="Homework No")
    hw_details = models.CharField(max_length=200, verbose_name="Homework Description")

class Homework_grades(models.Model):
    student_email= models.CharField(max_length=50, verbose_name="Student Email")
    course_id = models.CharField(max_length=50, verbose_name="Course ID")
    sec_no = models.CharField(max_length=50, verbose_name="Section No")
    hw_no = models.CharField(max_length=50, verbose_name="Homework No")
    grade = models.CharField(max_length=50, verbose_name="Grade")


class Exams(models.Model):
    course_id = models.CharField(max_length=50, verbose_name="Course ID")
    sec_no = models.CharField(max_length=50, verbose_name="Section No")
    exam_no = models.CharField(max_length=50, verbose_name="Exam No")
    exam_details = models.CharField(max_length=200, verbose_name="Exam Description")


class Exam_grades(models.Model):
    student_email= models.CharField(max_length=50, verbose_name="Student Email")
    course_id = models.CharField(max_length=50, verbose_name="Course ID")
    sec_no = models.CharField(max_length=50, verbose_name="Section No")
    exam_no = models.CharField(max_length=50, verbose_name="Exam No")
    grades = models.CharField(max_length=50, verbose_name="Grads")



class Capstone_section(models.Model):
    course_id =  models.CharField(max_length=50, verbose_name="Course ID")
    sec_no = models.CharField(max_length=50, verbose_name="Section No")
    project_no = models.CharField(max_length=50, verbose_name="Project No")
    sponsor_id = models.CharField(max_length=50, verbose_name="Sponsor ID")



class Capstone_Team(models.Model):
    course_id = models.CharField(max_length=50, verbose_name="Course ID")
    sec_no = models.CharField(max_length=50, verbose_name="Section No")
    capstone_team_id = models.CharField(max_length=50, verbose_name="Capstone Team ID")
    project_no = models.CharField(max_length=50, verbose_name="Project No")


class Capstone_Team_Members(models.Model):
    student_email=models.CharField(max_length=50, verbose_name="Student Email")
    capstone_team_id = models.CharField(max_length=50, verbose_name="Capstone Team ID")
    course_id = models.CharField(max_length=50, verbose_name="Course ID")
    sec_no = models.CharField(max_length=50, verbose_name="Section No")



class Capstone_grades(models.Model):
    course_id = models.CharField(max_length=50, verbose_name="Course ID")
    sec_no = models.CharField(max_length=50, verbose_name="Section No")
    capstone_team_id = models.CharField(max_length=50, verbose_name="Capstone Team ID")
    grade = models.CharField(max_length=50, verbose_name="Grade")

