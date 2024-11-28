from django.db import models

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    cloud_image_url = models.URLField()  # Use URLField for cloud-stored image URL
    action = models.URLField(blank=True, null=True)
    year = models.IntegerField()
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Imagen: " + self.title + " (" + str(self.year) + ")" + " | " + " Sección: " + self.section.name
    
class TextContent(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    year = models.IntegerField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " (" + str(self.year) + ")"

class TextContentImage(models.Model):
    text_content = models.ForeignKey(TextContent, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return "Texto: " + self.text_content.title + " (" + str(self.text_content.year) + ")" + " | " + "Imagen: " +  self.image.title + " (" + str(self.image.year) + ")"