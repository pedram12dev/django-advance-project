from rest_framework import serializers
from blog.models import Category, Post



# class PostSerializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length = 250)



class CategorySerializer(serializers.ModelSerializer):


    class  Meta:
        model = Category
        fields = ['id' , 'name']



class PostSerializers(serializers.ModelSerializer):
    content = serializers.ReadOnlyField()
    snippet = serializers.ReadOnlyField(source = 'get_snippet')
    category = serializers.SlugRelatedField(
                            many=False , 
                            slug_field = 'name' , 
                            queryset = Category.objects.all())

    class Meta:
        model = Post
        fields = ['auther','title','status','content','category','snippet' ,'created_date','published_date']
        read_only_fields = ['category']
