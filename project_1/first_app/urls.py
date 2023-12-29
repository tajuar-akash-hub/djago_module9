
from django.urls import path
# from views import contact
from . import views  


urlpatterns = [
    
    
    path('courses/',views.course),
    path('about/',views.about),
    path("",views.home),
    


]