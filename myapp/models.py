
from django.db import models
from django.forms.widgets import Widget
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings
from django.db import models
from embed_video.fields import EmbedVideoField

class Mentor_TV(models.Model):
    Headline = models.CharField(max_length = 20)
    video = EmbedVideoField()  # same like models.URLField()


# Create your models here.
class Contact(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	subject = models.CharField(max_length = 60)
	email_address = models.EmailField(max_length = 150)
	message = models.TextField(help_text='Write here your message!')

	def __str__(self):
		return self.first_name+" wants to contact you"

# class SubscribeModel(models.Model):
#     sys_id = models.AutoField(primary_key=True, null=False, blank=True)
#     email = models.EmailField(null=False, blank=True, max_length=200, unique=True)
#     status = models.CharField(max_length=64, null=False, blank=True)
#     created_date = models.DateTimeField(null=False, blank=True)
#     updated_date = models.DateTimeField(null=False, blank=True)

#     class Meta:
#         app_label = "myapp"
#         db_table = "myapp_subscribe"

#     def __str__(self):
#         return self.email
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    conf_num = models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        #return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"
        return self.email + " (" + str(self.confirmed) + ")"

class Newsletter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    contents = models.FileField(upload_to='media/')

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")

    def send(self, request):
        contents = self.contents.read().decode('utf-8')
        subscribers = Subscriber.objects.filter(confirmed=True)
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        for sub in subscribers:
            message = Mail(
                    from_email=settings.FROM_EMAIL,
                    to_emails=sub.email,
                    subject=self.subject,
                    html_content=contents + (
                        '<br><a href="{}?email={}&conf_num={}">Unsubscribe</a>.').format(
                            request.build_absolute_uri('/delete/'),
                            sub.email,
                            sub.conf_num))
            sg.send(message)


from django.urls import  reverse

class MTV_Category(models.Model):
    name=models.CharField(max_length=150,db_index=True)
    slug=models.SlugField(unique=True)
    class Meta:
        ordering=('-name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('myapp:MTV_by_category', args=[self.slug])

class Mentor_TV2(models.Model):
    category=models.ForeignKey(MTV_Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    body=models.TextField(db_index=True,blank=True)
    #footer=models.TextField(blank=True)
    video = EmbedVideoField()  # same like models.URLField()
    publish=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=('-publish',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
       return reverse('myapp:MTV_Details',args=[self.id,])
