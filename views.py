from django.shortcuts import render
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from .tf import tf

from .models import *
import xlrd


# Create your views here.
def home(request):
    return render(request, 'index.html')


def signupdef(request):
    return render(request, 'signup.html')


def userlogindef(request):
    return render(request, 'user.html')


def userloginactiondef(request):
    if request.method == 'POST':
        uid = request.POST['mail']
        pwd = request.POST['pwd']
        d = onlineuser.objects.filter(email__exact=uid).filter(pwd__exact=pwd).count()

        if d > 0:
            d = onlineuser.objects.filter(email__exact=uid)
            name = ""
            for d1 in d:
                name = d1.name

            request.session['email'] = uid
            request.session['name'] = name
            return render(request, 'user_home.html', {'dat a': d[0]})

        else:
            return render(request, 'user.html', {'msg': "Login Fail"})

    else:
        return render(request, 'user.html')


def usignupactiondef(request):
    email = request.POST['email']
    ph = request.POST['ph']
    pwd = request.POST['pwd']
    name = request.POST['name']
    gen = request.POST['gen']

    d = onlineuser.objects.filter(email__exact=email).count()
    if d > 0:
        return render(request, 'signup.html', {'msg': "Email Already Registered"})

    else:
        d = onlineuser(name=name, email=email, pwd=pwd, gender=gen, phone=ph)
        d.save()
        return render(request, 'signup.html', {'msg': "Registration Success, You can Login.."})


def userhomedef(request):
    if "email" in request.session:
        uid = request.session["email"]
        d = onlineuser.objects.filter(email__exact=uid)
        return render(request, 'user_home.html', {'data': d[0]})

    else:
        return render(request, 'user.html')


def userlogoutdef(request):
    try:
        del request.session['email']
    except:
        pass
    return render(request, 'user.html')


def adminlogin(request):
    return render(request, 'admin.html')


