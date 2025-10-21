from django.db import models



#
# class Img(models.Model):
#       image  = models.ImageField(upload_to='note/')
#       created = models.DateTimeField(auto_created=True)
#
#       class Meta:
#           verbose_name= "Rasm"




class TextRight(models.Model):
     name_right = models.CharField(max_length=200, verbose_name="Qator nomi o'ng taraf")
     text_right = models.CharField(max_length=200, verbose_name="Text nomi o'ng taraf")
     link_right = models.URLField(max_length=4000, verbose_name="Link url o'ng taraf")
     created = models.DateTimeField(auto_created=True)

     def __str__(self):
         return self.name_right

     class Meta:
          verbose_name = "O'ng taraf ozgarish"


class TextLeft(models.Model):
    name_left = models.CharField(max_length=200, verbose_name="Qator nomi chap taraf")
    text_left = models.CharField(max_length=200, verbose_name="Text nomi chap taraf")
    link_left = models.URLField(max_length=4000, verbose_name="Link url chap taraf")
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
          return self.name_left

    class Meta:
          verbose_name = "Chap taraf ozgarish"


class Users(models.Model):
     name = models.CharField(max_length=400, verbose_name="Nomi:")
     body  = models.TextField()

     def __str__(self):
          return self.name

     class Meta:
          verbose_name = "Foydalanuvchi_"