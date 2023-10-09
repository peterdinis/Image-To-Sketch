from django.db import models

##TODO: Update this later
def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

# Create your models here.
class Sketch(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(default='')

    def __str__(self):
        return self.name