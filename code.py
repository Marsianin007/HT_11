import requests
import random
link_users = "https://jsonplaceholder.typicode.com/users"
page = requests.get(link_users)
users = page.json()

posts_link = "https://jsonplaceholder.typicode.com/posts"
page = requests.get(posts_link)
posts_json = page.json()

posts_link = "https://jsonplaceholder.typicode.com/todos"
page = requests.get(posts_link)
todos_json = page.json()

posts_link = "https://jsonplaceholder.typicode.com/photos"
page = requests.get(posts_link)
photos_json = page.json()


def main_menu():
    for i in users:
        print("id: " + str(i["id"]), "name: " + i["name"], "username: " + i["username"])
    id_of_user = input("Виберіть id потрібного користувача: ")
    if not id_of_user.isdigit():
        print("Введіть будь ласка число\n")
        main_menu()
    try:
        id_of_user = int(id_of_user)
        if id_of_user > 10 or id_of_user < 1:
            print("Такого id немає\n")
            main_menu()
    except:
        None
    choice_of_action(id_of_user)


def choice_of_action(id_of_user):
    print("Виберіть дію:\n1. Повна інформацію про користувача\n2. Пости\n3. List 'to do'\n4. Рандомна картинка")
    number_to_do = input("Ваш вибір: ")
    if not number_to_do.isdigit():
        print("Введіть будь ласка число\n")
        choice_of_action(id_of_user)
    number_to_do = int(number_to_do)
    if number_to_do < 1 or number_to_do > 4:
        print("Такої дії немає\n")
        choice_of_action(id_of_user)
    if number_to_do == 1:
        all_info(id_of_user)
    if number_to_do == 2:
        print("")
        posts(id_of_user)
    if number_to_do == 3:
        tasks_to_do(id_of_user)
    if number_to_do == 4:
        random_picture(id_of_user)


def all_info(id_of_user):
    for i in users:
        if i["id"] == id_of_user:
            print("id: " + str(i["id"]))
            print("name: " + i["name"])
            print("username: " + i["username"])
            print("email: " + i["email"])
            print("Address ↓↓↓")
            for a in i["address"].items():
                if a[0] != "geo":
                    print(a[0] + ": " + a[1])
                else:
                    print("lat: " + a[1]["lat"])
                    print("lng: " + a[1]["lng"])
            print("phone: " + i["phone"])
            print("website: " + i["website"])
            print("Company ↓↓↓")
            for b in i["company"].items():
                print(b[0] + ": " + b[1])
    print("")
    choice_of_action(id_of_user)


def posts(id_of_user):
    print("Виберіть дію:\n1. Переглянути пости користувача\n2. Інформація про конкретний пост")
    choice_number = input("Ваш вибір:")
    if not choice_number.isdigit():
        print("Введіть число:")
        posts(id_of_user)
    choice_number = int(choice_number)
    if choice_number not in [1, 2]:
        print("Такої дії не існує")
        posts(id_of_user)

    if choice_number == 1:
        for i in posts_json:
            if i["userId"] == id_of_user:
                print("")
                print("id: " + str(i["id"]))
                print(i["title"])
    if choice_number == 2:
        post_number = input("Виберіть id посту, про який хочете отримати інформацію(всього 10 постів): ")
        if not post_number.isdigit():
            print("Введіть число будь-ласка")
            posts(id_of_user)
        post_number = int(post_number)
        if post_number < 1 or post_number > 10:
            print("Такого поста не існує")
            posts(id_of_user)

        post_number = (id_of_user - 1) * 10 + post_number
        for i in posts_json:
            if i["userId"] == id_of_user and i["id"] == post_number:
                print("ID: " + str(post_number))
                print("title: " + i["title"])
                print("text: " + i["body"])
                print("всього 5 коментарів")
                print("id коментарів: ")

        for comment_id in range(((id_of_user - 1) * 50 + post_number * 5 - 4), ((id_of_user - 1) * 50 + post_number * 5 + 1)):
            print(comment_id)
    print("")
    choice_of_action(id_of_user)


def tasks_to_do(id_of_user):
    print("Юзер має 20 завдань, які бажаєте подивитися\n1 - Невиконані\n2 - Виконані ")
    number_of_choise = input("Ваш вибір: ")
    if not number_of_choise.isdigit():
        print("Введіть число")
    number_of_choise = int(number_of_choise)
    if number_of_choise not in [1, 2]:
        print("Такої дії немає")
    if number_of_choise == 1:
        for i in todos_json:
            if i["userId"] == id_of_user and i["completed"] is False:
                print("id: " + str(i["id"]), "title: " + i["title"])

    if number_of_choise == 2:
        for i in todos_json:
            if i["userId"] == id_of_user and i["completed"] is True:
                print("id: " + str(i["id"]), "title: " + i["title"])
    print("")
    choice_of_action(id_of_user)


def random_picture(id_of_user):
    picture_id = random.randrange(5000)
    for i in photos_json:
        if i["id"] == picture_id:
            print(i["url"])
    print("")
    choice_of_action(id_of_user)


main_menu()