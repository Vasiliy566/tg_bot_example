import sqlite3


def create_user(telegram_id, name, email):
    con = sqlite3.connect('users.db')
    cur = con.cursor()

    cur.execute(
        f"""
            INSERT INTO users
            (telegram_id, name, mail)
            VALUES({telegram_id}, '{name}', '{email}');
        """
    )
    con.commit()
    con.close()


def is_user_exists(telegram_id):
    con = sqlite3.connect('users.db')
    cur = con.cursor()

    res = cur.execute(
        f"""
           SELECT * FROM users WHERE telegram_id = {telegram_id};
        """
    )
    is_exists = res.fetchone() is not None
    con.close()
    return is_exists


def add_money_to_user(user_id, money_to_add):
    con = sqlite3.connect('users.db')
    cur = con.cursor()

    cur.execute(
        f"""
            UPDATE users
            SET balance = balance + {money_to_add}
            WHERE telegram_id={user_id};
        """
    )
    con.commit()
    con.close()


def get_user_balance(telegram_id):
    con = sqlite3.connect('users.db')
    cur = con.cursor()

    res = cur.execute(
        f"""
           SELECT balance FROM users WHERE telegram_id = {telegram_id};
        """
    )
    balance = res.fetchone()[0]
    con.close()
    return balance


if __name__ == "__main__":
    print(get_user_balance(124))
