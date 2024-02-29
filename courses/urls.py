from django.urls import path
from . import views
from .views import CourseList,CourseDetail,CourseCreate,CourseUpdate

urlpatterns = [
    path('',views.home,name='home'),
    path('category/<str:category_name>/',views.home2,name='category'),
    path('course/<int:pk>/',CourseDetail.as_view(),name='detail'),
    path('course-create/',CourseCreate.as_view(),name='course-create'),
    path('course-update/<int:pk>/',CourseUpdate.as_view(template_name='courses/course_update_form.html'),name='course-update')
]
