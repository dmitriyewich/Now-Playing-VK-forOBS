import vk_api # $ pip3 install vk_api

from time import sleep

TOKEN = ''	# токен юзера(не группы!)
test = ''
vk_session = vk_api.VkApi(token = TOKEN)
try:
    vk = vk_session.get_api()
    try:
        while True:
                if test == vk.status.get()['text']:
                    sleep(1)
                else:
                    test = vk.status.get()['text']
                    print(f"{vk.status.get()['text']}        ")
                    my_file = open("Now-Playing-VK-forOBS.txt", "w",  encoding='UTF-8')
                    my_file.write(f"Сейчас играет: {vk.status.get()['text']}         ")
                    my_file.close()
                    sleep(1)
    except KeyboardInterrupt:
        exit()
except vk_api.AuthError as error_msg:
    print(error_msg)
