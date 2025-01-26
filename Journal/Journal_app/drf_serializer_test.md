## Testy serializerów

Przykładowy kod testujący dwa serializery:
```python
from myapp.serializers import ArticleSerializer, AuthorSerializer

article_data = {
    "id": 1,
    "title": "Testowy artykuł",
    "content": "To jest treść testowego artykułu.",
    "published_date": "2025-01-21"
}

author_data = {
    "id": 1,
    "name": "Jan Kowalski",
    "bio": "Autor testowy"
}

# Test ArticleSerializer
article_serializer = ArticleSerializer(data=article_data)
if article_serializer.is_valid():
    print("ArticleSerializer działa poprawnie:", article_serializer.validated_data)

# Test AuthorSerializer
author_serializer = AuthorSerializer(data=author_data)
if author_serializer.is_valid():
    print("AuthorSerializer działa poprawnie:", author_serializer.validated_data)