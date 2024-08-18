from django.shortcuts import render, get_object_or_404
from .models import Course, Tutorial

def tutorial_detail(request, course_id):
    # Get the specific course
    course = get_object_or_404(Course, id=course_id)
    
    # Get the specific tutorial ID from query parameters
    tutorial_id = request.GET.get('tutorial_id')
    
    # If tutorial_id is provided, fetch that specific tutorial
    if tutorial_id:
        tutorial = get_object_or_404(Tutorial, id=tutorial_id, course=course)
        tutorial.views_count += 1
        tutorial.save()
    else:
        # Default to the first tutorial if no tutorial_id is provided
        tutorial = Tutorial.objects.filter(course=course).order_by('order').first()
    
    # Fetch all tutorials for displaying in the sidebar
    tutorials = Tutorial.objects.filter(course=course).order_by('order')
    
    # Fetch all courses for the header
    courses = Course.objects.all()
    
    # Get the top 5 most viewed tutorials across all courses
    top_tutorials = Tutorial.objects.all().order_by('-views_count')[:5]
    
    return render(request, 'tutorial_screen.html', {
        'course': course,
        'tutorial': tutorial,
        'tutorials': tutorials,
        'courses': courses,  # Add this line to pass courses to the template
        'top_tutorials': top_tutorials,  # Add this line to pass top tutorials to the template
    })



def index(request):
    # Retrieve all Course objects from the database
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'home_screen.html', context)