def adminloginaction(request):
    userid = request.POST['aid']
    pwd = request.POST['pwd']
    print(userid, pwd, '< <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    if userid == 'admin' and pwd == "admin":
        request.session['adminid'] = 'admin'
        return render(request, 'adminhome.html')
    else:
        err = ' Your Login Data is wrong !!'
        return render(request, 'admin.html', {' msg': err})


def adminhome(request):
    return render(request, 'adminhome.html')


def adminlogout(request):
    return render(request, 'admin.html')


def datasetpage(request):
    return render(request, 'datasetpage.html')


def classification(request):
    return render(request, 'classification.html')


def nbtrain(request):
    
    from .Training import Training
    sc = Training.train(1)

    performance.objects.filter(alg_name='Naive Bayes').delete()
    
    d = performance(alg_name='Naive Bayes', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
    d.save()
    
    return render(request, 'classification.html', {'msg': "Naive Bayes Algorithm's training completed"})


def dttrain(request):
    from .Training import Training
    sc = Training.train(4)

    performance.objects.filter(alg_name='Decision Tree').delete()
    
    d = performance(alg_name='Decision Tree', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
    d.save()
    
    return render(request, 'classification.html', {'msg': "Decision Tree Algorithm's training completed"})


def svmtrain(request):
    from .Training import Training
    sc = Training.train(3)
    performance.objects.filter(alg_name='SVM').delete()
  
    d = performance(alg_name='SVM', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
    d.save()

    return render(request, 'classification.html', {'msg': "SVM Algorithm's training completed"})


def nntrain(request):
    from .Training import Training
    sc = Training.train(2)
    performance.objects.filter(alg_name='Neural Networks').delete()
    d = performance(alg_name='Neural Networks', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
    d.save()

    return render(request, 'classification.html', {'msg': "Neural Networks Algorithm's training completed"})


def rftrain(request):
    from .Training import Training
    sc = Training.train(5)
    performance.objects.filter(alg_name='Random Forest').delete()
    d = performance(alg_name='Random Forest', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])

    d.save()

    return render(request, 'classification.html', {'msg': "Random Forest Algorithm's training completed"})


def evaluation(request):
    d = performance.objects.all()
    val = dict({})
    for d1 in d:
        val[d1.alg_name] = d1.sc1
    from .Graphs import viewg
    try:
        viewg(val)
    except:
        pass
    return render(request, 'viewacc.html', {'data': d})




def uploaddataset(request):
    if "adminid" in request.session:

        return render(request, 'uploaddataset.html')

    else:
        return render(request, 'adminlogin.html')

def uploadaction(request):
    if "adminid" in request.session:
        file = 'Questions.csv'
        file2 = 'Answers.csv'
        import csv
        d = Questions.objects.all().delete()
        d = Answers.objects.all().delete()
        with open(file, 'r') as fin:
            dr = csv.DictReader(fin)  # comma is default delimiter
            to_db = [(i['Qid'], i['Question']) for i in dr]
            for l in to_db:
                d = Questions(qid=l[0], Question=l[1])
                d.save()
        with open(file2, 'r') as fin:
            dr = csv.DictReader(fin)  # comma is default delimiter
            to_db = [(i['Qid'], i['Response']) for i in dr]
            for l in to_db:
                d = Answers(qid=l[0], Answer=l[1])
                d.save()

        return render(request, 'uploaddataset.html', {'msg': "Datasets Uploaded Successfully"})

    else:
        return render(request, 'adminlogin.html')




def chatstore(user, msg):
    d = chat(name=user, email=user, message=msg)
    d.save()



def chatpage(request):
    
    chat.objects.all().delete()
    try:
        del request.session['prediction']
        del request.session['clss']
        del request.session['res']
    
    except:
        pass
            
    d=chat.objects.filter().all()
    return render(request, 'chatpage.html',{'data': d})


anxiety=["I'm sorry, you're suffering from anxiety", "Anxiety can be a challenging condition to deal with, but there are treatment options available that can help you manage it", "It's important to remember that everyone's experience with anxiety is unique, and what works for one person may not work for another. It's recommended to consult with a healthcare professional who can provide personalized advice and guidance based on your specific situation."]
depression=["I'm sorry, you're suffering from depression.", "Depression is a serious mood disorder that can have a significant impact on your daily life. It's important to seek help and support to manage your symptoms."]
loneliness=["I'm sorry, you're suffering from loneliness", "Remember, it's important to be patient with yourself and understand that building connections takes time. By taking proactive steps and seeking support, you can effectively cope with loneliness and improve your overall well-being."]
stress=["I'm sorry, you're suffering from stress", "Take deep breaths, stretch, or meditate: These relaxation techniques can help calm your mind and reduce stress levels."]
normal=["Don't worry, just relax. Your are normal.. "]



def chataction(request):
    message=request.POST['chat']
    uemail=request.session["email"]
    uname=request.session["name"]
    d=chat(name='user',email=uemail,message=message)
    d.save()
    hi=['hi', 'hello', 'hi there','hey']

    message=message.lower()

    if message in hi:
        d=chat(name='chatbot',email=uemail,message='Hi.. ')
        d.save()

        try:
            del request.session['prediction']
            del request.session['clss']
            del request.session['res']
        
        except:
            pass




        d=chat.objects.filter().all()
        return render(request, 'chatpage.html',{'data': d})

    if "prediction" in request.session:
        message=message.lower()
        message=message.strip()
        
        if message=='yes':message=1
        else:message=0

        dct=request.session['res']
        print(dct,'*******************')
        
        #
        case=True

        for d1 in dct.keys():
            
            if case:
                if dct[d1]=='non':
                    dct[d1]=message
                    case=False

                
        
        print(dct,'&&&&&&&&&&&&&&&&&&&&&&&&&&&&',list(dct.values()))
            
        
        if 'non' in list(dct.values()):
            for d1 in dct.keys():
                print(dct[d1],'<<<<<<<<<<<<<<<<')
                if dct[d1] == 'non':
                    s=d1.replace('.',' ')
                    msg='Are you '+str(s)+' ? (Yes or No)'
                    d=chat(name='chatbot',email='chatbot',message=msg)
                    d.save()
                    break
            request.session['res'] = dct
            d=chat.objects.filter().all()
            return render(request, 'chatpage.html',{'data': d})


        else:
            labels=request.session['clss']
            c=list(dct.values())
            from .Prediction import predict
            res=predict(labels,c)
            msg=''
            print(res,'>>>>>>>>>>>>>>>>>>>>>>>>>')
            if res=='Normal':
                for m in normal:
                    d=chat(name='chatbot',email='chatbot',message=m)
                    d.save()
            
                
            elif res=='Anxiety':
                for m in anxiety:
                    d=chat(name='chatbot',email='chatbot',message=m)
                    d.save()
            
            elif res=='Depression':
                for m in depression:
                    d=chat(name='chatbot',email='chatbot',message=m)
                    d.save()
            
            elif res=='Loneliness':
                for m in loneliness:
                    d=chat(name='chatbot',email='chatbot',message=m)
                    d.save()
            
            elif res=='Stress':
                for m in stress:
                    d=chat(name='chatbot',email='chatbot',message=m)
                    d.save()
            

                
            d=chat.objects.filter().all()
            return render(request, 'chatpage.html',{'data': d})

            del request.session['prediction']
            del request.session['clss']
            del request.session['res']
            
    ans='Sorry, Not Understood'

    cid=tf.calc(message)
    if cid!=-1:
        from .FeatureSelection import featureselection
        clss=featureselection.calc()
        
        d={clss[0]:'non',clss[1]:'non',clss[2]:'non',clss[3]:'non',clss[4]:'non',clss[5]:'non',clss[6]:'non',clss[7]:'non',clss[8]:'non'}
        
        request.session['clss'] = clss
        request.session['res'] = d
        request.session['prediction'] = True
        s=clss[0].replace('.',' ')

        msg='Are you '+str(s)+' ? (Yes or No)'
        
        d=chat(name='chatbot',email='chatbot',message=msg)
        d.save()
        

        d=chat.objects.filter().all()
        return render(request, 'chatpage.html',{'data': d})
   
    else:
        d=chat(name='chatbot',email='chatbot',message=ans)
        d.save()

        d=chat.objects.filter().all()
        return render(request, 'chatpage.html',{'data': d})
                    




            