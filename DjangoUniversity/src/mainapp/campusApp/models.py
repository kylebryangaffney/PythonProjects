from django.db import models

# Create your models here.

# Defines model for university campus location
class UniversityCampus(models.Model):

    # The name of the campus
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    # The two-letter state abbreviation where the campus is located
    campus_state = models.CharField(max_length=2, default="", blank=True, null=False)
    # A numeric identifier for the campus
    campus_number = models.IntegerField(default=0, blank=True, null=False)
    # Explicitly attaches Django's default Manager
    objects = models.Manager()

    # Controls how a UniversityCampus instance is displayed as a string
    def __str__(self):
        # Template with the campus's campus_name and campus_state.
        display_campus = "{0.campus_name}: {0.campus_state}"
        return display_campus.format(self)

    # Meta class provides additional configuration for the model.
    class Meta:
        verbose_name_plural = "University Campus"
