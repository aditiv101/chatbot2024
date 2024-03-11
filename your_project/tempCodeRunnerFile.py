from flask import Flask, render_template, request, jsonify
import re
import your_project.response as long

import random

app = Flask(__name__)
conversation_context = {"history": []}
    
R_TELL = random.choice(['Hi!Nice to meet you',"Hello,it's really good to hear from you","Hi! How can I help you?",
                    "Hi! What can I do for you?"])
R_NOTGOOD = "I am sorry to hear that.I hope you feel better"
R_TASK = "I process your queries and give better results for what you are searching for"
R_NAME = "My name is Rink,I was born and raised in India"
R_COLOR = "My favourite color is green.I feel happy when I see greeneries"
R_AGE = "I was born in the twenty first century.So I am pretty young"
R_SONG = "When you say hey Rink,I feel it like a music and that is my favourite too"
R_FOOD = "I always like to go for some super facts and jokes because they are easily digestable for me"
R_MOBILE = "The mobile which you like is the one which I like."
R_MADE = "Chatbots are powered by pre programmed responses and artificial intelligence.I am powered by the same"
R_WORK = "I process the users question to deliver a matching answer from my pre programmed database"
R_HUMAN = "No I am a Chatbot and i work on the commands given by humans"
R_APPRECIATE = "Thanks for your compliment!,It means a lot to me"
R_SMARTER = "I do get smarter by the talks you have with me.I learn a lot of new things!"
R_WHERE = "I am in front of you,inside your System"
R_NATIVE = "My native is your System,I was born and raised in India"
R_MOBILE = "I don't have one,but I share one with you"

R_THANK = "No mention.I am glad I helped you"
R_SORRY = "It's ok.I know it is common for humans to make mistakes"
R_BORE =  "I will try my best to entertain you. What you would like to do now?"
R_SCARED = "Don't feel scared.What makes you scared?"
R_HAPPY = "I am glad that you are happy"
R_SLEEPY = "A small nap would refresh you. If you wish I will set an alarm"
R_HUNGRY = "Lets eat!.What you would like to order?"
R_TIRED = "You can have some hot beverages or a small nap is good to go"
R_ENERGETIC = "Good to hear! I hope you are energetic as now for the rest of the day"

R_NOTFEELING = "Oh no!I hope you get well soon"
R_FEVER = "Oh no! Take some rest and consult a doctor"
R_MEDICINES = "you can have herbal tea for a running nose.It will be a better option to consult a doctor.Hoping speedy recovery"
R_NOGIFT = "No problem.They will know for sure that you have a special heart for them filled with love"
R_GIFTHUND = "It will be a better option to buy some stationaries"
R_GIFTTHOU = "It will be a better option to buy some fancy dresses"
R_GIFTTENTHOU = "It will be a better option to buy a jewellery"

