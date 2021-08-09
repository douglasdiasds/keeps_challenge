from django.contrib import admin
from django.urls import path, re_path, include
from keeps_challenges.views import StudentViewSet, CoursesViewSet, EnrollmentsViewSet, StatusFilterViewSet
from rest_framework import routers

#Registra os endpoints
router = routers.DefaultRouter()
router.register(r'students', StudentViewSet, 'students')
router.register(r'courses', CoursesViewSet, 'courses')
router.register(r'enrollments', EnrollmentsViewSet, 'enrollments')


router2 = routers.DefaultRouter()
router2.register(r'enrollmentsStatus', StatusFilterViewSet)
#Atribui os endpoints as url's
urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include(router.urls)),
	##re_path(r'^students/{[9-0]}/$', include(router2.urls))
]