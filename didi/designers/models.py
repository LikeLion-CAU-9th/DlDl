from django.db import models

# Create your models here.
class Designer_Info(models.Model):
    
    name = models.CharField(max_length=20, null = True)
    # 커버사진
    cover_image = models.ImageField(upload_to='images/', blank=True, null=True)
    
    # 성향 정하기(임시 셋팅)
    personerity = (
      ('1', '시간 엄수'),
      ('2', '소통'),
      ('3', '친화력'),
      ('4', '협업'),
      ('5', '아이디어'),
      ('6', '기획'),
      ('7', '노력'),
      ('8', '인내'),
      ('9', '열정'),
    )
    personerity_pick_1 = models.CharField(max_length=1, choices=personerity)
    personerity_pick_2 = models.CharField(max_length=1, choices=personerity)
    personerity_pick_3 = models.CharField(max_length=1, choices=personerity)
    
    # 소개
    introduce = models.TextField()


    def __str__(self):
        return self.name


class Portfolio(models.Model):


  designer = models.ForeignKey(Designer_Info, on_delete=models.CASCADE, null= True, related_name='portfolio')
  name = models.CharField(max_length=20)

  is_repre = (
      ('0', '서브'),
      ('1', '대표')
  )
  representation = models.CharField(max_length=1, choices= is_repre)
  photo = models.ImageField(upload_to ='uploads/', blank=True, null=True)
  comment = models.TextField()
  # file = models.FileFeild(upload_to ='uploads/', blank=True, null=True)
