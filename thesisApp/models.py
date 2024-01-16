from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Institute(models.Model):
    name = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SubjectTopic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Keyword(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ThesisType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Thesis(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='authored_thesis_set', on_delete=models.CASCADE)
    supervisor = models.ForeignKey(User, related_name='supervised_thesis_set', on_delete=models.SET_NULL, null=True, blank=True)
    co_supervisor = models.ForeignKey(User, related_name='co_supervised_thesis_set', on_delete=models.SET_NULL, null=True, blank=True)
    keywords = models.ManyToManyField(Keyword)
    thesis_no = models.CharField(max_length=7, unique=True, editable=False)
    title = models.CharField(max_length=500)
    abstract = RichTextField(max_length=5000)
    text = RichTextField()
    thesis_type = models.ForeignKey(ThesisType, on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)
    page_amount = models.IntegerField()
    year = models.IntegerField()
    submission_date = models.DateField(auto_created=True, auto_now_add=True)
    topic = models.ForeignKey(SubjectTopic, on_delete=models.CASCADE)

    readonly_fields = ('thesis_no',)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # auto generate thesis_no
        if not self.thesis_no:
            self.thesis_no = self.generate_thesis_no()
        super().save(*args, **kwargs)
    
    def generate_thesis_no(self):
        # generate thesis_no Ex: 367541, 817720
        # get last thesis_no
        last_thesis = Thesis.objects.all().order_by('id').last()
        if not last_thesis:
            return '000001'
        last_thesis_no = int(last_thesis.thesis_no)
        new_thesis_no = last_thesis_no + 1
        return str(new_thesis_no).zfill(6)