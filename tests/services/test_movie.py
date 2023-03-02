from unittest.mock import MagicMock

import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture
def movie_dao():
    movie_dao = MovieDAO(None)

    m1 = Movie(id=1, title='Фильм 1', description='Описание фильма 1', trailer='www.trailer1', year=2023, rating=8.76,
               genre_id=1, director_id=1)
    m2 = Movie(id=2, title='Фильм 2', description='Описание фильма 2', trailer='www.trailer2', year=2022, rating=8.77,
               genre_id=2, director_id=2)
    m3 = Movie(id=3, title='Фильм 3', description='Описание фильма 3', trailer='www.trailer3', year=2021, rating=8.75,
               genre_id=3, director_id=3)

    movie_dao.get_one = MagicMock(return_value=m1)
    movie_dao.get_all = MagicMock(return_value=[m1, m2, m3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            'id': 4,
            'title': 'Фильм 4',
            'description': 'Описание фильма 4',
            'trailer': 'www.trailer4',
            'year': 2020,
            'rating': 6.7,
            'genre_id': '4',
            'director_id': '4'
        }

        movie = self.movie_service.create(movie_d)

        assert movie.id is not None

    def test_update(self):
        movie_d = {
            'id': 4,
            'title': 'Фильм 4',
            'description': 'Описание фильма 4',
            'trailer': 'www.trailer4',
            'year': 2020,
            'rating': 6.7,
            'genre_id': '4',
            'director_id': '4'
        }

        self.movie_service.update(movie_d)

    def test_delete(self):
        self.movie_service.delete(1)
