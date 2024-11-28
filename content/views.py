from rest_framework import viewsets
from rest_framework.response import Response
from collections import defaultdict
from .serializer import SectionSerializer, ImageSerializer, TextContentSerializer, TextContentImageSerializer, TextContentOnlySerializer, YearGroupedImageSerializer
from .models import Section, Image, TextContent, TextContentImage

class SectionView(viewsets.ReadOnlyModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()

class ImageView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ImageSerializer
    def get_queryset(self):
        """
        Optionally restricts the returned images to a given section,
        by filtering against a `section` query parameter in the URL.
        """
        queryset = Image.objects.all()
        section_name = self.request.query_params.get('section')
        if section_name is not None:
            queryset = queryset.filter(section__name=section_name)
        return queryset    

class TextContentOnlyView(viewsets.ReadOnlyModelViewSet):
    serializer_class = TextContentOnlySerializer
    def get_queryset(self):
        """
        Optionally restricts the returned text content to a given section,
        by filtering against a `section` query parameter in the URL.
        """
        queryset = TextContent.objects.all().order_by('id')
        section_name = self.request.query_params.get('section')
        if section_name is not None:
            queryset = queryset.filter(section__name=section_name)
        return queryset
    

class TextContentView(viewsets.ReadOnlyModelViewSet):
    serializer_class = TextContentSerializer
    def get_queryset(self):
        """
        Optionally restricts the returned text content to a given section,
        by filtering against a `section` query parameter in the URL.
        """
        queryset = TextContent.objects.all().order_by('-year')
        section_name = self.request.query_params.get('section')
        if section_name is not None:
            queryset = queryset.filter(section__name=section_name)
        return queryset

class TextContentImageView(viewsets.ReadOnlyModelViewSet):
    serializer_class = TextContentImageSerializer
    queryset = TextContentImage.objects.all()

class YearGroupedImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = YearGroupedImageSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        section_name = self.request.query_params.get('section')
        if section_name is not None:
            queryset = queryset.filter(section__name=section_name)
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        grouped_images = defaultdict(list)
        for image in data:
            grouped_images[image['year']].append(image)

        grouped_data = [{'year': year, 'images': images} for year, images in grouped_images.items()]
        grouped_data.sort(key=lambda x: x['year'], reverse=True)


        return Response(grouped_data)
