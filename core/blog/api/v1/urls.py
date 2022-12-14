from django.urls import path
from .views import CategoryModelViewSet, PostViewSet
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register('post' ,PostViewSet , basename = 'post')
router.register('category' , CategoryModelViewSet , basename = 'category')
urlpatterns = router.urls


# urlpatterns =[
#     # path('post/' , views.PostList.as_view() , name = "post-list"),
#     # path('post/<int:pk/' , views.PostDetail.as_view() , name = "post-detail"),
#     path('post/' ,views.PostViewSet.as_view({'get':'list' ,'post':'create'}) , name="post-list"),
#     path('post/<int:pk>/' ,views.PostViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}) , name="post-detail")

# ]