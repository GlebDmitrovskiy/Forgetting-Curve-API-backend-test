from config.base_test import BaseTest
from services.text_generator import text_generator
from services.forgetting_curve.users.digit_generator import digit_generator
import pytest
import allure


class TestUsers(BaseTest):

    @pytest.fixture
    def create_and_delete_users(self):
        generated_nickname = text_generator(20)
        response = self.api_users.create_users(nickname=generated_nickname, first_name=text_generator(20),
                                               last_name=text_generator(20), age=digit_generator(99),
                                               job=text_generator(100))
        print(response.json())
        yield generated_nickname
        self.api_users.delete_users_by_nickname(generated_nickname)

    @allure.feature("test_positive_create_user")
    @pytest.mark.parametrize("allure_title, nickname, first_name, last_name, age, job",
                             [("Проверка создания пользователя, nickname 1 символ", text_generator(1),
                               text_generator(10), text_generator(10), digit_generator(50), text_generator(50)),
                              ("Проверка создания пользователя, nickname 20 символов", text_generator(20),
                               text_generator(10), text_generator(10), digit_generator(50), text_generator(50)),
                              ("Проверка создания пользователя, first_name 1 символ", text_generator(10),
                               text_generator(1), text_generator(10), digit_generator(50), text_generator(50)),
                              ("Проверка создания пользователя, first_name 20 символов", text_generator(10),
                               text_generator(20), text_generator(10), digit_generator(50), text_generator(50)),
                              ("Проверка создания пользователя, last_name 1 символ", text_generator(10),
                               text_generator(10), text_generator(1), digit_generator(50), text_generator(50)),
                              ("Проверка создания пользователя, last_name 20 символов", text_generator(10),
                               text_generator(10), text_generator(20), digit_generator(50), text_generator(10)),
                              ("Проверка создания пользователя, age 1 символ", text_generator(10), text_generator(10),
                               text_generator(10), 1, text_generator(10)),
                              ("Проверка создания пользователя, age 99 символов", text_generator(10),
                               text_generator(10), text_generator(10), 99, text_generator(10)),
                              ("Проверка создания пользователя, job 1 символ", text_generator(10), text_generator(10),
                               text_generator(10), digit_generator(50), text_generator(1)),
                              ("Проверка создания пользователя, job 100 символов", text_generator(10),
                               text_generator(10), text_generator(10), digit_generator(50), text_generator(100))

                              ]
                             )
    def test_positive_create_user(self, allure_title, nickname, first_name, last_name, age, job):
        data = {"nickname": nickname, "first_name": first_name, "last_name": last_name, "age": age, "job": job}
        response = self.api_users.create_users(**data)
        print(response.json())
        assert response.status_code == 200
        self.api_users.delete_users_by_nickname(nickname=nickname)

    @allure.feature("test_negative_create_user")
    @pytest.mark.parametrize("allure_title, nickname, first_name, last_name, age, job",
                             [("Негативная проверка создания пользователя, nickname 0 символов", "",
                               text_generator(10), text_generator(10), digit_generator(50), text_generator(50)),
                              ("Негативная проверка создания пользователя, nickname 21 символ", text_generator(21),
                               text_generator(10), text_generator(10), digit_generator(50), text_generator(50)),
                              ("Негативная проверка создания пользователя, nickname число", digit_generator(20),
                               text_generator(10), text_generator(10), digit_generator(50), text_generator(50)),
                              ("Негативная проверка создания пользователя, nickname float", 47.7,
                               text_generator(10), text_generator(10), digit_generator(50), text_generator(50)),
                              ("Негативная проверка создания пользователя, nickname bool", True,
                               text_generator(10), text_generator(10), digit_generator(50), text_generator(50)),
                              ("Негативная проверка создания пользователя, first_name 0 символов", text_generator(10),
                               "", text_generator(10), digit_generator(50), text_generator(50)),
                              ("Негативная проверка создания пользователя, first_name 21 символ", text_generator(10),
                               text_generator(21), text_generator(10), digit_generator(50), text_generator(50)),
                              ("Негативная проверка создания пользователя, first_name число", text_generator(10),
                               digit_generator(10), text_generator(10), digit_generator(50), text_generator(50)),
                              ("Негативная проверка создания пользователя, first_name float", text_generator(10),
                               47.7, text_generator(10), digit_generator(50), text_generator(50)),
                              ("Негативная проверка создания пользователя, first_name bool", text_generator(10),
                               True, text_generator(10), digit_generator(50), text_generator(50)),
                              ("Негативная проверка создания пользователя, last_name 0 символов", text_generator(10),
                               text_generator(10), "", digit_generator(50), text_generator(50)),
                              ("Негативная проверка создания пользователя, last_name 21 символ", text_generator(10),
                               text_generator(10), text_generator(21), digit_generator(50), text_generator(50)),
                              ("Негативная проверка создания пользователя, last_name число", text_generator(10),
                               text_generator(10), digit_generator(10), digit_generator(50), text_generator(50)),
                              ("Негативная проверка создания пользователя, last_name float", text_generator(10),
                               text_generator(10), 47.7, digit_generator(50), text_generator(50)),
                              ("Негативная проверка создания пользователя, last_name bool", text_generator(10),
                               text_generator(10), True, digit_generator(50), text_generator(50)),
                              ("Негативная проверка создания пользователя, age пустая строка", text_generator(10),
                               text_generator(10), text_generator(10), "", text_generator(50)),
                              ("Негативная проверка создания пользователя, age 0", text_generator(10),
                               text_generator(10), text_generator(10), 0, text_generator(50)),
                              ("Негативная проверка создания пользователя, age 100 символов", text_generator(10),
                               text_generator(10), text_generator(10), 100, text_generator(50)),
                              ("Негативная проверка создания пользователя, age строка", text_generator(10),
                               text_generator(10), text_generator(10), text_generator(10), text_generator(50)),
                              ("Негативная проверка создания пользователя, age float", text_generator(10),
                               text_generator(10), text_generator(10), 47.7, text_generator(50)),
                              ("Негативная проверка создания пользователя, age None", text_generator(10),
                               text_generator(10), text_generator(10), False, text_generator(50)),
                              ("Негативная проверка создания пользователя, job 0 символов", text_generator(10),
                               text_generator(10), text_generator(10), digit_generator(50), ""),
                              ("Негативная проверка создания пользователя, job 101 символ", text_generator(10),
                               text_generator(10), text_generator(10), digit_generator(50), text_generator(101)),
                              ("Негативная проверка создания пользователя, job число", text_generator(10),
                               text_generator(10), text_generator(10), digit_generator(50), digit_generator(50)),
                              ("Негативная проверка создания пользователя, job float", text_generator(10),
                               text_generator(10), text_generator(10), digit_generator(50), 47.7),
                              ("Негативная проверка создания пользователя, job bool", text_generator(10),
                               text_generator(10), text_generator(10), digit_generator(50), True)
                              ]
                             )
    def test_negative_create_user(self, allure_title, nickname, first_name, last_name, age, job):
        data = {"nickname": nickname, "first_name": first_name, "last_name": last_name, "age": age, "job": job}
        response = self.api_users.create_users(**data)
        print(response.json())
        assert response.status_code == 400
        self.api_users.delete_users_by_nickname(nickname=nickname)

    @allure.feature("test_get_users")
    def test_get_users(self):
        response = self.api_users.get_users()
        print(response.json())
        assert response.status_code == 200

    @allure.feature("test_get_users")
    def test_get_users_by_nickname(self, create_and_delete_users):
        response = self.api_users.get_users_by_nickname(nickname=create_and_delete_users)
        print(response.json())
        assert response.status_code == 200

    @allure.feature("test_delete_users")
    def test_delete_users(self):
        generated_nickname = text_generator(20)
        self.api_users.create_users(nickname=generated_nickname, first_name=text_generator(20),
                                    last_name=text_generator(20), age=digit_generator(99), job=text_generator(100))
        response = self.api_users.delete_users_by_nickname(nickname=generated_nickname)
        print(response.json())
        assert response.status_code == 200
        get_users = self.api_users.get_users_by_nickname(nickname=generated_nickname)
        print(get_users.json())
        assert get_users.status_code == 404

    @allure.feature("put_users")
    @pytest.mark.parametrize(
        "allure_title, age, job",
        [
            ("Проверка обновления данных о пользователе, age 1 символ", 1, text_generator(5)),
            ("Проверка обновления данных о пользователе, age 99 символов", 99, text_generator(5)),
            ("Проверка обновления данных о пользователе, job 1 символ", 50, text_generator(1)),
            ("Проверка обновления данных о пользователе, job 100 символов", 50, text_generator(100))
        ]
    )
    def test_positive_put_users(self, allure_title, age, job, create_and_delete_users):
        allure.dynamic.title(allure_title)
        nickname = create_and_delete_users
        data = {"age": age, "job": job}
        response = self.api_users.update_users_by_nickname(nickname=nickname, **data)
        assert response.status_code == 200, response.json()

    @allure.feature("put_users")
    @pytest.mark.parametrize(
        "allure_title, nickname, age, job, expected_status_code ",
        [
            ("Негативная проверка обновления данных о пользователе, nickname пустой", "", 50, text_generator(5), 405),
            ("Негативная проверка обновления данных о пользователе, nickname рандомные символы", text_generator(5), 50,
             text_generator(5), 404),
            ("Негативная проверка обновления данных о пользователе, age 0", None, 0, text_generator(5), 400),
            ("Негативная проверка обновления данных о пользователе, age 100", None, 100, text_generator(5), 400),
            ("Негативная проверка обновления данных о пользователе, age пустая строка", None, "", text_generator(5),
             400),
            ("Негативная проверка обновления данных о пользователе, age символы рандомные", None, text_generator(10),
             text_generator(5), 400),
            ("Негативная проверка обновления данных о пользователе, age 1.5", None, 1.5, text_generator(5), 400),
            ("Негативная проверка обновления данных о пользователе, age 0.999999", None, 0.999999, text_generator(5),
             400),
            ("Негативная проверка обновления данных о пользователе, age 1.000001", None, 1.000001, text_generator(5),
             400),
            ("Негативная проверка обновления данных о пользователе, job 0", None, 50, "", 400),
            ("Негативная проверка обновления данных о пользователе, job 101", None, 50, text_generator(101), 400),
        ]
    )
    def test_negative_put_users(self, allure_title, nickname, age, job, create_and_delete_users, expected_status_code):
        allure.dynamic.title(allure_title)
        if nickname is None:
            nickname = create_and_delete_users
        data = {"age": age, "job": job}
        response = self.api_users.update_users_by_nickname(nickname=nickname, **data)
        assert response.status_code == expected_status_code, response.json()
