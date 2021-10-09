from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Сохраняет автора поста(авториз.пользователь)"""
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """запрещает редактировать не автору"""
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("Изменение чужого контента запрещено!")
        return super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        """запрещает удалять не автору"""
        if serializer.author != self.request.user:
            raise PermissionDenied("Удаление контента запрещено!")
        return super(PostViewSet, self).perform_destroy(serializer)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer

    def get_queryset(self):
        """возвращает запрос, отфильтрованный по id поста,
           к которому написаны комментарии"""
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        """Сохраняет автора коммента(авториз.пользователь)"""
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """запрещает редактировать не автору"""
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("Изменение чужого контента запрещено!")
        return super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        """запрещает удалять не автору"""
        if serializer.author != self.request.user:
            raise PermissionDenied("Удаление контента запрещено!")
        return super(CommentViewSet, self).perform_destroy(serializer)
