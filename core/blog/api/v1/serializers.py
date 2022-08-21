from rest_framework import serializers
from blog.models import Post



# class PostSerializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length = 250)






class PostSerializers(serializers.ModelSerializer):
    
    

    class Meta:
        model = Post
        fields = ['auther','title','status','content','created_date','published_date']