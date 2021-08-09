from rest_framework import serializers
from keeps_challenges.models import Student 
from keeps_challenges.models import Course
from keeps_challenges.models import Enrollment
from keeps_challenges.models import Status

#Serializable do model 'Student'
class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ['id', 'name', 'phone', 'date_created']

#Serializable do model 'Course'
class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ['id', 'name', 'description', 'duration']

#Serializable do model 'Course'
class EnrollmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Enrollment
		fields = ['id', 'student', 'course', 'score', 'status']

class EnrollmentStatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = ['id',]