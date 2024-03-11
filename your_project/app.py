from flask import Flask, render_template, request, jsonify
import re
import response as long

app = Flask(__name__)
conversation_context = {"history": []}


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = sum(word in user_message for word in recognised_words)

    percentage = (message_certainty / len(recognised_words)) if len(recognised_words) > 0 else 0

    has_required_words = all(word in user_message for word in required_words)

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}


    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        certainty = message_probability(message, list_of_words, single_response, required_words)
        print(f"Response: {bot_response}, Certainty: {certainty}")
        highest_prob_list[bot_response] = certainty

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
    response(long.R_MATERNITYLEAVE, ['what','is','maternity','what','are','the','rules','to','apply','maternity leave'], required_words=['maternity','leave','maternit leave'])
    response(long.R_LEAVEFORRESEARCHSCHOLARS, ['what','are','the','procedures','for','research','scholars'], required_words=['reseach'])
    response(long.R_LEAVEPOLICYFORJRFSRFPROJECTFELLLOW, ['what','are','the','policy','and','policies','for','srf','jrf','project','fellows'])
    response(long.R_LEAVE, ['what','is','leave','i wanna take leave', 'i wanna avail'], required_words=['leave'])
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
    print(f"Best Match: {best_match}")
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match
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

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
