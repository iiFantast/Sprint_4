# Sprint_4
Описание методов для тестирования класса BooksCollector:
1. def test_add_new_book_add_two_books - проверяет добавление двух книг
2. def test_add_new_book_add_book_with_len_name_less_0_or_more_40 - проверяет, что нельзя добавить книгу название которой содержит 0 символов или больше 41 символа
3. def test_set_book_genre_add_genre_to_book - проверяет добавление жанра книге
4. def test_get_book_genre_existing_book - проверяет получение жанра по названию книги
5. def test_get_book_genre_non_existing_book - проверяет, что жанр книги не возвращается, если книги не существует
6. def test_get_books_with_specific_genre_get_two_book - проверяет, что возвращаются книги с определенным жанром
7. def test_get_books_genre_get_added_book_name_and_genre - проверяет, что возвращается словарь с добавленной книгой и жанром
8. def test_get_books_for_children_get_book_for_children - проверяет, что возвращаются книги, жанр которых определен как для детей
9. def test_get_books_for_children_not_return_book_with_age_rating_genre - проверяет, что в списке книг для детей не возвращаются книги из списка 18+
10. def test_add_book_in_favorites_add_book - проверяет добавление книги в избранное
11. def test_delete_book_from_favorites_delete_one_book - проверяет удаление книги из избранного
12. def test_get_list_of_favorites_books_get_added_book - проверяет получения списка избранных книг