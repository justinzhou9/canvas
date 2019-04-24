from django.contrib import admin

# Register your models here.
from .models import Zipcode,Student,Department,Professor,Course,Prof_teams,Sections,Enrolls,\
    Prof_team_members,Homework,Homework_grades,Exams,Exam_grades,\
    Capstone_section,Capstone_Team,Capstone_Team_Members,Capstone_grades

# Register your models here.




# modify Course
class CourseAdmin(admin.ModelAdmin):
    list_display =  ('course_id', 'course_name', 'course_description',)
    ordering = ('course_id', 'course_name')
    list_per_page = 10
admin.site.register(Course,CourseAdmin)

class Prof_teamsAdmin(admin.ModelAdmin):
    list_display =  ('teaching_team_id',)
    ordering =  ('teaching_team_id',)
    list_per_page = 10
admin.site.register(Prof_teams,Prof_teamsAdmin)

class Prof_team_members_Admin(admin.ModelAdmin):
    list_display =  ('prof_email', 'teaching_team_id',)
    ordering = ('prof_email', 'teaching_team_id',)
    list_per_page = 10
admin.site.register(Prof_team_members,Prof_team_members_Admin)



class EnrollsAdmin(admin.ModelAdmin):
    list_display =  ('student_email', 'course_id', 'section_no',)
    ordering =('student_email', 'course_id', 'section_no',)
    list_per_page = 10
admin.site.register(Enrolls,EnrollsAdmin)

class HomeworkAdmin(admin.ModelAdmin):
    list_display =  ('course_id', 'sec_no', 'hw_no', 'hw_details')
    ordering = ('course_id', 'sec_no', 'hw_no', )
    list_per_page = 10
admin.site.register(Homework,HomeworkAdmin)
class Homework_grades_Admin(admin.ModelAdmin):
    list_display =  ('student_email', 'course_id', 'sec_no', 'hw_no', 'grade')
    ordering = ('student_email', 'course_id', 'sec_no', 'hw_no',)
    list_per_page = 10
admin.site.register(Homework_grades,Homework_grades_Admin)
class ExamsAdmin(admin.ModelAdmin):
    list_display =  ('course_id', 'sec_no', 'exam_no', 'exam_details')
    ordering =('course_id', 'sec_no', 'exam_no')
    list_per_page = 10
admin.site.register(Exams,ExamsAdmin)
class Exam_grades_Admin(admin.ModelAdmin):
    list_display =  ('student_email', 'course_id', 'sec_no', 'exam_no', 'grades')
    ordering =('student_email', 'course_id', 'sec_no', 'exam_no')
    list_per_page = 10
admin.site.register(Exam_grades,Exam_grades_Admin)
class Capstone_section_Admin(admin.ModelAdmin):
    list_display =  ('course_id', 'sec_no', 'project_no', 'sponsor_id')
    ordering = ('course_id', 'sec_no', 'project_no')
    list_per_page = 10
admin.site.register(Capstone_section,Capstone_section_Admin)
class Capstone_Team_Admin(admin.ModelAdmin):
    list_display =  ('course_id', 'sec_no', 'capstone_team_id', 'project_no')
    ordering =('course_id', 'sec_no', 'capstone_team_id', 'project_no')
    list_per_page = 10
admin.site.register(Capstone_Team,Capstone_Team_Admin)
class Capstone_Team_Members_admin(admin.ModelAdmin):
    list_display =  ('student_email', 'capstone_team_id', 'course_id', 'sec_no')
    ordering =('student_email', 'capstone_team_id', 'course_id', 'sec_no')
    list_per_page = 10
admin.site.register(Capstone_Team_Members,Capstone_Team_Members_admin)
class Capstone_grades_admin(admin.ModelAdmin):
    list_display =  ('course_id', 'sec_no', 'capstone_team_id', 'grade')
    ordering =('course_id', 'sec_no', 'capstone_team_id',)
    list_per_page = 10
admin.site.register(Capstone_grades,Capstone_grades_admin)

admin.site.site_header = 'Canvas Management Information Center'
admin.site.site_title = 'Canvas Management Information Center'
