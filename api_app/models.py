from django.db import models
import uuid
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.
class Causes(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=100)
  description = models.TextField()
  image_url = models.ImageField(upload_to='causes_images/')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.title} - {self.image_url}"
  
class Contribute(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=255)
  email = models.EmailField()
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  causes = models.ForeignKey(Causes, related_name='contributions', on_delete=models.CASCADE)
  receipt_pdf = models.FileField(upload_to='cause_receipts/', storage=RawMediaCloudinaryStorage())
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.name} contributed {self.amount} to {self.causes.title}"