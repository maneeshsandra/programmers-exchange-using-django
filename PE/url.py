from django.urls import path
from PE import views
urlpatterns=[
    path('',views.home,name='home'),
    path('index',views.home,name='home'),
    path('easy',views.Easy.as_view(),name='easy'),
    path('medium',views.Medium.as_view(),name='medium'),
    path('hard',views.Hard.as_view(),name='hard'),
    path('contribute',views.contribute,name='contribute'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('problems',views.problems,name='problems'),
    path('action',views.action,name='action'),
    path('detail',views.detail,name='detail'),
    path('detail/<slug:pk>/',views.DetailView.as_view(),name='detail')
]