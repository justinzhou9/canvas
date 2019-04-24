from django.shortcuts import render
from . import models
import os,sys,csv
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request,"index.html")

def showLogin(request):
    return render(request,"login.html")

def getUserByEmailPasswd(email,password,userType):
    if userType == "1":
        return models.Student.objects.filter(email=email,password=password)
    elif userType == "2":
        return models.Professor.objects.filter(email=email,password=password)
    elif userType=='3':
        return adminUserLogin(email,password)

def adminUserLogin(email,password):
    auth.authenticate(email=email,password=password)
    user=User.objects.filter(email=email)
    print(user)
    return user

def getLogin(request):
    if request.method == 'POST':
         userType = request.POST.get('userType')
         email = request.POST.get('email')
         password = request.POST.get('password')

         users = getUserByEmailPasswd(email,password,userType)
         if users is not None:
             request.session.set_expiry(0)
             request.session['email'] = email
             if userType=='3':
                request.session['name'] = users[0].username
             else:
                request.session['name'] = users[0].name
             request.session['userType'] = userType
             return render(request,'index.html')
         else:
             return render(request,'login.html',{'login_error':'email or password not right'})

    return render(request,'login.html')


def setLoginOut(request):
    request.session['name'] =''
    request.session['email'] =''
    request.session['userType'] =''
    return render(request,'login.html')

def getStudentsInfo(request):
    stuList=[]
    email = request.session.get('email')
    if email is None:
        return render(request,'login.html')
    student = models.Student.objects.filter(email=email)[0]
    enrolls = models.Enrolls.objects.filter(student_email=email)
    for e in enrolls:
        course_id = e.course_id
        courses = models.Course.objects.filter(course_id=course_id)[0]
        prof_team_members = models.Prof_team_members.objects.filter(teaching_team_id=course_id)[0]
        professors = models.Professor.objects.filter(email=prof_team_members.prof_email)[0]
        sections = models.Sections.objects.filter(course_id=course_id)[0]
        section_no = sections.sec_no
        exams = models.Exams.objects.filter(course_id=course_id,sec_no=section_no)[0]
        exam_no = exams.exam_no
        exam_grades = models.Exam_grades.objects.filter(student_email=email,course_id=course_id,sec_no=section_no,exam_no=exam_no)
        grade=''
        if len(exam_grades)>0:
            grade = exam_grades[0].grades

        stuList.append({"email":email,"name":student.name,"course_id":courses.course_id,"course_name":courses.course_name,"course_desc":courses.course_description,
                       "professor_email":professors.email,"exam_no":exam_no,"grade":grade})
    return render(request,'showStudent.html',{'infoList':stuList,"title":"Student Info","noc":"1"})

def getRestPasswd(request):
    userType=request.session.get("userType")
    if userType=="1":
        return render(request,"resetPasswd.html")
def resetPasswd(request):
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    email = request.session.get("email")
    if password==password2:
        models.Student.objects.filter(email=email).update(password=password)
        return render(request,"index.html",{"message":"Reset password successed"})
    else:
        return render(request,"resetPasswd.html",{"message":"passwords not the same"})

def getHomeworkList(request):
    email=request.session.get("email")
    ptms=models.Prof_team_members.objects.filter(prof_email=email)
    hws=[]
    for c in ptms:
        cs =models.Course.objects.filter(course_id=c.teaching_team_id)[0]
        secs=models.Sections.objects.filter(course_id=c.teaching_team_id)[0]
        hwList = models.Homework.objects.filter(course_id=c.teaching_team_id,sec_no=secs.sec_no)
        for hw in hwList:
            hws.append({"course_id":hw.course_id,"sec_no":hw.sec_no,"hw_no":hw.hw_no,"hw_details":hw.hw_details})
    return render(request,"showHomework.html",{"infoList":hws,"noc":"1"})

def setHomework(request):
    email=request.session.get("email")
    ptms=models.Prof_team_members.objects.filter(prof_email=email)
    sections=[]
    courses=[]
    for c in ptms:
        cs =models.Course.objects.filter(course_id=c.teaching_team_id)[0]
        secs=models.Sections.objects.filter(course_id=c.teaching_team_id)[0]
        courses.append({"course_id":cs.course_id,"course_name":cs.course_name})
        sections.append({"sec_no":secs.sec_no})
    return render(request,"addHomework.html",{"courses":courses,"sections":sections})


