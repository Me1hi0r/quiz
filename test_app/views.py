from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Test, Question

from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

from .models import MyUser, Question, Test
from .utils import account_activation_token


def redir(request):
    return redirect('login')

@login_required(login_url="/login")
def test_list(request):
    tests = Test.objects.all()
    context = {
        'tests': tests,
    }
    return render(request, 'test_app/test.html', context)


class QuizView(View):
    def get(self, request, id):
        test = Test.objects.get(pk=id)
        name = test.test_name

        attempts = request.session.get(name, 0)
        if attempts > test.max_attepts:
            context = {
                'text': 'You have no attempts left, please choose another test.'
            }
            return render(request, 'test_app/result.html', context)
        request.session[f'{name}_score'] = 0

        request.session[f'{name}_quest'] = 1
        request.session[name] = attempts+1

        quest = request.session.get(f'{name}_quest')
        quest_all = test.question.all().count()
        progres_text = f'Question {quest} of {quest_all}'
        qst = test.question.all()[quest - 1]

        context = {
            'progress': progres_text,
            'question': qst,
            'choice1': qst if qst.used_1 else False,
            'choice2': qst if qst.used_2 else False,
            'choice3': qst if qst.used_3 else False,
            'choice4': qst if qst.used_4 else False,
            'choice5': qst if qst.used_5 else False,
        }

        return render(request, 'test_app/quiz.html', context)
    
    def post(self, request, id):
        test = Test.objects.get(pk=id)
        name = test.test_name
        request.session[f'{name}_quest'] += 1
        score = request.session.get(f'{name}_score')
    
        quest = request.session.get(f'{name}_quest')
        quest_all = test.question.all().count()

        if quest > quest_all:
            attempts = request.session[name]
            if test.pass_point < score:
                text = f'Congratulations, you passed\
                     the test on {attempts} try.'
            else:
                text = f'You have not passed the test.\
                    You have {test.max_attepts + 1 - attempts} attempts left.'

            score_text = f'Your result is {score} points.'
            context = {
                'text': text, 
                'score': score_text,
            }
            return render(request, 'test_app/result.html', context)

        if quest <= quest_all:
            choiced_answers_numb = \
                [int(x) for x in list(request.POST) if x.isdigit()]
            qst = test.question.all()[quest - 1]
            for numb in choiced_answers_numb:
                if getattr(qst, f'right_{numb}'):
                    score += getattr(qst, f'points_{numb}')
            request.session[f'{name}_score'] = score

            progres_text = f'Question {quest} of {quest_all}'
            context = {
                'progress': progres_text,
                'question': qst,
                'choice1': qst if qst.used_1 else False,
                'choice2': qst if qst.used_2 else False,
                'choice3': qst if qst.used_3 else False,
                'choice4': qst if qst.used_4 else False,
                'choice5': qst if qst.used_5 else False,
            }
            return render(request, 'test_app/quiz.html', context)


class RegistrationView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        usermail = request.POST['email']
        password = request.POST['password']

        user = MyUser.objects.create_user(username=usermail)
        user.set_password(password)
        user.is_active = False
        user.save()

        current_site = get_current_site(request)
        email_body = {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        }

        link = reverse('activate', kwargs={
                       'uidb64': email_body['uid'], 'token': email_body['token']})

        email_subject = 'Activate your account'
        email_body = f'Hi {user.username}, Please the\
             link below to activate your account \
            \nhttp://{current_site.domain}{link}'

        email = EmailMessage(
            email_subject,
            email_body,
            'noreply@semycolon.com',
            [usermail],
        )
        email.send(fail_silently=False)

        messages.success(request, 'Account successfully created. Please check your email')
        return render(request, 'register.html')


class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = MyUser.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login'+'?message='+'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')

        except Exception as ex:
            pass

        return redirect('login')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome, ' +
                                     user.username+' you are now logged in')
                    return redirect('/test/')
                messages.error(
                    request, 'Account is not active,please check your email')
                return render(request, 'login.html')
            messages.error(
                request, 'Invalid credentials, try again')
            return render(request, 'login.html')

        messages.error(
            request, 'Please fill all fields')
        return render(request, 'login.html')


def log_out(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')
