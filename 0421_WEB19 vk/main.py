from pprint import pprint

from login_password import LOGIN, PASSWORD
import vk_api


def captcha_handler(captcha):
    key = input(f'{captcha.get_url()} \nВведите капчу из ссылки выше: ')
    return captcha.try_again(key)


def auth_handler():
    key = input('Введите полученный код:')
    remember_device = True
    return key, remember_device


def main():
    vk_session = vk_api.VkApi(LOGIN, PASSWORD,
                              auth_handler=auth_handler,
                              captcha_handler=captcha_handler
                              )
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as err_msg:
        print(err_msg)

        return
    vk = vk_session.get_api()
    response = vk.wall.get(count=0, offset=0)
    if response['items']:
        for i in response['items']:
            pprint(i)


if __name__ == '__main__':
    main()
