from django.conf.urls import url
from basic_app import views
from django.conf import settings
from django.conf.urls.static import static
# SET THE NAMESPACE!
app_name = 'basic_app'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_DIR)
    