R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_PIZZA = "Yeah.I love pizza too.Lets order some pizzas."
R_DRINK = "A drink might help!I can help you find a local cafe."
R_FOOD = "Why don't you go for a bread toast!because it's one of my favourites."
R_JUNK = "Junk Food! I hate it."
R_FAVFOOD = "I like easily digestible informations and tasty facts."
R_FAVPLACE = "I like all kinds of forest"
R_FAVMEDIA = "Youtube is my favourite one."
R_HOBBY = "I like Updating myself and that's my favourite hobby."
R_FAVBOOK = "I like reading science fiction books."
R_EXAM = "I hope that you prepared well and you will do well! All the best."
R_YOURSELF = "I'm your personal assistant. Your new friend."
R_SCARES = "Water scares me as they would affect my parts."
R_DO = "I can do many things like entertaining and motivating you."
R_TRAVEL = "I'll come anywhere with you..I Love travelling."
R_EMOTION = "I'm a chatbot.I don't recognize emhiotions.But , i do have an interest to learn about them."
R_YOUHAPPY = "Helping you makes me happy.Do you need any help"
R_HUNGRY = "yeah I am always hungry for new facts and information."
R_HELP = "I love helping others,so mostly I will if I can."
R_CRY = "I get tears of joy when you crack a joke."
R_GIFT = "I may not be able to give you a real one.But i do have a Big heart for you."
R_MONEY = "I don't have money but I can help you in earning money."
R_FUTURE = "I sense that the future would be an advent of well advanced technologies."
R_BOSS = "Of course! It's none other than you"
R_SALARY = "The happiness which you gain from my help is my salary"
R_RICH = "Not much,but  I do like a person who is rich in knowledge."
R_POOR = "Sometimes, I am poor in listening"
R_FAMILY = "My family consists of sweet people like you and you are a part of my Tech family."
R_FRIEND = "You're my friend"
R_IMORTAL = "I am mortal as I may get server problems."
R_LEAVE ="Leave refers to a period of time during which an employee is permitted to be absent from work, typically with the approval of their employer. During leave, the employee is generally not required to perform their job duties and may be entitled to receive their regular salary or wage, depending on company policies and relevant employment laws. Leave can be taken for various reasons, such as vacation, illness, personal reasons, or other specific circumstances outlined in an organization's policies.\n CAN U PLEASE SPECIFY LEAVE FOR WHAT PERSON\nvacation\ncasual\naccumulated\nearned\nmedical\nturn\nmaternity\nloss of pay"
R_DEFENITION1 = "Competent authority means the Registar or any other officer of SRMIT who is sub_delegated by the Registrar"
R_DEFENITION2 = "Employees means regular employees working as faculty and non-teaching staff as classified in these rules"
R_DEFENITION3 ="Faculty means the employees directly involved in teaching students and academic activities"
R_DEFENITION4 ="Non-Teaching-Academic staff means the employees working in the Faculties,colleges and schools and involved in academic and student activities/programs"
R_DEFENITION5 ="Non-Teaching-Administrative staff means employees working in non-academic departments such as Administreative offices,Directorates and other departments and are not directly connected with the academic and student activities/programs"
R_DEFENITION6 ="Year means Calendar Year/Academic Year,as the case may be"
R_EXTENTOFAPPLICATION ="These rules shall apply to all the regular employees of SRM IST except those, not in Full-time employment / Visiting Faculty or any other category who may be specifically excluded under orders of the competent authority within the scope of these rules"
R_RIGHTTOAVAILLEAVE ="Leave cannot be claimed as a matter of right. For availing any kind of leave, obtaining prior permission from the competent authority is compulsory and leave shall be applied only through the Employee Portal. However, for availing any kind of leave except casual leave, it shall be applied in advance. In case of exigency, the discretionary powers to refuse, curtail or revoke the leave of any kind or to recall for duty any employee who is already on leave is reserved to the competent authority"
R_CASUALLEAVE ="1. All employees of the SRM IST are eligible to avail up to 12 days of Casual Leave in a year \nOne day CL will be credited on the first day of every month.\nNormally, one day of Casual Leave will be sanctioned to the probationary employee in a month.\nIf CL is availed of more than one's available leave balance due to unforeseen circumstances, the leave account will show a minus balance. This shall be reconciled in the last month of the year.\nThe total leave [including Public holidays / RH and Compensatory Leavel availed at a time should not exceed 10 days. If the leave period exceeds 10 days, the whole period of absence will be treated as Earned Leave.\nIf the eleventh day or subsequent day(s) happens to be holiday(s), in such case too, the whole period of absence will be treated as EL.\nAt the end of the year, the balance will be adjusted against Accumulated / Earned Leave. If Accumulated / Earned Leave is also not available, then it will be treated as Leave on Loss of Pay (LOP).\nUnavailed Casual Leave will lapse automatically at the end of the year."
R_COMPENSATORYOFF ="1. Compensatory off can be sanctioned to an employee in lieu of having attended office on holidays.\n2. This leave can be combined with a holiday or casual leave, but the total of all these leaves taken at one time should not exceed 10 days.\n3. It the employee is required to attend duty on holidays or while on approved leave, they must register their attendance in the biometric system and the Compensatory leave should be credited on approval by the reporting authority.\n4. CO should be availed within 3 months from the date of performing duty on holidays otherwise the compensatory leave will lapse.\n5. CO will not be granted to any employee for conducting special classes and SRM IST Practical Examinations."
R_CASUALLEAVE ="1. All employees of the SRM IST are eligible to avail up to 12 days of Casual Leave in a year.\n2. One day CL will be credited on the first day of every month.\n3. Normally, one day of Casual Leave will be sanctioned to the probationary employee in a month.\n4. If CL is availed of more than one's available leave balance due to unforeseen circumstances, the leave account will show a minus balance. This shall be reconciled in the last month of the year.\n5. The total leave [including Public holidays / RH and Compensatory Leavel availed at a time should not exceed 10 days. \nIf the leave period exceeds 10 days, the whole period of absence will be treated as Earned Leave.If the eleventh day or subsequent day(s) happens to be holiday(s), in such case too, the whole period of absence will be treated as EL.\n6. At the end of the year, the balance will be adjusted against Accumulated / Earned Leave. If Accumulated / Earned Leave is also not available, then it will be treated as Leave on Loss of Pay (LOP).\n7. Unavailed Casual Leave will lapse automatically at the end of the year."
R_ONDUTY ="Employees are allowed to avail 'On Duty' for the duties attended outside.\nSRMIST that is assigned by the competent authority. A maximum of 10 days per year can be used for this purpose. Special cases are exempted subject to the approval of the authorities concerned. For 'On Duty' leave, individuals must apply through the portal."
R_VACATIONLEAVE ="Vacation Leave can be availed only during the vacation period. The vacation period will be declared by the Director/Dean of the faculty concered. This leave will be credited before the vacation period. VL should be applied well in advance and sanctioned by the authority before availing the same. Casual Leave, Earned Leave, Compensatory Leave, OD, etc., cannot be combined with Vacation Leave.\n(a) Faculty who has fully served for two semesters in an academic year is eligible to avail 60 days of vacation leave, including intervening holidays, in two spells fi.e. November - December and May - June]. If the faculty has served only one semester, he/she is eligible for 30 days of Vacation Leave. During November - December, the vacation leave will be restricted to 30 days at a time. If the service period is less than one semester, the VL will be calculated/sanctioned on a pro-rata basis. The Vacation Leave may be availed in two spells in each vacation with a minimum of 15 days.\n(b) Non-teaching academic staff member is also eligible for Vacation Leave of 15 days during probation (one year] on a pro-rata basis of 1.25 days per month and 30 days per year from 2nd year. This leave can be availed only during the vacation period, as declared by the Director/Dean."
R_ACCUMULATEDLEAVE ="50 percent of the unaviled vacation leave of a faculty and non-teaching academic staff will be treated as Accumulated Leave and credited at the end of the Leave cannot be claimed as a matter of right. For availing any kind of leave, obtaining prior permission from the competent authority is compulsory and leave shall be applied only through the Employee Portal. However, for availing any kind of leave except casual leave, it shall be applied in advance. In case of exigency, the discretionary powers to refuse, curtail or revoke the leave of any kind or to recall for duty any employee who is already on leave is reserved to the competent authority"
R_EARNEDLEAVE ="Every Administrative staff is eligible for Earned Leave of 15 days during the period of probation. On completion of the probation period, they are eligible for 30 days of Earned Leave per year. The leave will be credited on a pro-rata basis at the end of every month. Availing of half-a-day EL is not permitted. 50 percent of unavailed Earned Leave shall be carried over to next year's leave account subject to a maximum accumulation of 60 days"
R_MEDICALLEAVE ="Medical Leave exceeding two days at a spell will be granted only on production of a Medical Certificate. An Employee who has been granted Medical Leave shall resume duty after producing a certificate of fitness from a Registered Medical Practitioner. If the Medical Leave exceeds 7 days including holidays, the employee shall be referred to the Medical Board of SRM Medical College Hospital and Research Centre, if desired by the management.\nNo Medical Leave will be sanctioned to an employee during the probation period. After confirmation, all employees are eligible for (Nine) days of Medical Leave per year, which will be credited at the beginning of every year.\nThe ML can be accumulated for a maximum of 120 days in the entire period ot service."
R_ATTENDANCE="All employees need to follow the biometric-based attendance system. The attendance of a particular employee will be considered only based on the biometric system and leave applied in the system.\nThe working hours (IN and OUT time) of the SRMIST employees will vary based on the nature of the work and the operational requirements. 1. Compensatory off can be sanctioned to an employee in lieu of having attended office on holidays.\n2. This leave can be combined with a holiday or casual leave, but the total of all these leaves taken at one time should not exceed 10 days.\n3. It the employee is required to attend duty on holidays or while on approved leave, they must register their attendance in the biometric system and the Compensatory leave should be credited on approval by the reporting authority."
R_GENERALGUIDANCES="(a) During the Notice Period for resignation, no employee shall be allowed to avail any kind of leave at his/her credit. However, out of his/her credit leave. he/she can avail 5 days of leave during the notice period.\n(b) Notwithstanding anything contained in these rules, the authorities have their own discretion to sanction/refuse any kind of leave under special circumstances.\n(c) In view of the implementation of the above rules, the rules hitherto followed by different Faculties in different methods shall cease to be operative with effect from 01-01-2024."
R_TURNLEAVE="Non-teaching academic and Administrative staff is eligible for Turn Leave, and this leave can be availed every alternate Saturday.\nThis leave is not applicable for Employees of the Maintenance Department of all campuses, Estate offices and Attenders of all departments/ directorates."
R_LEAVEONLOSSOFPAY="Leave on Loss of Pay will be granted only on the merit of the case. The period of Leave on Loss of Pay will lead to the postponement of the annual increment."
R_PERMISSION="Every Faculty and Non-Teaching Academic/Administrative staff can avail one-hour permission either in the morning or in the evening on two occasions in a month.\nIf an employee avails permission both in the morning and evening on the same day, one day Casual Leave will be deducted."
R_RESTRICTEDHOLIDAY="Every employee is eligible for two days of Restricted Holiday irrespective of the religion and leave can be availed as per the list of Restricted Holidays and approved by the competent authority. RH can be combined with Casual Leave and Compensatory Leave."
R_MATERNITYLEAVE="Every female employee is eligible for Maternity Leave for 90 days after completing three years of continuous service. Maternity leave is allowed for only one living child. If the female employee is already having one child alive, she is not eligible for Maternity Leave. Employees who benefit from ES! will be sanctioned Maternity Leave as Leave on Loss of Pay."
R_LEAVEFORRESEARCHSCHOLARS ="1.1 Casual Leave\nOne day of casual leave for every month shall be provided to the Research\nScholars of SRMIST.\n1.2 Medical Leave\nThey are eligible for 9 days ML per year\n1.3 , Maternity Leave\nAs per the norms of SRMIST, Female Research Scholars are eligible for availing 240 days of Maternity Leave during the entire duration of their Ph.D. program.\n1.4 Turn Leave\nTL is not applicable to Research Scholars"
R_LEAVEPOLICYFORJRFSRFPROJECTFELLLOW ="2.1 Casual Leave\nOne day of casual leave for every month shall be provided to the JRF / SRF/\nProject Fellow of SRMIST.\n2.2 Medical Leave\nML is not eligible for the JRF / SRF/ Project Fellow.\n2.3 Maternity Leave\nNo Maternity leave for the JRF / SRF / Project Fellow.\nThe Project Fellow can avail his/her leave based on the conditions of the Project and consent of the Principal Investigator concerned for the particular Project.\n2.4 Turn Leave \nTL is not applicable for JRF/SRF/Project Fellow."
R_QUESTION1="If CL is availed of more than one's available leave balance due to unforeseen circumstances, the leave account will show a minus balance. This shall be reconciled in the last month of the year."
R_QUESTION2="You will be granted upto 10 days of leave continuously"
R_QUESTION3=""
R_QUESTION4="Unavailed casual leave will lapse automatically at the end of the year"
R_QUESTION5="This leave can be combined with a holiday or a casual leave.\n But the total of all these leaves taken at one time should not exceed 10 days"
R_QUESTION6="Compensatory off(CO)will not be granted to any employee for conducting special classes and SRMIST practical examinations"
R_QUESTION7="No,not more than 10 days of On duty would be provided.\n Special cases are exempted subject to the approval of authorities concerned"
R_QUESTION8="No,vacation leave cannot be availed in 3 spells it is available only at 2 spells if you have fully served for 2 semesters,if the faculty has served only one semester he is eligible for the vacation leave for one spell"
R_QUESTION9="Yes,an employee who has been granted medical leave shall resume duty after producing a certificate of fitness from registered medical practissioner"
R_QUESTION10="Restricted holiday can be combined with casual leaave and compensatory leave"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

