#coding=utf8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.core.urlresolvers import reverse

NAME_CHOICES = (
    ('XQ', r'需求'),
    ('WT', r'问题'),
)
STATU_CHOICES = (
    ('CG', r'常规'),
    ('JJ', r'紧急'),
    ('TJ', r'特级'),
)

class Content(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey('Project')
    type = models.CharField(max_length=2, choices=NAME_CHOICES)
    statu = models.CharField(max_length=2, choices=STATU_CHOICES)
    plan_version = models.ForeignKey('Version', related_name="plan_version")
    actual_version = models.ForeignKey('Version', related_name="actual_version")
    uat_date = models.DateField(blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)
    module = models.ManyToManyField('Module')
    product_manager = models.ForeignKey(User, related_name='product_manager') # need to be filtered
    developer = models.ManyToManyField(User, related_name='developer') # need to be filtered
    tester = models.ManyToManyField(User, related_name='tester') # need to be filtered
    
    def __unicode__(self):
        return self.name
    def get_success_url(self):
        return reverse("PM:list_content")
    class Meta:
        ordering = ('-id',)
    def get_absolute_url(self):
        return reverse("PM:list_content")
    
class Project(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="项目名")
    description = models.CharField(max_length=100, blank=True, null=True, verbose_name="描述")
    add_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("PM:list_project")
    class Meta:
        ordering = ('-add_date',)

class Module(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    def get_success_url(self):
        return reverse("PM:list_module")
    
class Version(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="版本号")
    description = models.CharField(max_length=100, blank=True, null=True, verbose_name="描述")
    add_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name
    def get_success_url(self):
        return reverse("PM:list_version")
    def get_absolute_url(self):
        return reverse("PM:list_version")
    class Meta:
        ordering = ('-add_date',)