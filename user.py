class User:
    def __init__(self, telegram_id, name=None, email=None):
        self.telegram_id = telegram_id
        self.name = name
        self.name = email

    def save_to_db(self):
        create_user(self.telegram_id, )