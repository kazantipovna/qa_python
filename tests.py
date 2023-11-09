import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre.keys()) == 2

    def test_set_book_genre_set_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Реликт')
        collector.set_book_genre('Реликт', 'Фантастика')
        assert list(collector.books_genre.values()) == ['Фантастика']

    def test_add_new_book_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Реликт')
        assert list(collector.books_genre.values()) == ['']

    def test_get_book_genre_get_genre_by_name(self, books_dict):
        assert books_dict.get_book_genre('Реликт') == 'Фантастика'

    def test_get_books_with_specific_genre_get_fantastic_books(self, books_dict):
        assert books_dict.get_books_with_specific_genre('Фантастика') == ['Реликт']

    def test_get_books_genre_all_books(self, books_dict):
        books_dict.get_books_genre()
        assert books_dict.books_genre == {'Реликт': 'Фантастика',
                                          'Зов Ктулху': 'Ужасы',
                                          '12 негритят': 'Детективы',
                                          'Незнайка на луне': 'Мультфильмы',
                                          'Золотой теленок': 'Комедии'}

    def test_get_books_for_children_all_children_books(self, books_dict):
        assert books_dict.get_books_for_children() == ['Реликт', 'Незнайка на луне', 'Золотой теленок']

    @pytest.mark.parametrize('adult_books', ['Зов Ктулху', '12 негритят'])
    def test_get_books_for_children_no_adult_books(self, books_dict, adult_books):
        assert adult_books not in books_dict.get_books_for_children()

    def test_add_book_in_favorites_add_two_books(self, books_dict):
        books_dict.add_book_in_favorites('Реликт')
        books_dict.add_book_in_favorites('Зов Ктулху')
        assert len(books_dict.favorites) == 2

    def test_delete_book_from_favorites_one_book_stand(self, books_dict, favorites_books):
        books_dict.delete_book_from_favorites('Зов Ктулху')
        assert books_dict.favorites == ['Реликт']

    def test_delete_book_from_favorites_one_no_books_stand(self, books_dict, favorites_books):
        books_dict.delete_book_from_favorites('Реликт')
        books_dict.delete_book_from_favorites('Зов Ктулху')
        assert books_dict.favorites == []

    def test_get_list_of_favorites_books_all_favorites_books(self, books_dict, favorites_books):
        assert books_dict.favorites == ['Реликт', 'Зов Ктулху']
