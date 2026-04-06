from django.db import models

# Create your models here.

# Defines a model of a university course.
# Each instance of this class corresponds to a row in the database table.
class UniversityClasses(models.Model):

    # The string literal name of the course.
    title = models.CharField(max_length=60, default="", blank=True, null=False)

    # A numeric identifier for the course for the level
    course_number = models.IntegerField(default=0, blank=True, null=False)

    # The full name of the course instructor.
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)

    # The length of the course in hours, not needed, can be left blank.
    duration = models.FloatField(null=True, blank=True, default=None)

    # Explicitly attaches Django's default Manager, which makes UniversityClasses.objects.all() work
    objects = models.Manager()

    # Controls how a UniversityClasses instance is displayed as a string
    def __str__(self):
        # Formatting template with the course's title and instructor_name.
        display_course = "{0.title}: {0.instructor_name}"
        # Inserts this class's attributes into the template and returns it.
        return display_course.format(self)

    # Meta data for legibility outside of the code
    class Meta:
        verbose_name_plural = "University Classes"