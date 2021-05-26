from DatabaseUpdater import users_id_list, add_new_user


class User:
    def __init__(self):
        pass

    def handle_message(self, chat_id, first_name, last_name, message, type="default"):
        print(message)

    def exist_in_db(self, chat_id):
        return chat_id in users_id_list()

    def add_in_db(self, chat_id, first_name, last_name, vip=0):
        add_new_user(chat_id, first_name, last_name, vip)

    def check_and_add(self, chat_id, first_name, last_name, vip=0):
        if not self.exist_in_db(chat_id):
            self.add_in_db(chat_id, first_name, last_name, vip)

def check_and_add(chat_id, f_name, s_name, vip=0):
    if (chat_id,) not in users_id_list():
        add_new_user(chat_id, f_name, s_name, vip)
