from rest_framework import serializers
from .models import Section, Image, TextContent, TextContentImage
from itertools import groupby

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'name', 'description')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class TextContentImageSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    class Meta:
        model = TextContentImage
        fields = '__all__'

class TextContentSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    class Meta:
        model = TextContent
        fields = ('title', 'text', 'year', 'section', 'images')
    def get_images(self, obj):
        images = Image.objects.filter(textcontentimage__text_content=obj)
        return ImageSerializer(images, many=True).data

class TextContentOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = TextContent
        fields = ('id', 'title', 'text', 'year', 'section')

class YearGroupedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'




