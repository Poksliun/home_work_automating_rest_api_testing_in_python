import requests

# url = "https://playground.learnqa.ru/api/homework_cookie"
#
# response = requests.get(url)
#
# print(response.cookies.items())

# url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
# # header = {'user_agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:105.0) Gecko/20100101 Firefox/105.0"}
# header = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
#
#
# response = requests.get(url, headers=header)
# print(response.json())


some = "some.txt"


# def pars_some_txt(file_name: str) -> dict:
#     file = open(file_name, 'r')
#     start_str_list = file.read().split("\n")
#     midle_str_list = []
#     for elements in start_str_list:
#         if elements != '':
#             midle_str_list.append(elements)
#
#     params_dict = {}
#
#     for index in range(2, len(midle_str_list), 5):
#         params_dict[midle_str_list[index]] = {midle_str_list[index + 2]}
#         return params_dict

def pars_some_txt(file_name: str) -> list:
    file = open(file_name, 'r')
    start_str_list = file.read().split("\n")
    midle_str_list = []
    for elements in start_str_list:
        if elements != '':
            midle_str_list.append(elements)

    params_list = []
    params_dict = {}

    for index in range(2, len(midle_str_list), 5):
        a = str(midle_str_list[index])
        b = 1
        new_dict = {a: b}
        print(new_dict)
        params_list.append(params_dict)
    print(params_list)
    return params_list

a = pars_some_txt('some.txt')
# user_agent = str(*a[0])
# output_params = a[0][user_agent]
# print(output_params)