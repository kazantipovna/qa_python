Файл test.py - проверки:
	1.	test_add_new_book_add_two_books - добавление книг в словать
	2.	test_set_book_genre_set_genre - установка жанра для книги
	3.	test_add_new_book_no_genre - добавление книги без жанра и у добавленной книги жанр пустой
	4.	test_get_book_genre_get_genre_by_name - жанр по названию книги
	5.	test_get_books_with_specific_genre_get_fantastic_books - поиск книг по жанру (фантастика)
	6.	test_get_books_genre_all_books - отработка метода get_books_genre
	7.	test_get_books_for_children_all_children_books - получение списка книг, подходящих детям
	8.	test_get_books_for_children_no_adult_books - в детсвком списке нет книг для взрослых
	9.	test_add_book_in_favorites_add_two_books - добавление книг в избранное
	10.	test_delete_book_from_favorites_one_book_stand - удаление книги из избранного, список остается не пустой
	11.	test_delete_book_from_favorites_one_no_books_stand - удаление книг из избранного, список остается пустой
	12.	test_get_list_of_favorites_books_all_favorites_books - отработка метода get_list_of_favorites_books

Файл conftest.py - фикстуры:
books_dict - создание словаря книг с каждым жанром
favorites_books - создание списка избранного
