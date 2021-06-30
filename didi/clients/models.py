from django.db import models
from django.utils import timezone
from django.conf import settings
from accounts.models import User

class Enterprise(models.Model):
    # title, body, show, datetime, image

    PUBLIC = 'public'
    PRIVATE = 'private'
    MY = 'my'

    SHOW_TYPES = [
        (PUBLIC, 'PUBLIC'),
        (PRIVATE, 'PRIVATE'),
        (MY, 'MY')
    ]

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, help_text="기관명")
    certification_number = models.CharField(max_length=10, help_text="인증번호") # 제2021-035호
    representation = models.CharField(max_length=10, help_text="대표자명")
    social_type = models.CharField(max_length=20, help_text="사회적목적 실현 유형")
    certification_date = models.DateField(null=True, help_text="인증시기")
    location = models.CharField(max_length=50, help_text="소재지")
    tel = models.CharField(max_length=20, help_text="대표번호")
    fax = models.CharField(max_length=20, help_text="팩스번호")
    business_inform = models.CharField(max_length=50, help_text="사업내용")
    service_category = models.CharField(max_length=50, help_text="사회서비스 분야")
    logo_image = models.ImageField(upload_to='images/', blank=True, null=True)
    email = models.EmailField(max_length=128, help_text="이메일")
    page = models.URLField(max_length=200, help_text="기업 페이지")


    def __str__(self):
        return self.title