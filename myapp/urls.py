from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# from .views import CourseListView
app_name = 'myapp'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('Contact/',views.contact,name='contact'),
    path('new/', views.new, name='new'),
    path('confirm/', views.confirm, name='confirm'),
    path('delete/', views.delete, name='delete'),
    # path('Mentor-Tv/', views.mentor_tv, name='mentor_tv'),

    path('Mentor-Tv/', views.MTV_Catergory_List, name='Category_list'),
    path('<slug:category_slug>', views.MTV_Catergory_List, name='MTV_by_category'),
    path('<int:id>/', views.MTV_Detail, name='MTV_Details'),

    # path('', CourseListView.as_view(), name='course_list'),

    # path('subscribe/', views.subscribe, name='subscribe'),
    # path('subscribe/confirm/', views.subscription_confirmation, name='subscription_confirmation'),
    # #path(r'unsubscribe/', views.unsubscribe, name='unsubscribe'),

    # path('ATS/',views.ATS_HomePage1,name='ATS'),
    # path('Demo/',views.Demo,name='demo'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)