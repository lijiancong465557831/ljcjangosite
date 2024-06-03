from django.db import models
class  Event(models.Model):
    #主键 显示定义
    id=models.IntegerField('主键',primary_key=True)
    name=models.CharField('发布会名称',max_length=256)
    address=models.CharField('发布会地址',max_length=512)
    limits=models.IntegerField(default=100)
    status=models.BooleanField(default=True)
    start_time=models.DateTimeField(null=True)
    def __str__(self):
        return self.name
# Create your models here.
