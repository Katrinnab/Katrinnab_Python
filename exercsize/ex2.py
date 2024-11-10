from book import Book

library = [Book("Красная шапочка", "Ш. Перро"),
           Book("Сказки", "А.С. Пушкин"),
           Book("Красное и черное", "Стендаль")]

for i in library:
    print(f"{i.title} - {i.author}")
