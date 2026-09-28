from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import mixins, viewsets, generics

from django_filters.rest_framework import DjangoFilterBackend ###
from rest_framework.filters import SearchFilter, OrderingFilter ###

from .models import Mixin, Human, Client, Post 
from .serialzers import MixinSerializer, HumanSerializer, PostSerializer, ClientSerializer
from .pagination import HumanPag
# Create your views here.

# class MixinView(mixins.ListModelMixin,
#                 mixins.CreateModelMixin,
#                 GenericAPIView): # 
    
#     queryset = Mixin.objects.all()
#     serializer_class = MixinSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     print('cоздаеттся книга')

    #     self.response = super().create(request, *args, **kwargs)
    #     return self.response 
    
    # def perform_create(self, serializer):
    #     serializer.save()

    # def perform_create(self, serializer):
    #     serializer.save(title=self.request.user)


    
# class MixinDetailView(mixins.RetrieveModelMixin,
#                 mixins.UpdateModelMixin,
#                 mixins.DestroyModelMixin,
#                 GenericAPIView): # 
    
#     queryset = Mixin.objects.all()
#     serializer_class = MixinSerializer

#     def get(self, request, *args, **kwargs): # kwargs = pk
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)



class HumanViewsets(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('id',)
    serializer_class = HumanSerializer
    
    pagination_class = HumanPag

    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]

    filter_fields = ('title',) 
    search_fields = ('title', 'description')

    ordering = ('title',) # order = 1 


# ==========================================
# 1. API для раздела "Статьи и Новости"
# ==========================================

class PostListCreateAPIView(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            generics.GenericAPIView):
    """
    GET  /mixin/posts/ - Получить список всех статей (200 OK)
    POST /mixin/posts/ - Создать новую статью (201 Created)
    """
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostDetailAPIView(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    """
    GET    /mixin/posts/<id>/ - Получить статью по ID (200 OK)
    PUT    /mixin/posts/<id>/ - Полная перезапись статьи (200 OK)
    PATCH  /mixin/posts/<id>/ - Частичное обновление статьи (200 OK)
    DELETE /mixin/posts/<id>/ - Удалить статью (204 No Content)
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# ==========================================
# 2. API для раздела "Клиентская база"
# ==========================================

class ClientListCreateAPIView(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              generics.GenericAPIView):
    """
    GET  /mixin/clients/ - Получить список клиентов (200 OK)
    POST /mixin/clients/ - Добавить клиента (201 Created)
    """
    queryset = Client.objects.all().order_by('-id')
    serializer_class = ClientSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ClientDetailAPIView(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          generics.GenericAPIView):
    """
    GET    /mixin/clients/<id>/ - Получить карточку клиента по ID (200 OK)
    PUT    /mixin/clients/<id>/ - Полностью обновить данные клиента (200 OK)
    PATCH  /mixin/clients/<id>/ - Изменить одно/несколько полей (200 OK)
    DELETE /mixin/clients/<id>/ - Удалить клиента из базы (204 No Content)
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)