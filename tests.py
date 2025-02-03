from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('name', ['', 'НазваниеКнигиБольше40Символов НазваниеКни'])
    def test_add_new_book_add_book_with_len_name_less_0_or_more_40(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.books_genre) == 0

    @pytest.mark.parametrize('name, genre',
                             [
                                 ['Война и Мир', 'Детективы'],
                                 ['Задача трех тел', 'Фантастика'],
                                 ['Чужак', 'Ужасы'],
                                 ['Хеллсинг', 'Мультфильмы'],
                                 ['Крутой учитель Онидзука', 'Комедии']
                             ])
    def test_set_book_genre_add_genre_to_book(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    def test_get_book_genre_existing_book(self, collector):
        collector.add_new_book('Нетопырь')
        collector.set_book_genre('Нетопырь', 'Детективы')
        assert collector.get_book_genre('Нетопырь') == 'Детективы'

    def test_get_book_genre_non_existing_book(self, collector):
        collector.add_new_book('Крутой учитель Онидзука')
        collector.set_book_genre('Крутой учитель Онидзука', 'Комедии')
        assert collector.get_book_genre('Не очень Крутой учитель Онидзука') is None

    def test_get_books_with_specific_genre_get_two_book(self, collector):
        collector.add_new_book('Красношейка')
        collector.set_book_genre('Красношейка', 'Детективы')
        collector.add_new_book('Королевство')
        collector.set_book_genre('Королевство', 'Детективы')
        assert len(collector.get_books_with_specific_genre('Детективы')) == 2
        assert 'Королевство' in collector.get_books_with_specific_genre('Детективы')

    def test_get_books_genre_get_added_book_name_and_genre(self, collector):
        collector.add_new_book('Капитал')
        collector.set_book_genre('Капитал', 'Фантастика')
        assert 'Капитал' in collector.get_books_genre().keys() and 'Фантастика' in collector.get_books_genre().values()

    def test_get_books_for_children_get_book_for_children(self, collector):
        collector.add_new_book('Капитанская дочка')
        collector.set_book_genre('Капитанская дочка', 'Фантастика')
        assert 'Капитанская дочка' in collector.get_books_for_children()

    def test_get_books_for_children_not_return_book_with_age_rating_genre(self, collector):
        collector.add_new_book('Туман')
        collector.set_book_genre('Туман', 'Ужасы')
        collector.add_new_book('Двадцать тысяч лье под водой')
        collector.set_book_genre('Двадцать тысяч лье под водой', 'Фантастика')
        assert 'Туман' not in collector.get_books_for_children()

    def test_add_book_in_favorites_add_book(self, collector):
        collector.add_new_book('Колыбельная')
        collector.set_book_genre('Колыбельная', 'Ужасы')
        collector.add_book_in_favorites('Колыбельная')
        assert 'Колыбельная' in collector.favorites

    def test_delete_book_from_favorites_delete_one_book(self, collector):
        collector.add_new_book('Шаровая молния')
        collector.set_book_genre('Шаровая молния', 'Фантастика')
        collector.add_book_in_favorites('Шаровая молния')
        collector.delete_book_from_favorites('Шаровая молния')
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_get_added_book(self, collector):
        collector.add_new_book('Евангелион')
        collector.set_book_genre('Евангелион', 'Фантастика')
        collector.add_book_in_favorites('Евангелион')
        assert len(collector.get_list_of_favorites_books()) == 1
