import pytest
import requests

class TestHomeWork():

    user_agent = [
                   {
                   'Mozilla/5.0'
                   ' (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) '
                   'AppleWebKit/534.30 (KHTML, like Gecko)'
                   ' Version/4.0 Mobile Safari/534.30':
                       {
                        'platform': 'Mobile',
                        'browser': 'No',
                        'device': 'Android'
                       }
                   },
                  {
                   "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X)"
                   " AppleWebKit/605.1.15 (KHTML, like Gecko)"
                   " CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1":
                       {
                        'platform': 'Mobile',
                        'browser': 'Chrome',
                        'device': 'iOS'
                       }
                   },
                  {
                   'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)':
                       {
                        'platform': 'Googlebot',
                        'browser': 'Unknown',
                        'device': 'Unknown'
                       }
                   },
                  {
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0':
                       {
                        'platform': 'Web',
                        'browser': 'Chrome',
                        'device': 'No'
                       }
                  }
                  ]

    # # Проверка, что сообщение переданное через консоль короче 15 символов
    # def test_input_len(self):
    #     message = input("Set a message: ")
    #     assert len(message) <= 15, "Длина сообшения больше 15 символов."

    # def test_cookie_request(self):
    #
    #     url = "https://playground.learnqa.ru/api/homework_cookie"
    #     response = requests.get(url)
    #     cookie = response.cookies.get('HomeWork')
    #     print("Фактическое значение cookie: '%s'" % cookie)
    #     assert cookie == 'hw_value', f"Предполагаемое (hw_value) и фактическое ({cookie}) значение cookie не совпадают"

    # def test_reauest_header(self):
    #
    #     required_header = "Some secret value"
    #     url = "https://playground.learnqa.ru/api/homework_header"
    #     response = requests.get(url)
    #     checked_header = response.headers['x-secret-homework-header']
    #     print("Фактическое значение header: '%s'" % checked_header)
    #
    #     assert checked_header == required_header, "Предполагаемое (%s) и" \
    #                                               " фактическое (%s) значение cookie не совпадают"\
    #                                               % (required_header, checked_header)

    @pytest.mark.parametrize("user_param", user_agent)
    def test_the_definition_of_a_user_agent(self, user_param):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        response = requests.get(url, headers={'User-Agent': str(*user_param)})

        for param_key in user_param.keys():
            assert "user_agent" in response.json()
            assert param_key == response.json()['user_agent']
            for param in user_param[param_key].keys():
                assert param in response.json()
                assert user_param[param_key][param] == response.json()[param]