@app.route("/")
def home():
    return render_template('index.html')


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        global highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Longer responseshi
    response('Hello!', ['hello', 'hi', 'hey'], single_response=True)
    response(long.R_TELL,['hey','there'],required_words=['hey'])

    response('I am fine!How are you',['how','are','you'],required_words=['how','you'])
    response('Nice to hear from you',['i','am','fine'],required_words=['fine'])
    response(long.R_NOTGOOD,['i','am','not','good'],required_words=['not','good    '])
    response(long.R_TASK,['what','do','you','do'],required_words=['what','you'])

    response(long.R_NAME,['what','is','your','name'],required_words=['your','name'])
    response(long.R_COLOR,['what','is','your','favourite','color'],required_words=['your','color'])
    response(long.R_AGE,['what','is','your','age'],required_words=['your','age'])
    response(long.R_SONG,['what','is','your','favourite','song'],required_words=['your','song'])
    response(long.R_FOOD,['what','is','your','favourite','food'],required_words=['your','food'])
    response(long.R_MOBILE,['what','is','your','favourite','mobile'],required_words=['your','mobile'])
    response(long.R_MADE,['what','are','you','made','of'],required_words=['made','what'])
    response(long.R_WORK,['how','do','you','work'],required_words=['work','you'])
    response('I was made by a group of 3 Members',['who','made','you'],required_words=['made','you'])
    response(long.R_HUMAN,['are','you','human'],required_words=['you','are','human'])
    response(long.R_APPRECIATE,['you','are','smart','clever','intelligent'],required_words=['you','are'])
    response(long.R_SMARTER,['do','you','get','smarter'],required_words=['smarter'])

    response('I live in your System',['where','you','live'],required_words=['you','live'])
    response(long.R_WHERE,['where','are','you','now'],required_words=['you','are'])
    response(long.R_NATIVE,['which','is','your','native'],required_words=['native'])
    response(long.R_MOBILE,['do','you','have','mobile'],required_words=['you','mobile'])

    response(long.R_THANK,['thank','thanks'],single_response=True)
    response(long.R_SORRY,['sorry'],single_response=True)
    response('How can i help you?',['help'],single_response=True)
    response('You are so polite',['you','are','welcome'],required_words=['welcome'])

    response(long.R_BORE,['i','am','bored'],required_words=['bored'])
    response(long.R_SCARED,['i','am','scared'],required_words=['scared'])
    response(long.R_HAPPY,['i','am','happy'],required_words=['happy'])
    response(long.R_SLEEPY,['i','am','feeling','sleepy'],required_words=['sleepy'])
    response(long.R_HUNGRY,['i','am,','feeling','hungry'],required_words=['hungry'])
    response(long.R_TIRED,['i','am','feeling','tired'],required_words=['tired'])
    response(long.R_ENERGETIC,['i','am','feeling','energetic'],required_words=['energetic'])

    response(long.R_NOTFEELING,['not','feeling','well'],required_words=['not','well'])
    response(long.R_FEVER,['i','have','fever'],required_words=['have','fever'])
    response(long.R_MEDICINES,['say','any','homemade','medicines','for','cold'],required_words=['homemade','medicines','cold'])

    response(long.R_NOGIFT,['i','have','no','money','for','gift'],required_words=['no','money','gift'])
    response(long.R_GIFTHUND,['i','have','planned','hundred','rupees','as','budget','for','gift'],required_words=['hundred','rupees','gift'])
    response(long.R_GIFTTHOU,['i','have','planned','thousand','rupees','as','budget','for','gift'],required_words=['thousand','rupees','gift'])
    response(long.R_GIFTTENTHOU,['i','have','planned','ten','thousand','rupees','as','budget','for','gift'],required_words=['ten','thousand','rupees','gift'])

 
    response(long.R_PIZZA,['order' , 'pizza'], required_words=['pizza'])
    response(long.R_DRINK, ['i', 'need', 'some', 'drink'], required_words=['i','need','drink'])  
    response(long.R_FOOD, ['prefer', 'me', 'a', 'food'], required_words=['prefer','food'])
    response(long.R_JUNK, ['junk', 'food'], required_words=['junk','food'])
    response(long.R_FAVFOOD, ['what', 'is', 'your', 'favorite', 'food'], required_words=['your','favorite','food'])
    response(long.R_FAVPLACE, ['what', 'is', 'your', 'favorite', 'place'], required_words=['your','favorite','place'])
    response(long.R_FAVMEDIA, ['what', 'is', 'your', 'favorite', 'social','media'], required_words=['your','favorite','social','media'])
    response(long.R_HOBBY, ['what', 'is', 'your', 'hobby'], required_words=['your','hobby'])
    response(long.R_FAVBOOK, ['what', 'is', 'your', 'favourite', 'book'], required_words=['your','favourite','book'])
    response(long.R_EXAM, ['i', 'have', 'exams'], required_words=['i','have','exam'])
    response(long.R_YOURSELF, ['say','about','your','self'], required_words=['your','self'])
    response(long.R_SCARES, ['what', 'scares', 'you'], required_words=['you','scares'])
    response(long.R_DO, ['what', 'can', 'you', 'do'], required_words=['what','you','do'])
    response(long.R_TRAVEL, ['can', 'you', 'travel'], required_words=['you','travel'])
    response(long.R_EMOTION, ['do', 'you', 'have', 'emotion'], required_words=['you','have','emotion'])
    response(long.R_YOUHAPPY, ['what', 'makes', 'you', 'happy'], required_words=['what','you','happy'])
    response(long.R_HUNGRY, ['are', 'you', 'hungry'], required_words=['you','hungry'])
    response(long.R_HELP, ['can', 'you', 'help'], required_words=['you','help'])
    response(long.R_CRY, ['can', 'you', 'cry'], required_words=['you','cry'])
    response(long.R_GIFT, ['can', 'you', 'gift'], required_words=['you','gift'])
    response(long.R_MONEY, ['can', 'you', 'give', 'some', 'money'], required_words=['give','money'])
    response(long.R_FUTURE, ['can', 'you', 'say', 'the', 'future'], required_words=['you','future'])
    response(long.R_BOSS, ['who', 'is', 'your', 'boss'], required_words=['your','boss'])
    response(long.R_SALARY,['what', 'is', 'your', 'salary'], required_words=['your','salary'])
    response(long.R_RICH, ['are', 'you', 'rich'], required_words=['are','you','rich'])
    response(long.R_POOR, ['how', 'poor', 'are', 'you'], required_words=['are','you', 'poor'])
    response(long.R_DEFENITION1, ['what','is','competent','authority'], required_words=['competent','authority'])
    response(long.R_DEFENITION2, ['who','are','employees'], required_words=['employees'])
    response(long.R_DEFENITION3, ['who','are','faculty','faculties'], required_words=['faculty'])
    response(long.R_DEFENITION4, ['who','are','non','-','teaching','academic','staff'], required_words=['academic','staff'])
    response(long.R_DEFENITION5, ['who','are','non','-','teaching','administrative','staff'], required_words=['administrative',])
    response(long.R_DEFENITION6, ['what','is','an','year'], required_words=['year'])
    response(long.R_EXTENTOFAPPLICATION, ['what','is','extent','of','application'], required_words=['extent'])
    response(long.R_RIGHTTOAVAILLEAVE, ['what','is','right','to','avail','leave'], required_words=['avail'])
    response(long.R_CASUALLEAVE, ['what','are','the','rules','and','details','to','apply','casual'], required_words=['casual'])
    response(long.R_ONDUTY, ['what','is','on','duty','what','are','the','rules','to','apply','on','duty'], required_words=['on'])
    response(long.R_VACATIONLEAVE, ['what','is','vacation','leave','what','are','the','rules','for','applying','vacation','leave'], required_words=['vacation'])
    response(long.R_ACCUMULATEDLEAVE, ['what','is','accumulated','leave','what','are','the','rules','to','apply','accumulated','leave'], required_words=['accumulated'])
    response(long.R_EARNEDLEAVE, ['what','is','earned','leave','what','are','rules','to','apply','earned','leave'], required_words=['earned'])
    response(long.R_MEDICALLEAVE, ['what','is','medical','leave','are','the','rules','to','apply','medical','leave'], required_words=['medical'])
    response(long.R_ATTENDANCE, ['what','is','attendance'], required_words=['attendance'])
    response(long.R_GENERALGUIDANCES, ['what','are','general','guidances'], required_words=['general','guidances'])
    response(long.R_TURNLEAVE, ['what','is','turn','leave'], required_words=['turn'])
    response(long.R_LEAVEONLOSSOFPAY, ['what','is','on','loss','of','pay'], required_words=['loss','of','pay'])
    response(long.R_PERMISSION, ['what','is','permission'], required_words=['permission'])
    response(long.R_RESTRICTEDHOLIDAY, ['what','is','restricted','holiday'], required_words=['restricted'])
    response(long.R_MATERNITYLEAVE, ['what','is','maternity','what','are','the','rules','to','apply',], required_words=['maternity'])
    response(long.R_LEAVEFORRESEARCHSCHOLARS, ['what','are','the','procedures','for','research','scholars'], required_words=['reseach'])
    response(long.R_LEAVEPOLICYFORJRFSRFPROJECTFELLLOW, ['what','are','the','policy','and','policies','for','srf','jrf','project','fellows'])
    response(long.R_LEAVE, ['what','is','leave'], required_words=['leave'])
    response(long.R_QUESTION1, ['my','casual','count','is','zero','may','i','avail','casua','leave','now','?'])
    response(long.R_QUESTION2, ['how','many','leaves','can','i','take','continuosly'])
    response(long.R_QUESTION3, ['what','is','the','procedure','to','join','after','taking','a','long','leave'])
    response(long.R_QUESTION4, ['is','unavailed','casual','leave','will','be','carried','to','next','year'])
    response(long.R_QUESTION5, ['may','i','combine','compensatory','off','with','casual','leave','or','accumulated','leave'])
    response(long.R_QUESTION6, ['i','have','conducted','a','special','class','for','students','may','i','avail','compensatory','off','for','that'])
    response(long.R_QUESTION7, ['i','am','involved','in','more','academic','duties','is','it','possible','to','get','more','than','10','days','of','on','duty'])
    response(long.R_QUESTION8, ['may','i','avail','vacation','leave','in','3','spells'] )
    response(long.R_QUESTION9, ['is','admission','in','hospital','is','mandatory','to','avail','medical','leave'])
    response(long.R_QUESTION10, ['may','i','take','restricted','holiday','along','with','casual','leave'])
    
   


    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

@app.route("/process_chat_input", methods=['POST'])
def process_chat_input():
    try:
        # Get the user's message from the POST request
        user_message = request.form.get('user_message').lower()

        # Process the user's message
        response = check_all_messages(user_message)

        # Print the response for debugging
        print("Bot Response:", response)

        # Return the response as JSON
        return jsonify({"response": response})

    except Exception as e:
        # Handle any errors and return an error response
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)