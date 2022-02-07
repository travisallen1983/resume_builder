import time
import matplotlib.pyplot as plt 
from datetime import date

date = date.today()
date = date.strftime("%B_%d_%Y")

jobs = []
skills = []
education = []
employer = ''
# Text Variables
print('\n')
print('\n')
print('Welcome to this simple, work-in-progress resume builder.')
time.sleep(.5)
print('\n')
print("Let's start with a few general questions about you.")
time.sleep(.5)
first_name = str(input('What is your first name? '))
first_name = first_name.strip().lower().capitalize()
last_name = str(input('Okay ' + first_name + ', what is your last name? '))
last_name = last_name.strip().lower().capitalize()
name = first_name + ' ' + last_name
title = str(input('What job title best describes the postion you are applying for? '))
title = title.strip().lower().title()
city = str(input('What city do you currently live in? '))
city = city.strip().lower().capitalize()
state = str(input('What state do you currently live in? '))
state = state.strip().upper()
state = state[0:2]
address =  city + ', ' + state
phone = str(input('What is you phone number? '))
phone = phone.strip()
email = str(input('What is your preferred email address? '))
email = email.strip()
github = str(input('if you have a github, what is your github address?'))
github = github.strip()

skills_header = 'Skills'
skills.append('HEAD_' + skills_header)

for i in range(1,5):
    if i == 1:
        print('\n')
        print("Alright " + first_name + ", let's add some of your skills.")
        print('\n')
        time.sleep(1)
        print("Input up to four skills.")
        time.sleep(1)
    if i == 1:
        skill = str(input('What do you want listed as your top skill? '))
    elif i == 2:
        skill = str(input('After ' + skill[2:] + ', what do you want as your ' + str(i) + 'nd skill? '))
    elif i == 3:
        skill = str(input('After ' + skill[2:] + ', what do you want as your ' + str(i) + 'rd skill? '))
    else:
        skill = str(input('How about one final skill to round it all out? '))        
    skill = '- ' + skill.strip()
    skills.append('DESC_' + skill)

experience_header = 'WORK EXPERIENCE'
for i in range(1,4):
    if i == 1:
        print('\n')
        print("Let's add some work experience.\n\nStart with your most recent employer and then add two more.")
        currently_employed = input(str('Are you currently employed(Y/N)? '))
        currently_employed = currently_employed.strip().upper()[0]
    if i >= 2: 
        print('\n')
        print("That is enough about " + employer + ".\nLet's move on to your next employer.") 

    if i == 1 and currently_employed == 'Y':
        employer = str(input('Who is your current employer? '))
        job_title = str(input('What is your job title at ' + employer  + '? '))
    if i == 1 and currently_employed == 'N':
        employer = str(input('Who was your most recent employer? '))
        job_title = str(input('What is was job title at ' + employer  + '? ')) 
    if  i >= 2:
        employer = str(input('Who is your next most recent employer? '))
        job_title = str(input('What was your job title at ' + employer  + '? '))
    employment_start_year = str(input('What year did you start at ' + employer  + '? '))
    employment_start_month = str(input('What month did you start at ' + employer  + '? '))
    if employment_start_month in list('123456789'):
        employment_start_month = '0' + employment_start_month        
    employment_start_date =  employment_start_month + '/' + employment_start_year

    if i == 1 and currently_employed == 'Y':
        print('\n')
        print("Since you are currently employed at " + employer + " your employment end date will be set as 'present'")
        employment_end_date = 'Present'
    else:
        employment_end_year = str(input('What was your last year at ' + employer  + '? '))
        employment_end_month = str(input('What was your last month at ' + employer  + '? '))
        if employment_end_month in list('123456789'):
            employment_end_month = '0' + employment_end_month        
    if i == 2 or i == 3:
        employment_end_date =  employment_end_month + '/' + employment_end_year            
            
    jobs.append('HEAD_' + job_title + ' at ' + employer + '(' + employment_start_date + ' - ' + employment_end_date + ')' )
    if i == 1: 
        print('\n')
        print("Now we just need a few sentences about the job.\n\nAfter each complete sentence, hit enter to continue the description.")
    for j in range(1,7):
        if j == 1:
            job_desc = str(input('How would you describe your work at ' + employer + '? '))
        if j >= 2:
            continue_check = str(input('Do you want to add more to your job description(Y/N)? '))
            continue_check = 'Y'
            if continue_check == 'Y':
                job_desc = str(input('>> '))
        if job_desc!= '':
            jobs.append('DESC_' + job_desc)

education_header = 'EDUCATION'        
            
for i in range(1,4):
    if i == 1:
        print('\n')
        print('Alright, you are almost finished. The last thing needed is education.')
        print('\n')
        print("The first two prompts will be for schools you attended.\n\nThe last prompt will be for any bootcamps you might have gone through.")
    if i == 1:
        institution = str(input('What is the name of the most recent education institution you attended? '))
    if i == 2:
        institution = str(input('What is the name of the ' + str(i) + 'nd most recent education institution you attended? '))
    if i == 3:
        institution = str(input('If you attended a bootcamp or workshop, what was the orginizations name? '))
    if i == 1 or i == 2:
        degree = str(input('What degree did you receive from ' + institution + '? '))
        major = str(input('What was your major at '  + institution + '?'))
        GPA = str(input('Finally, what was your GPA at '  + institution + '?'))
        education_start_year = str(input('What year did you start at ' + institution  + '? '))
        education_start_month = str(input('What month did you start at ' + institution  + '? '))

        if education_start_month in list('123456789'):
            education_start_month = '0' + education_start_month        
        education_start_date =  education_start_month + '/' + education_start_year
        education_end_year = str(input('What was you last year at ' + institution  + '? '))
        education_end_month = str(input('What was you last month at ' + institution  + '? '))
        if education_end_month in list('123456789'):
            education_end_month = '0' + education_end_month        
        education_end_date =  education_end_month + '/' + education_end_year
    if i ==3:
        degree = str(input('What was the name of the program offered by ' + institution + '? '))
        major = str(input('What programming languages did you learn from '  + degree + '?'))
        education_start_date = str(input('What year did you attend ' + degree + '? '))        
        
    if i ==1 or i ==2:
        education_title = institution + ', ' + degree + '(' + education_start_date + ' - ' + education_end_date + ')'
        major_desc = 'Major: ' + major + '(' + GPA + ' GPA)'
    if i ==3:
        education_title = institution + ', ' + degree + '(' + education_start_date + ')'
        major_desc = 'Languages: ' + major
        
    education.append('HEAD_' + education_title)
    education.append('DESC_' + major_desc)     
               