def setExam(request):
    email=request.session.get("email")
    ptms=models.Prof_team_members.objects.filter(prof_email=email)
    sections=[]
    courses=[]
    for c in ptms:
        cs =models.Course.objects.filter(course_id=c.teaching_team_id)[0]
        secs=models.Sections.objects.filter(course_id=c.teaching_team_id)[0]
        courses.append({"course_id":cs.course_id,"course_name":cs.course_name})
        sections.append({"sec_no":secs.sec_no})
    return render(request,"addExam.html",{"courses":courses,"sections":sections})


def addExam(request):
    course_id = request.GET.get('course')
    section_id = request.GET.get('section')
    exam_details = request.GET.get("exam_details")
    exams = models.Exams.objects.filter(course_id=course_id,sec_no=section_id)
    for e in exams:
        ex_no = float(e.exam_no)+1
        models.Exams.objects.create(course_id=course_id,sec_no=section_id,exam_no=ex_no,exam_details=exam_details)
    return render(request,"index.html",{"meesage":"add homework successed"})



def addHomework(request):
    course_id = request.GET.get('course')
    section_id = request.GET.get('section')
    hw_details = request.GET.get("hw_details")
    hw = models.Homework.objects.filter(course_id=course_id,sec_no=section_id)
    for h in hw:
        hw_no = float(h.hw_no)+1
        models.Homework.objects.create(course_id=course_id,sec_no=section_id,hw_no=hw_no,hw_details=hw_details)
    return render(request,"index.html",{"meesage":"add homework successed"})



def getExamList(request):
    email=request.session.get("email")
    ptms=models.Prof_team_members.objects.filter(prof_email=email)
    exs=[]
    for c in ptms:
        cs =models.Course.objects.filter(course_id=c.teaching_team_id)[0]
        secs=models.Sections.objects.filter(course_id=c.teaching_team_id)[0]
        examList = models.Exams.objects.filter(course_id=c.teaching_team_id,sec_no=secs.sec_no)
        for ex in examList:
            exs.append({"course_id":cs.course_id,"sec_no":ex.sec_no,"exam_no":ex.exam_no,"exam_details":ex.exam_details})
    return render(request,"showExam.html",{"infoList":exs,"noc":"1"})

def setAddExam(request):
    course_id = request.GET.get('course')
    section_id = request.GET.get('section')
    exam_details = request.GET.get("exam_details")
    exams = models.Exams.objects.filter(course_id=course_id,sec_no=section_id)
    for e in exams:
        ex_no = int(e.hw_no)+1
        models.Exams.objects.create(course_id=course_id,sec_no=section_id,exam_no=ex_no,ex_details=exam_details)
    return render(request,"index.html",{"isBG":1,"meesage":"add homework successed"})


def getProfessorList(request):
    result=[]
    email = request.session.get('email')
    if email is None:
        return render(request,'login.html')
    profs = models.Professor.objects.filter(email=email)[0]

    professor_name = profs.name
    office = profs.office_address
    pts = models.Prof_team_members.objects.filter(prof_email=email)
    for pt in pts:
        email_id = pt.teaching_team_id
        course_id = pt.teaching_team_id

        courses = models.Course.objects.filter(course_id=course_id)[0]
        enrolls = models.Enrolls.objects.filter(course_id=course_id)
        for e in enrolls:
            student_email=e.student_email
            section_no = e.section_no
            student = models.Student.objects.filter(email=student_email)[0]
            hw=models.Homework.objects.filter(course_id=course_id,sec_no=section_no)[0]
            hwg=models.Homework_grades.objects.filter(course_id=course_id,sec_no=section_no,hw_no=hw.hw_no)
            hwg_grade=""
            if len(hwg)>0:
                hwg_grade=hwg[0].grade
            exam=models.Exams.objects.filter(course_id=course_id,sec_no=section_no)[0]
            exms = models.Exam_grades.objects.filter(student_email=student_email,course_id=course_id,sec_no=section_no,exam_no=exam.exam_no)
            grade=""
            if len(exms)>0:
                grade=exms[0].grades
            result.append({"email":email,"name":profs.name,"office":office,"course_id":course_id,"course_name":courses.course_name,
                           "course_desc":courses.course_description,"sec_no":section_no,"student_name":student.name,
                           "hw_no":hw.hw_no,"hw_grade":hwg_grade,"exam_no":exam.exam_no,"exms_grade":grade})
    return render(request,"showProfessor.html",{"title":"Professor Info","proList":result,"noc":"1"})


