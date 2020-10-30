from django.db import models

# Create your models here.
class DjangoClasses(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False)
    courseNumber = models.IntegerField(blank=False, null=False, unique=True)
    instructorName  = models.CharField(max_length=60, blank=True, null=False)
    duration = models.FloatField(blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return "{}\t{}".format(self.courseNumber, self.title)

dc1 = DjangoClasses(title = 'Python Course', courseNumber = 1001, instructorName = 'Fred', duration = 10.0)
dc2 = DjangoClasses(title = 'Database Course', courseNumber = 1002, instructorName = 'Wilma', duration = 5.5)
dc3 = DjangoClasses(title = 'Javascript', courseNumber = 1003, instructorName = 'Barney', duration = 6.3)