print('\nCool that is everything the resume builder currently takes.\n\nNow it just needs to be made into a document.')
time.sleep(2)
Footer = 'This resume was built with python and the matplotlib library.\n  The code can be seen at' + github +'.'

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral' 
fig, ax = plt.subplots(figsize=(8.5, 11))


header_font_size = 12
text_font_size = 10

r,g,b = 0 ,0, 0
r_super, g_super, b_super = 0, 0, 0
xmin, xmax = 0, 0.01
xmax_super, xmin_super = 0, 0

for i in range(100):
    plt.axhline(y=.99, xmin=xmin, xmax=xmax, color=(r,g,b), linewidth=200)# set background color
    xmin_super = xmax_super
    xmin = xmin_super/100
    xmax_super = i
    xmax = (xmax_super + 1)/100
    r_super = r_super + .6
    g_super = g_super + 1
    b_super = b_super + .65

    r = (r_super)/100
    g = (g_super)/100
    b = (b_super)/100

ax.set_facecolor('white')# remove axes
plt.axis('off')# add text
personal_info = [name, address, phone, email, github]
x=.02
y=.95
weight = ''
fontsize = 0
count = 0
r,g,b = 0 ,0, 0
r_super, g_super, b_super = 0, 0, 0
color = 'black'
for info in personal_info:
    if info == name:
        weight = 'bold'
        fontsize = header_font_size
    else:
        weight = 'regular'
        fontsize = text_font_size
    plt.annotate(info, (x, y), weight = weight, fontsize = fontsize, color=color)
    fontsize_offset = (fontsize - 8)/100
    y = y - fontsize_offset

x=.70
y=.95
weight = ''
fontsize = 0
count = 0
color = 'black'
for skill in skills:   
    if skill[0:4] == 'HEAD':    
        weight = 'bold'
        fontsize = header_font_size
    else:
        weight = 'regular'
        fontsize = text_font_size
    plt.annotate(skill[5:], (x,y), weight=weight, fontsize=fontsize, color=color)
    fontsize_offset = (fontsize - 8)/100
    y = y - fontsize_offset
    count = count + 1
y = y-.02
plt.axhline(y=y, xmin=0, xmax=1, color=(0,0,0), linewidth=2.5)
plt.annotate(title, (.30, .785), weight = 'regular', fontsize = header_font_size, color='black')
y= y-.04
plt.axhline(y= y, xmin=0, xmax=1, color=(0,0,0), linewidth=2.5)
plt.annotate(experience_header, (.02,.735), weight='bold', fontsize=header_font_size, color='darkgreen')


y = y - .07
x=.02
y= y
weight = ''
fontsize = 0
count = 0
color = 'black'
for job in jobs:
    if job[0:4] == 'HEAD': 
        weight = 'bold'
        fontsize = header_font_size
    else:
        weight = 'regular'
        fontsize = text_font_size
    if job[0:4] == 'HEAD' and job != jobs[0]:
        y = y - .02
    plt.annotate(job[5:], (x,y), weight=weight, fontsize=fontsize, color=color)
    count_newline = job.count('\n')
    fontsize_offset = (fontsize - 8)/100
    y = y - fontsize_offset
    
plt.annotate(education_header, (.02,.3), weight='bold', fontsize=header_font_size, color='darkgreen')


y = y -.037
x = .02
weight = ''
fontsize = 0
count = 0
color = 'black'
for school in education:
    if school[0:4] == 'HEAD':
        weight = 'bold'
        fontsize = header_font_size
    else:
        weight = 'regular'
        fontsize = text_font_size
    if school[0:4] == 'HEAD' and job != school[0]:
        y = y - .02
    plt.annotate(school[5:], (x,y), weight=weight, fontsize=fontsize, color=color)
    count_newline = school.count('\n')
    fontsize_offset = (fontsize - 9)/100
    y = y - fontsize_offset

r,g,b = 0 ,0, 0
r_super, g_super, b_super = 0, 0, 0
xmin, xmax = 0, 0
xmax_super, xmin_super = 0, 0

for i in range(100):
    plt.axhline(y=.01, xmin=xmin, xmax=xmax, color=(r,g,b), linewidth=60)# set background color
    xmin_super = xmax_super
    xmin = xmin_super/100
    xmax_super = i
    xmax = (xmax_super + 1)/100
    r_super = r_super + .6
    g_super = g_super + 1
    b_super = b_super + .65
    r = (r_super)/100
    g = (g_super)/100
    b = (b_super)/100
    
y = y - .085
x = .2
plt.annotate(Footer, (x, y), weight='bold', fontsize=text_font_size)

plt.savefig('resume' + date + '.pdf', dpi=300, bbox_inches='tight')