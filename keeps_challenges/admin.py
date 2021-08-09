from django.contrib import admin
from keeps_challenges.models import Student
from keeps_challenges.models import Course
from keeps_challenges.models import Enrollment
from keeps_challenges.models import Status

class Students(admin.ModelAdmin):
		list_display = ('id', 'name', 'phone')
		link_list_display = ('id', 'name',)
		search_fields = ('name', )

class Courses(admin.ModelAdmin):
		list_display = ('id', 'name', 'description', 'duration')
		link_list_display = ('id', 'name')
		search_fields = ('name',)

class Enrollments(admin.ModelAdmin):
		list_display = ('id', 'student', 'course', 'date_enroll')
		link_list_display = ('id', 'name')
		search_fields = ('name',)

class Stats(admin.ModelAdmin):
		list_display = ('id', 'status')
		link_list_display = ('id', 'status')
		search_fields = ('status',)


admin.site.register(Student, Students)
admin.site.register(Course, Courses)
admin.site.register(Enrollment, Enrollments)
admin.site.register(Status, Stats)
