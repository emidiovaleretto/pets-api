from rest_framework.serializers import ModelSerializer
from posts.models import Post


class PostSerializer(ModelSerializer):
    '''
    Post Serializer to serialize the Post model fields
    '''
    class Meta:
        model = Post
        fields = '__all__'
