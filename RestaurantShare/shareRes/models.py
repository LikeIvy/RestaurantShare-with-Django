from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length = 100)

class Restaurant(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=3) # Category모델 참조, on_delete => 참조하는 모델이 삭제되었을 때 해당 요소는 어떻게 할지 물어보는 것
    restaurant_name = models.CharField(max_length = 100)                            # 여기서는 SET_DEFAULT로 참조되는 요소가 삭제될 때 이를 참조하는 요소에 대해서 참조 값을 설정해 둔 DEFAULT값으로 설정한다.
    restaurant_link = models.CharField(max_length = 500)                            # default로 id값 3을 줬으므로 restaurant 요소가 참조하는 category가 삭제될 때 자동으로 id값이 3인 category를 참조하도록 설정해둔 것
    restaurant_content = models.TextField() # 길이 제한이 없는 문자열을 갖는 요소 TextField
    restaurant_keyword = models.CharField(max_length = 50)