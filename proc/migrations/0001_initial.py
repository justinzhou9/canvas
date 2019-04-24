# Generated by Django 2.0 on 2019-04-23 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capstone_grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=50, verbose_name='Course ID')),
                ('sec_no', models.CharField(max_length=50, verbose_name='Section No')),
                ('capstone_team_id', models.CharField(max_length=50, verbose_name='Capstone Team ID')),
                ('grade', models.CharField(max_length=50, verbose_name='Grade')),
            ],
        ),
        migrations.CreateModel(
            name='Capstone_section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=50, verbose_name='Course ID')),
                ('sec_no', models.CharField(max_length=50, verbose_name='Section No')),
                ('project_no', models.CharField(max_length=50, verbose_name='Project No')),
                ('sponsor_id', models.CharField(max_length=50, verbose_name='Sponsor ID')),
            ],
        ),
        migrations.CreateModel(
            name='Capstone_Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=50, verbose_name='Course ID')),
                ('sec_no', models.CharField(max_length=50, verbose_name='Section No')),
                ('capstone_team_id', models.CharField(max_length=50, verbose_name='Capstone Team ID')),
                ('project_no', models.CharField(max_length=50, verbose_name='Project No')),
            ],
        ),
        migrations.CreateModel(
            name='Capstone_Team_Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_email', models.CharField(max_length=50, verbose_name='Student Email')),
                ('capstone_team_id', models.CharField(max_length=50, verbose_name='Capstone Team ID')),
                ('course_id', models.CharField(max_length=50, verbose_name='Course ID')),
                ('sec_no', models.CharField(max_length=50, verbose_name='Section No')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=50, verbose_name='Course ID')),
                ('course_name', models.CharField(max_length=50, verbose_name='Course Name')),
                ('course_description', models.CharField(max_length=50, verbose_name='Course Description')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_id', models.CharField(max_length=50, verbose_name='Dept ID')),
                ('dept_name', models.CharField(max_length=50, verbose_name='Dept Name')),
                ('dept_head', models.CharField(max_length=50, verbose_name='Dept Head')),
            ],
        ),
        migrations.CreateModel(
            name='Enrolls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_email', models.CharField(max_length=50, verbose_name='Student Email')),
                ('course_id', models.CharField(max_length=50, verbose_name='Course ID')),
                ('section_no', models.CharField(max_length=50, verbose_name='Section No')),
            ],
        ),
        migrations.CreateModel(
            name='Exam_grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_email', models.CharField(max_length=50, verbose_name='Student Email')),
                ('course_id', models.CharField(max_length=50, verbose_name='Course ID')),
                ('sec_no', models.CharField(max_length=50, verbose_name='Section No')),
                ('exam_no', models.CharField(max_length=50, verbose_name='Exam No')),
                ('grades', models.CharField(max_length=50, verbose_name='Grads')),
            ],
        ),
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=50, verbose_name='Course ID')),
                ('sec_no', models.CharField(max_length=50, verbose_name='Section No')),
                ('exam_no', models.CharField(max_length=50, verbose_name='Exam No')),
                ('exam_details', models.CharField(max_length=50, verbose_name='Exam Description')),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=50, verbose_name='Course')),
                ('sec_no', models.CharField(max_length=50, verbose_name='Section No')),
                ('hw_no', models.CharField(max_length=50, verbose_name='Homework No')),
                ('hw_details', models.CharField(max_length=50, verbose_name='Homework Description')),
            ],
        ),
        migrations.CreateModel(
            name='Homework_grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_email', models.CharField(max_length=50, verbose_name='Student Email')),
                ('course_id', models.CharField(max_length=50, verbose_name='Course ID')),
                ('sec_no', models.CharField(max_length=50, verbose_name='Section No')),
                ('hw_no', models.CharField(max_length=50, verbose_name='Homework No')),
                ('grade', models.CharField(max_length=50, verbose_name='Grade')),
            ],
        ),
        migrations.CreateModel(
            name='Prof_team_members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_email', models.CharField(max_length=50, verbose_name='Professor Email')),
                ('teaching_team_id', models.CharField(max_length=50, verbose_name='Teaching Team ID')),
            ],
        ),
        migrations.CreateModel(
            name='Prof_teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teaching_team_id', models.CharField(max_length=50, verbose_name='Teaching Team ID')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('gender', models.CharField(max_length=5, verbose_name='Gender')),
                ('office_address', models.CharField(max_length=50, verbose_name='Office Address')),
                ('department', models.CharField(max_length=50, verbose_name='Department ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=50, verbose_name='Course ID')),
                ('sec_no', models.CharField(max_length=50, verbose_name='Section No')),
                ('section_type', models.CharField(max_length=50, verbose_name='Section Type')),
                ('limit', models.CharField(max_length=50, verbose_name='Limit')),
                ('teaching_team_id', models.CharField(max_length=50, verbose_name='Teaching Team ID')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('gender', models.CharField(max_length=5, verbose_name='Gender')),
                ('major', models.CharField(max_length=50, verbose_name='Major')),
                ('street', models.CharField(max_length=50, verbose_name='Street')),
                ('zipcode', models.CharField(max_length=50, verbose_name='Zipcode')),
            ],
        ),
        migrations.CreateModel(
            name='Zipcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipcode', models.CharField(max_length=50, verbose_name='Zipcode')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('state', models.CharField(max_length=50, verbose_name='State')),
            ],
        ),
    ]
