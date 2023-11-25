from rest_framework import serializers

from books.models import Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"
        depth = 1
