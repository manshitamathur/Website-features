# Create your views here.
import django
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib import messages
from django.urls import reverse
from . import validation_utility
# from .models import SubscribeModel
import time
import logging
from django.core.exceptions import ObjectDoesNotExist
import traceback
from . import utility
from django.template.response import TemplateResponse
from . import email_utility

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber,Mentor_TV
from .forms import SubscriberForm
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail



# def contact(request):
# 	if request.method == 'POST':
# 		form = ContactForm(request.POST)
# 		if form.is_valid():
# 			subject = "Website Inquiry" 
# 			body = {
# 			'first_name': form.cleaned_data['first_name'], 
# 			'last_name': form.cleaned_data['last_name'], 
# 			'email': form.cleaned_data['email_address'], 
# 			'message':form.cleaned_data['message'], 
# 			}
# 			message = "\n".join(body.values())

# 			# try:
#             #     sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
#             #     response = sg.send(message)

#             try:
#                 sg=SendGridAPIClient(settings.SENDGRID_API_KEY)
#                 response = sg.send(message)
# 				# send_mail(subject, message, 'rekhasadhwani1718@gmail.com', ['manshitamathur@gmail.com']) 
# 			except BadHeaderError:
# 				return HttpResponse('Invalid header found.')
# 	        return render(request, "contact.html")

      
# 	form = ContactForm()
# 	return render(request, "contact.html", {'form':form})

# def contact(request):
# 	if request.method == 'POST':
# 		form = ContactForm(request.POST)
# 		if form.is_valid():
#             message = Mail(
# 			    from_email=settings.FROM_EMAIL,
# 			    to_emails='rekhasadhwani1718@gmail.com',
# 			    subject = "Website Inquiry" ,
# 			    body = {
# 			'first_name': form.cleaned_data['first_name'], 
# 			'last_name': form.cleaned_data['last_name'], 
# 			'email': form.cleaned_data['email_address'], 
# 			'message':form.cleaned_data['message'], 
# 			})
												
# 			# try:
# 			#     sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
# 			#     response = sg.send(message)

# 			try:
# 				sg=SendGridAPIClient(settings.SENDGRID_API_KEY)
# 				response = sg.send(message)
# 				# send_mail(subject, message, 'rekhasadhwani1718@gmail.com', ['manshitamathur@gmail.com']) 
# 			except BadHeaderError:
# 				return HttpResponse('Invalid header found.')
# 			return render(request, "contact.html")

			
# 	form = ContactForm()
# 	return render(request, "contact.html", {'form':form})
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			message = Mail(
				from_email=settings.FROM_EMAIL,
				to_emails='rekhasadhwani1718@gmail.com',
				subject='Website Enquirey',
				html_content = 'Name: {} {}\n Email: {}\n Message: {}\n'.format(form.cleaned_data['first_name'],  form.cleaned_data['last_name'], form.cleaned_data['email_address'],form.cleaned_data['message']))
					
				# try:
				#     sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
				#     response = sg.send(message)
			sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
			response = sg.send(message)
					# send_mail(subject, message, 'rekhasadhwani1718@gmail.com', ['manshitamathur@gmail.com']) 
			    # except BadHeaderError:
                #     return HttpResponse('Invalid header found.')
			messages.success(request,'Form submitted successfully!')
			return  TemplateResponse(request, "contact.html", {'form': ContactForm()})

				
	form = ContactForm()
	return render(request, "contact.html", {'form':form})





# def subscribe(request):
#     if request.method == 'POST':
#         post_data = request.POST.copy()
#         email = post_data.get("email", None)

#         error_msg = validation_utility.validate_email(email)
#         if error_msg:
#             messages.error(request, error_msg)
#             return HttpResponseRedirect(reverse('myapp:subscribe'))
#         save_status = save_email(email)

#         if save_status:
#             token = utility.encryption_util.encrypt(email + constants.SEPARATOR + str(time.time()))
#             subscription_confirmation_url = HttpResponse.request.build_absolute_uri(
#                 reverse('myapp:subscription_confirmation')) + "?token=" + token
#             status = email_utility.send_subscription_email(email, subscription_confirmation_url)
#             if not status:
#                 SubscribeModel.objects.get(email=email).delete()
#                 logging.getLogger("info").info(
#                     "Deleted the record from Subscribe table for " + email + " as email sending failed. status: " + str(
#                         status))
#             else:
#                 msg = "Mail sent to email Id '" + email + "'. Please confirm your subscription by clicking on " \
#                                                         "confirmation link provided in email. " \
#                                                         "Please check your spam folder as well."
#                 messages.success(request, msg)
#         else:
#             msg = "Some error occurred. Please try in some time. Meanwhile we are looking into it."
#             messages.error(request, msg)

