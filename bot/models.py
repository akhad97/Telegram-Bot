from django.db import models


class TelegramUser(models.Model):
    user_id = models.CharField(max_length=30)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, null=True)
    resume = models.CharField(max_length=100, null=True)
    # resume = models.FileField(upload_to="resume/%Y/%m", null=True)


    class Meta:
        verbose_name = 'TelegramUser'
        verbose_name_plural = 'TelegramUsers'

        
    def __str__(self):
        return self.full_name

class Vacancy(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name

# class Language(models.Model):
#     vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     code = models.CharField(max_length=30)


class Post(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, null = True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, null = True)


    def __str__(self):
        return self.user.full_name