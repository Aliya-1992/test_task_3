
class Validator:

    @classmethod
    def assertion(cls, actual_status_code, expected_status_code):
        """
        Метод позволяет сравнить полученный статус код со статусом 201
        """

        assert actual_status_code == expected_status_code, \
            f'Полученный статус код: {actual_status_code} не совпадает с ожидаемым значением {expected_status_code}'