def getImport(request):
    return render(request,'import.html')

def setImport(request):
    file = request.FILES.get('csvfile')
    if not file:
        return render(request,'import.html', {"message":"upload csv file failed."})
    else:
        path_name=os.path.join(os.getcwd(),'proc/upload',file.name)
        f  = open(path_name,'wb')
        for chunk in file.chunks():
           f.write(chunk)
        f.close()
        readCsv(path_name,file.name)
        return render(request,'import.html',{"message":"upload csf file successful"})

def readCsv(file,name):
    print(name)
    if name=='Students.csv':
        deleteStudents()
        readStudent(file)
    elif name=='Professors.csv':
        deleteProfessors()
        readProfessor(file)

def readStudent(file):
    csv_file = csv.reader(open(file,'r'))
    next(csv_file)
    for row in csv_file:
        name = row[0]
        email = row[1]
        age	= row[2]
        zip	= row[3]
        phone = row[4]
        gender	= row[5]
        city = row[6]
        state = row[7]
        password = row[8]
        street = row[9]
        major = row[10]
        course_id = row[11]    ####course 1
        course_name = row[12]
        course_detail = row[13]
        sec_type = row[14]
        sec_no = row[15]
        limit = row[16]
        hw_no = row[17]
        hw_details = row[18]
        hw_grade = row[19]
        exam_no = row[20]
        exam_details = row[21]
        ex_grade = row[22]
        course_id2 = row[23]  #####course 2
        course_name2 = row[24]
        course_detail2 = row[25]
        sec_type2 = row[26]
        sec_no2 = row[27]
        limit2 = row[28]
        hw_no2 = row[29]
        hw_details2 = row[30]
        hw_grade2 = row[31]
        exam_no2 = row[32]
        exam_details2 = row[33]
        ex_grade2 = row[34]
        course_id3 = row[35] #### course 3
        course_name3 = row[36]
        course_detail3 = row[37]
        sec_type3 = row[38]
        sec_no3 = row[39]
        limit3 = row[40]
        hw_no3 = row[41]
        hw_details3 = row[42]
        hw_grade3 = row[43]
        exam_no3 = row[44]
        exam_details3 = row[45]
        ex_grade3 = row[46]
        models.Zipcode.objects.create(zipcode=zip,city=city,state=state)
        zips=models.Zipcode.objects.filter(zipcode=zip)
        students=models.Student.objects.filter(email=email)
        if len(students)==0:
            models.Student.objects.create(email=email,password=password,name=name,age=int(age),gender=gender,major=major,street=street,zipcode=zips[0])
        addCourse(course_id,course_name,course_detail)
        addCourse(course_id2,course_name2,course_detail2)
        addCourse(course_id3,course_name3,course_detail3)
        addSection(course_id,sec_no,limit,sec_type)
        addSection(course_id2,sec_no2,limit2,sec_type2)
        addSection(course_id3,sec_no3,limit3,sec_type3)
        addEnrolls(email,course_id,sec_no )
        addEnrolls(email,course_id2,sec_no3 )
        addEnrolls(email,course_id3,sec_no3 )
        addHomework(course_id,sec_no,hw_no ,hw_details)
        addHomework(course_id2,sec_no2,hw_no2 ,hw_details2)
        addHomework(course_id3,sec_no3,hw_no3 ,hw_details3)
        addHomeworkGrade(email,course_id, sec_no,hw_no,hw_grade)
        addHomeworkGrade(email,course_id2, sec_no2,hw_no2,hw_grade2)
        addHomeworkGrade(email,course_id3, sec_no3,hw_no3,hw_grade3)
        addExam(course_id, sec_no,exam_no,exam_details)
        addExam(course_id2, sec_no2,exam_no2,exam_details2)
        addExam(course_id3, sec_no3,exam_no3,exam_details3)
        addExamGrade(email,course_id,sec_no,exam_no,ex_grade)
        addExamGrade(email,course_id2,sec_no2,exam_no2,ex_grade2)
        addExamGrade(email,course_id3,sec_no3,exam_no3,ex_grade3)



