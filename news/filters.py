from django_filters import FilterSet
from .models import Post

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'author': ['exact'],
            'zagolovok': ['icontains'],
            'time_in': ['gt'],
            'post_type': ['exact']
        }