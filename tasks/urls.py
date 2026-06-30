from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api' , views.TaskViewSet, basename='task')

urlpatterns = [



    path('', include(router.urls))
    
    #path('',views.task_list,name ='task_list'),

    # path('api/',views.api_task_list,name ='api_task_list'),

    # path('api/<int:pk>/', views.api_task_detail, name='api_task_detail'),
]

