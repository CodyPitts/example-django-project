from django.db import models

# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=50)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20, blank=True)
    venue = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(help_text='The URL piece that identifies this event, e.g. "example.com/spokane"')

    def __str__(self):
        return self.event_name


class Speaker(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    middle_name = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


# class Sponsor(models.Model):
#     logo = models.ImageField(blank=True)
#     name = models.CharField(max_length=200)
#     link = models.URLField(blank=True)
#     event = models.ManyToManyField(Event, blank=True)
#     description = models.TextField(blank=True)
#
#     def __str__(self):
#         return self.name


class Session(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    room = models.CharField(max_length=200, blank=True)
    summary = models.TextField(blank=True)
    speakers = models.ManyToManyField(Speaker, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
