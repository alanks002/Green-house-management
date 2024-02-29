from django.urls import path
from frontend import views


urlpatterns=[
     path('main_view/',views.main_view,name="main_view"),
     path('login_view/',views.login_view,name="login_view"),
     path('userlogout/',views.userlogout,name="userlogout"),
     path('user_sigin_in_post/',views.user_sigin_in_post,name="user_sigin_in_post"),
     path('sign_up_save/',views.sign_up_save,name="sign_up_save"),
     path('service_view/',views.service_view,name="service_view"),
     path('single_service/<int:g_id>',views.single_service,name="single_service"),
     path('contact_view/',views.contact_view,name="contact_view"),
     path('contact_save/',views.contact_save,name="contact_save"),
     path('booking_view/',views.booking_view,name="booking_view"),
     path('booking_save/',views.booking_save,name="booking_save"),

     path('about_view/',views.about_view,name="about_view"),
     path('project_view/',views.project_view,name="project_view"),
     path('success/',views.success,name="success"),

     path('blog_view/',views.blog_view,name="blog_view"),
     path('forgot_password/',views.forgot_password,name="forgot_password"),

     path('change_password/<str:token>/', views.change_password, name='change_password'),
     path('verification/', views.verification, name='verification'),


]