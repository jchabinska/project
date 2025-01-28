from django.urls import path
from . import views
from .views import (
    OsobaList, OsobaDetail, OsobaUpdateView, OsobaDeleteView,
    StanowiskoList, StanowiskoDetail, StanowiskoMembersView,
    OsobaView
)

urlpatterns = [
    path('osoby/', OsobaList.as_view(), name='osoba-list'), 
    path('osoby/<int:pk>/', OsobaDetail.as_view(), name='osoba-detail'),  
    path('osoba/<int:pk>/update/', OsobaUpdateView.as_view(), name='osoba-update'),  
    path('osoba/<int:pk>/delete/', OsobaDeleteView.as_view(), name='osoba-delete'),  
    path('osoba/<int:pk>/', views.person_view, name='person_view'),
    path('osoby/', OsobaView.as_view(), name='osoba_view'),

    path('persons/', views.person_list, name='person-list'),  
    path('persons/<int:pk>/', views.person_detail, name='person-detail'),  
    path('persons/update/<int:pk>/', views.person_update_delete, name='person-update'),  
    path('persons/delete/<int:pk>/', views.person_update_delete, name='person-delete'),  

    path('osoby/search/<str:substring>/', views.osoba_search, name='osoba-search'),  

    path('stanowiska/', StanowiskoList.as_view(), name='stanowisko-list'),  
    path('stanowiska/<int:pk>/', StanowiskoDetail.as_view(), name='stanowisko-detail'), 
    path('stanowisko/<int:id>/members/', StanowiskoMembersView.as_view(), name='stanowisko-members'),  

    path('welcome/', views.welcome_view, name='welcome-view'), 

    path('persons_html/', views.person_list_html, name='persons-html'), 
    path('persons_html/<int:id>/', views.person_detail_html, name='person-detail-html'),  

    path('teams_html/', views.team_list_html, name='teams-html'),  
    path('teams_html/<int:id>/', views.team_detail_html, name='team-detail-html'),  
]
