from django.db import models

class GlossaryTerm(models.Model):

    category_choices = [
        ('Architecture & Patterns', 'Architecture & Patterns'),
        ('Language & Core Tools', 'Language & Core Tools'),
        ('Security', 'Security'),
        ('Testing', 'Testing'),
        ('Jetpack Compose & UI', 'Jetpack Compose & UI'),
        ('Data & Storage', 'Data & Storage'),
        ('Networking', 'Networking'),
        ('Dependency Injection', 'Dependency Injection'),
        ('Navigation & Lifecycle', 'Navigation & Lifecycle'),
        ('Firebase & Cloud', 'Firebase & Cloud'),
        ('App Distribution & Analytics', 'App Distribution & Analytics'),
        ('Performance & Optimization', 'Performance & Optimization'),
        ('Other', 'Other'),
    ]
    
    term = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=50, choices=category_choices, default='Other')
    definition = models.TextField()

    def __str__(self):
        return self.term

    class Meta:
        verbose_name_plural = "Glossary Terms"
        ordering = ['term']
