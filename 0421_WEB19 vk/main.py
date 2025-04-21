from pprint import pprint

from login_password import LOGIN, PASSWORD
import vk_api


def main():
    vk_session = vk_api.VkApi(LOGIN, PASSWORD)
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



