from django.urls import path
from . import views 

app_name = "prac_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>/', views.detail, name="detail" ),
    # path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:num>/delete', views.delete, name="delete"),
    # path('<int:num>/edit', views.edit, name="edit"),
    path('<int:num>/update', views.update, name="update"),
    path('<int:num>/comments/', views.comments_create, name="comments_create"),
    path('<int:article_pk>/comments/<int:comment_pk>/delete',
         views.comments_delete,
         name="comments_delete"),
]
