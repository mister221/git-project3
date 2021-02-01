from django.urls import path

from . import views

from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [

		path('home/',views.home,name='home'),
		path('<int:id>/',views.home,name='update'),
		path('delete/<int:id>/',views.deleteEntry,name='delete_entry'),
		path('login/',LoginView.as_view(template_name='tasks/login.html'),name='login'),
		path('logout/',LogoutView.as_view(),name='logout'),

]