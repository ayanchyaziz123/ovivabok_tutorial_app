from django.contrib import admin
from .models import Course, Tutorial

# Customize the admin site headers
admin.site.site_header = "OvivaBok Administration"
admin.site.site_title = "OvivaBok Admin Portal"
admin.site.index_title = "Welcome to OvivaBok Admin"

# Register the Tutorial model with custom admin settings
@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ('tutorial_title', 'course', 'created_at', 'updated_at', 'is_public')
    list_filter = ('is_public', 'course')
    search_fields = ('tutorial_title', 'tutorial_description')

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            # Make 'is_public' read-only for non-admin users
            return self.readonly_fields + ('is_public',)
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            # Ensure 'is_public' is set to False for non-admin users
            obj.is_public = False
        super().save_model(request, obj, form, change)

# Register the Course model
admin.site.register(Course)
