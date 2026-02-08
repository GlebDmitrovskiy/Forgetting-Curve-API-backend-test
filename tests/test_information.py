from config.base_test import BaseTest
from services.text_generator import text_generator
from services.forgetting_curve.users.digit_generator import digit_generator
import pytest
import allure


class TestInformation(BaseTest):
    @pytest.fixture
    def create_and_delete_information(self):
        generated_nickname = text_generator(10)
        data = {"nickname": generated_nickname, "first_name": text_generator(10), "last_name": text_generator(10),
                "age": digit_generator(50), "job": text_generator(50)}
        self.api_users.create_users(**data)
        response = self.api_information.create_information(nickname=generated_nickname, information=text_generator(15),
                                                           explanation=text_generator(100))
        print(response.json())
        yield generated_nickname
        response_get = self.api_information.get_information(nickname=generated_nickname)
        data = response_get.json()
        if data:
            dict_get = response_get.json()[0]
            response_id = dict_get["id"]
            self.api_information.delete_information(nickname=generated_nickname, information_id=response_id)

    @allure.feature("Добавление информации пользователя")
    @allure.story("Позитивная проверка создания информации пользователя")
    @pytest.mark.parametrize("allure_title, information, explanation",
                             [("Позитивная проверка создания информации, information 1 символ", text_generator(1),
                               text_generator(100)),
                              ("Позитивная проверка создания информации, information 30 символов", text_generator(30),
                               text_generator(100)),
                              ("Позитивная проверка создания информации, explanation 1 символ", text_generator(15),
                               text_generator(1)),
                              ("Позитивная проверка создания информации, explanation 200 символов", text_generator(15),
                               text_generator(200))
                              ])
    def test_positive_create_information(self, allure_title, information, explanation):
        allure.dynamic.title(f"{allure_title}")
        generated_nickname = text_generator(10)
        with allure.step(f"Подготовка создания пользователя {generated_nickname}"):
            data = {"nickname": generated_nickname,
                    "first_name": text_generator(10),
                    "last_name": text_generator(10),
                    "age": digit_generator(50),
                    "job": text_generator(50)
                    }
            self.api_users.create_users(**data)
        with allure.step("Создание информации у пользователя"):
            data_post_information = {"information": information, "explanation": explanation}
            post_response = self.api_information.create_information(nickname=generated_nickname,
                                                                    **data_post_information)
            assert post_response.status_code == 200
        with allure.step(f"Удаление пользователя по id и никнейму:{generated_nickname}"):
            response_get = self.api_information.get_information(nickname=generated_nickname)
            dict_get = response_get.json()[0]
            response_id = dict_get["id"]
            self.api_information.delete_information(nickname=generated_nickname, information_id=response_id)

    @allure.feature("Негативное добавление информации у пользователя")
    @allure.story("Негативная проверка создания информации пользователя")
    @pytest.mark.parametrize("allure_title, information, explanation",
                             [("Негативная проверка создания информации, information 0 символов", "",
                               text_generator(100)),
                              ("Негативная проверка создания информации, information 31 символ", text_generator(31),
                               text_generator(100)),
                              ("Негативная проверка создания информации, information число", 1488,
                               text_generator(100)),
                              ("Негативная проверка создания информации, information float", 14.88,
                               text_generator(100)),
                              ("Негативная проверка создания информации, information bool", True,
                               text_generator(100)),
                              ("Негативная проверка создания информации, explanation 0 символов", text_generator(15),
                               ""),
                              ("Негативная проверка создания информации, explanation 201 символ", text_generator(15),
                               text_generator(201)),
                              ("Негативная проверка создания информации, explanation число", text_generator(15),
                               digit_generator(200)),
                              ("Негативная проверка создания информации, explanation float", text_generator(15),
                               14.88),
                              ("Негативная проверка создания информации, explanation bool", text_generator(15),
                               True),
                              ])
    def test_negative_create_information(self, allure_title, information, explanation):
        allure.dynamic.title(f"{allure_title}")
        generated_nickname = text_generator(10)
        with allure.step(f"Подготовка к созданию пользователя:{generated_nickname}"):
            data = {"nickname": generated_nickname, "first_name": text_generator(10), "last_name": text_generator(10),
                    "age": digit_generator(50), "job": text_generator(50)}
            self.api_users.create_users(**data)
        with allure.step(f"Создание информации пользователя:{generated_nickname}"):
            data_post_information = {"information": information, "explanation": explanation}
            post_response = self.api_information.create_information(nickname=generated_nickname,
                                                                    **data_post_information)
            assert post_response.status_code == 400

    @allure.feature("Управление информацией")
    @allure.story("Получение информации пользователя")
    def test_get_information(self, create_and_delete_information):
        nickname = create_and_delete_information
        allure.dynamic.title(f"Получение информации пользователя по никнейму:{nickname}")
        with allure.step(f"Запрос получения информации пользователя:{nickname}"):
            response = self.api_information.get_information(nickname=nickname)
            print(response.json())
            assert response.status_code == 200

    @allure.feature("Удаление информации")
    @allure.story("Проверка удаления информации пользователя")
    def test_delete_information(self, create_and_delete_information):
        with allure.step("Получение информации у пользователя"):
            response_get = self.api_information.get_information(nickname=create_and_delete_information)
        with allure.step("Извлечение id из получения информации для последующего удаления её"):
            dict_get = response_get.json()[0]
            response_id = dict_get["id"]
            response_delete = self.api_information.delete_information(nickname=create_and_delete_information,
                                                     information_id=response_id)
            print(response_delete.json())
            assert response_delete.status_code == 200
        with allure.step("Проверка что пользователь удалился"):
            get_user = self.api_information.get_information(nickname=create_and_delete_information)
            assert len(get_user.json()) == 0
