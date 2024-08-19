from django.shortcuts import render, get_object_or_404
from .models import Course, Tutorial

def tutorial_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    tutorial_id = request.GET.get('tutorial_id')
    if tutorial_id:
        tutorial = get_object_or_404(Tutorial, id=tutorial_id, course=course)
        tutorial.views_count += 1
        tutorial.save()
    else:
        tutorial = Tutorial.objects.filter(course=course).order_by('order').first()
    tutorials = Tutorial.objects.filter(course=course).order_by('order')
    courses = Course.objects.all()
    top_tutorials = Tutorial.objects.all().order_by('-views_count')[:5]
    return render(request, 'tutorial_screen.html', {
        'course': course,
        'tutorial': tutorial,
        'tutorials': tutorials,
        'courses': courses,
        'top_tutorials': top_tutorials,
        'current_course_id': course_id  # Add this line
    })


def index(request):
    # Retrieve all Course objects from the database
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'home_screen.html', context)
