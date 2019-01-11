from django.db import models

# Create your models here.
class DishName(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    name = models.CharField(
        max_length=200,
        help_text="Enter a dish name"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name