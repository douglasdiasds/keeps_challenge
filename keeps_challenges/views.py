from django.shortcuts import render
from rest_framework import viewsets
from keeps_challenges.models import Student 
from keeps_challenges.models import Course
from keeps_challenges.models import Enrollment
from keeps_challenges.serializable import StudentSerializer
from keeps_challenges.serializable import CourseSerializer
from keeps_challenges.serializable import EnrollmentSerializer
from keeps_challenges.serializable import EnrollmentStatusSerializer
#View para exibição de TODOS os objetos do tipo 'Student'
class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

#View para exibição de TODOS os objetos do tipo 'Course'
class CoursesViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

#View para exibição de TODOS os objetos do tipo 'Enrollment'
class EnrollmentsViewSet(viewsets.ModelViewSet):
	queryset = Enrollment.objects.all()
	serializer_class = EnrollmentSerializer

#View para exibição de TODOS as matrículas(Enrollments) que foram reprovadas
class StatusFilterViewSet(viewsets.ModelViewSet):
	queryset = Enrollment.objects.filter(status__status='Reprovado')
	serializer_class = EnrollmentStatusSerializer