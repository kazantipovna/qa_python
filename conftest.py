import pytest
from main import BooksCollector


@pytest.fixture
def books_dict():
    collector = BooksCollector()
    collector.add_new_book('Реликт')
    collector.set_book_genre('Реликт', 'Фантастика')
    collector.add_new_book('Зов Ктулху')
    collector.set_book_genre('Зов Ктулху', 'Ужасы')
    collector.add_new_book('12 негритят')
    collector.set_book_genre('12 негритят', 'Детективы')
    collector.add_new_book('Незнайка на луне')
    collector.set_book_genre('Незнайка на луне', 'Мультфильмы')
    collector.add_new_book('Золотой теленок')
    collector.set_book_genre('Золотой теленок', 'Комедии')
    return collector


@pytest.fixture
def favorites_books(books_dict):
    books_dict.add_book_in_favorites('Реликт')
    books_dict.add_book_in_favorites('Зов Ктулху')
    return books_dict.favorites