#     # return HttpResponseRedirect(reverse('myapp:subscribe'))
#     return render(request,'subscribe.html')

    
# def save_email(email):
#     try:
#         subscribe_model_instance = SubscribeModel.objects.get(email=email)
#     except ObjectDoesNotExist as e:
#         subscribe_model_instance = SubscribeModel()
#         subscribe_model_instance.email = email
#     except Exception as e:
#         logging.getLogger("error").error(traceback.format_exc())
#         return False

#     # does not matter if already subscribed or not...resend the email
#     # subscribe_model_instance.status = constants.SUBSCRIBE_STATUS_SUBSCRIBED
#     subscribe_model_instance.created_date = utility.now()
#     subscribe_model_instance.updated_date = utility.now()
#     subscribe_model_instance.save()
#     return True

# def subscription_confirmation(request):
#     if "POST" == request.method:
#         raise Http404

#     token = request.GET.get("token", None)

#     if not token:
#         logging.getLogger("warning").warning("Invalid Link ")
#         messages.error(request, "Invalid Link")
#         return HttpResponseRedirect(reverse('appname:subscribe'))

#     token = utility.encryption_util.decrypt(token)
#     if token:
#         token = token.split(constants.SEPARATOR)
#         email = token[0]
#         print(email)
#         initiate_time = token[1]  # time when email was sent , in epoch format. can be used for later calculations
#         try:
#             subscribe_model_instance = SubscribeModel.objects.get(email=email)
#             subscribe_model_instance.status = constants.SUBSCRIBE_STATUS_CONFIRMED
#             subscribe_model_instance.updated_date = utility.now()
#             subscribe_model_instance.save()
#             messages.success(request, "Subscription Confirmed. Thank you.")
#         except ObjectDoesNotExist as e:
#             logging.getLogger("warning").warning(traceback.format_exc())
#             messages.error(request, "Invalid Link")
#     else:
#         logging.getLogger("warning").warning("Invalid token ")
#         messages.error(request, "Invalid Link")

#     return HttpResponseRedirect(reverse('myapp:subscribe'))



# Helper Functions
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)

@csrf_exempt
def new(request):
    if request.method == 'POST':
        sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
        sub.save()
        message = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=sub.email,
            subject='Newsletter Confirmation',
            html_content='Thank you for signing up for my email newsletter! \
                Please complete the process by \
                <a href="{}?email={}&conf_num={}"> clicking here to \
                confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
                                                    sub.email,
                                                    sub.conf_num))
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return render(request, 'index.html', {'email': sub.email, 'action': 'added', 'form': SubscriberForm()})
    else:
        return render(request, 'index.html', {'form': SubscriberForm()})

def confirm(request):
    print("hello")
    
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()

        return render(request, 'index.html', {'email': sub.email, 'action': 'confirmed'})
    else:
        return render(request, 'index.html', {'email': sub.email, 'action': 'denied'})

def delete(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.delete()
        return render(request, 'index.html', {'email': sub.email, 'action': 'unsubscribed'})
    else:
        return render(request, 'index.html', {'email': sub.email, 'action': 'denied'})

def mentor_tv(request):
    mtvs = Mentor_TV.objects.all()
    return render(request,"Mentor_Tv.html",{'mtvs':mtvs})

# from django.views.generic.detail import DetailView
# class CourseDetailView(DetailView):
#     model = Mentor_TV
#     template_name = 'courses/course/detail.html'

# class CourseListView(TemplateResponseMixin, View):
#     model = Mentor_TV
#     template_name = 'courses/course/list.html'

from .models import Mentor_TV2,MTV_Category
from django.shortcuts import get_object_or_404

# Create your views here.
def MTV_Catergory_List(request,category_slug=None):
	category = None
	categories = MTV_Category.objects.all()
	mtvs = Mentor_TV2.objects.all()
	if category_slug:
		category = get_object_or_404(MTV_Category,slug=category_slug)
		mtvs = mtvs.filter(category=category)
	return render(request, 'MTV_List.html', {'categories':categories,
											  'category':category,
											  'mtvs':mtvs,
											  })

def MTV_Detail(request,id):
	mtv=get_object_or_404(Mentor_TV2,id=id)
	return render(request,'story_detail.html',{'mtv':mtv})


