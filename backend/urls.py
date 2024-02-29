from django.urls import path
from backend import views

urlpatterns = [
    path('green_main_view/',views.green_main_view,name="green_main_view"),
    path('add_single/',views.add_single,name="add_single"),
    path('post_single/',views.post_single,name="post_single"),
    path('single_table/',views.single_table,name="single_table"),
    path('single_update/<int:c_id>',views.single_update,name="single_update"),
    path('single_edit/<int:c_id>', views.single_edit, name="single_edit"),
    path('single_delete/<int:c_id>',views.single_delete,name="single_delete"),


    path('state_view/',views.state_view,name="state_view"),
    path('add_state/',views.add_state, name='add_state'),
    path('city_view/',views.city_view,name="city_view"),
    path('add_city/',views.add_city, name='add_city'),

]
