from django.db import models

class Vk(models.Model):
    nick = models.TextField(default='NickName')
    vk = models.TextField()
    id_vk = models.TextField()
    token_vk = models.TextField()

    

class Squad(models.Model):
    Name = models.TextField()


    def __str__(self):
        return self.Name