def addCourse(course_id,course_name,course_detail):
    models.Course.objects.create(course_id=course_id,course_name=course_name,course_description=course_detail)

def addSection(course_id,sec_no,limit,section_type):
    models.Sections.objects.create(course_id=course_id,sec_no=sec_no,limit=limit,section_type=section_type)
    if section_type=='Cap':
        addCapstone_section(course_id,sec_no,None,None)


def addCapstone_section(course_id, sec_no, project_no, sponsor_id):
    models.Capstone_section.objects.create(course_id=course_id, sec_no=sec_no)

def addEnrolls(email,course_id,sec_no ):
    models.Enrolls.objects.create(student_email=email,course_id=course_id,section_no=sec_no)

def addHomework(course_id,sec_no,hw_no ,hw_details):
    models.Homework.objects.create(course_id=course_id,sec_no=sec_no,hw_no=hw_no,hw_details=hw_details)

def addHomeworkGrade(email,course_id, sec_no,hw_no,hw_grade):
    models.Homework_grades.objects.create(student_email=email,course_id=course_id,sec_no=sec_no,hw_no=hw_no,grade=hw_grade)

def addExam(course_id, sec_no,exam_no,exam_details):
    models.Exams.objects.create(course_id=course_id,sec_no=sec_no,exam_no=exam_no,exam_details=exam_details)

def addExamGrade(email,course_id,sec_no,exam_no,ex_grade):
    models.Exam_grades.objects.create(student_email=email,course_id=course_id,sec_no=sec_no,exam_no=exam_no,grades=ex_grade)

def readProfessor(file):
    csv_file = csv.reader(open(file,'r',encoding='utf-8'))
    next(csv_file)
    for line in csv_file:
        name = line[0]
        email = line[1]
        password = line[2]
        age	= line[3]
        gender	= line[4]
        dept_id = line[5]
        office_address = line[6]
        dept_name = line[7]
        title = line[8]
        teach = line[9]
        teaching_team_id = line[10]
        depts = models.Department.objects.filter(dept_id=dept_id)
        if len(depts) ==0:
            models.Department.objects.create(dept_id=dept_id,dept_name=dept_name)
        profs = models.Professor.objects.filter(email=email)
        if len(profs) == 0:
            models.Professor.objects.create(email=email,password=password,name=name,age=int(age),gender=gender,office_address=office_address,title=title,department=dept_id)
        pts = models.Prof_teams.objects.filter(teaching_team_id=teaching_team_id)
        if len(pts)==0:
            models.Prof_teams.objects.create(teaching_team_id=teaching_team_id)
        capstone_section = models.Capstone_section.objects.filter(course_id=teaching_team_id)
        if len(capstone_section)==0:
            models.Capstone_section.objects.filter(course_id=teaching_team_id).update(sponsor_id=email)
        ptms = models.Prof_team_members.objects.filter(prof_email=email,teaching_team_id=teaching_team_id)
        if len(ptms)==0:
            models.Prof_team_members.objects.create(prof_email=email,teaching_team_id=teaching_team_id)



def deleteStudents():
    models.Student.objects.all().delete()
    models.Zipcode.objects.all().delete()
    models.Course.objects.all().delete()
    models.Sections.objects.all().delete()
    models.Enrolls.objects.all().delete()
    models.Homework.objects.all().delete()
    models.Homework_grades.objects.all().delete()
    models.Exams.objects.all().delete()
    models.Exam_grades.objects.all().delete()
    models.Capstone_section.objects.all().delete()
    models.Capstone_Team.objects.all().delete()
    models.Capstone_Team_Members.objects.all().delete()
    models.Capstone_grades.objects.all().delete()

def deleteProfessors():
    models.Department.objects.all().delete()
    models.Professor.objects.all().delete()
    models.Prof_teams.objects.all().delete()
    models.Prof_team_members.objects.all().delete()

