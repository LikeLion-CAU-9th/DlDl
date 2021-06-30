from django.db import models
from django.db.models.fields import CommaSeparatedIntegerField
from django.utils import timezone
from django.conf import settings
from designers.models import Designer_Info
from clients.models import Enterprise


class Project(models.Model):

    LOGO = 'logo'
    PACKAGE ='package'
    PRODUCT = 'product'
    WEB = 'web'
    APP = 'app'
    CHARACTER = 'charatcer'


    CATEGORY_TYPES = (
        (LOGO,'로고 디자인'),
        (PACKAGE,'패키지 디자인'),
        (PRODUCT, '제품 디자인'),
        (WEB,'웹 디자인'),
        (APP,'앱 디자인'),
        (CHARACTER, '캐릭터 디자인'),
    )

    enterprise_id = models.ForeignKey(Enterprise, related_name='enterprise', on_delete=models.CASCADE, db_column="enterprise_id")
    author =  models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=20)
    category = models.CharField(choices=CATEGORY_TYPES, max_length=9, null=True)
    budget = models.IntegerField()
    contest_start_time =models.DateTimeField(default=timezone.now)
    contest_last_time =models.DateTimeField(default=timezone.now)
    project_start_time =models.DateTimeField(default=timezone.now)
    project_last_time =models.DateTimeField(default=timezone.now)
    contest_contents =models.TextField()
    contest_references =models.FileField(upload_to='project/references', null=True)
    project_contents =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

  
    def publish(self):
        self.save() #automatically updated 

    def __str__(self):
        return self.title

    class Meta: 
        ordering = ['created_at']


class Apply(models.Model):
    designer_id =models.ForeignKey(Designer_Info, related_name='Designer', on_delete=models.CASCADE, db_column="designer_id")
    project_id = models.ForeignKey(Project, related_name='Project', on_delete=models.CASCADE, db_column="project_id")
    applier = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    proto_type = models.FileField(upload_to='apply/prototypes', null=True)
    cover_photo = models.ImageField(upload_to='covers',null=True)
    apply_comment = models.CharField(max_length=300, help_text ='저의 시안을 소개합니다!')
    apply_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.applier 
        
    class Meta : 
        db_table = 'Apply'


class ProjectComment(models.Model):
    project = models.ForeignKey(Project,related_name='project',on_delete=models.CASCADE,db_column="project_id")
    comment_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    comment_text =models.TextField(help_text="프로젝트에 관해 궁금한 내용을 물어보세요.")   
    comment_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.comment_author
