import sqlite3
from sqlite3 import Error
import random
import string
import hashlib


def create_connection():
    """ create database connection to a SQLite db
    :return: Connection object or None
    """
    con = None
    try:
        con = sqlite3.connect('db1.db')
        # print(sqlite3.version)
    except Error as e:
        print(e)

    return con


def create_table(con, create_table_sql):
    """ create table
    :param con: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        cur = con.cursor()
        cur.execute(create_table_sql)
    except Error as e:
        print(e)


def create_user(con, user):
    """ create user and insert values into users table in the database
    :param con: Connection object
    :param user:
    :return: user id
    """
    sql = ''' INSERT INTO users(login, password, salt) VALUES (?,?,?) '''
    cur = con.cursor()
    cur.execute(sql, user)
    con.commit()
    return cur.lastrowid


def display_users(con):
    """ display all records in users table in the database
    :param con: Connection object
    """
    cur = con.cursor()
    cur.execute("SELECT * FROM users")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def truncate(con):
    """ truncate users table
    :param con: Connection object
    """
    cur = con.cursor()
    cur.execute("DELETE FROM users")


def ver_passwd(password):
    """ verify password
    :param password: password typed by user
    :return: boolean value whether the verification is complete and password is fine
    """
    if (len(password) >= 8  # length
            and any(char.isdigit() for char in password)  # check if password contains numbers
            and any(not c.isalnum() for c in password)  # check if password contains symbols
            and (not password.islower() and not password.isupper())  # check if contains lower- and uppercase
    ):
        return True
    else:
        return False


def generate_salt(size, chars=string.ascii_uppercase + string.ascii_lowercase):
    """ generate salt for every user in database
    :param size: length of salt
    :param chars: components of generated salt (lower- and uppercase characters)
    :return: randomly generated salt
    """
    return ''.join(random.choice(chars) for _ in range(size))


def generate_login(size, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    """ generate login for every user in database
    :param size: length of login
    :param chars: components of generated login (lower- and uppercase characters, numbers)
    :return: randomly generated login
    """
    return ''.join(random.choice(chars) for _ in range(size))


def password_collection():
    """ user types password twice until password meets requirements
    :return: password
    """

    print("Please give password containing lower- and uppercase characters, numbers, symbols and is at least 8 "
          "characters long. ")

    while True:
        inp1 = input("Give password: ")
        inp2 = input("Give password again: ")
        if inp1 == inp2:
            if ver_passwd(inp1):
                break
            else:
                print("Given password does not meet expectations. ")
        else:
            print("Given passwords do not match. ")

    return inp1


def create_salt():
    """ generate salt and add it to the password
    :return: salt and string containing password and salt
    """
    salt = generate_salt(10)
    return salt


salt = create_salt()


def add_salt_to_pass(salt):
    pswd = password_collection() + salt
    return pswd


def hash_salted_password():
    """ convert salted password into bytes and hash it
    :return: hashed password
    """
    pswd = add_salt_to_pass(salt)
    pswd_as_bytes = str.encode(pswd)
    h = hashlib.sha256()
    h.update(pswd_as_bytes)
    hashed_password = h.hexdigest()
    return hashed_password


def hash_salted_password_2():
    """ convert salted password and salt to bytes and hash the password using pbkdf2_hmac
    :return: hashed password
    """
    pswd = add_salt_to_pass(salt)
    pswd_as_bytes = str.encode(pswd)
    salt_as_bytes = str.encode(salt)
    dk = hashlib.pbkdf2_hmac('sha256', pswd_as_bytes, salt_as_bytes, 100000)
    hashed_password = dk.hex()
    return hashed_password


def insert_user(con):
    """ insert values of user(login, hashed password, salt) into the database
    :param con: Connection object
    """
    login = generate_login(8)
    password = hash_salted_password_2()
    user = (login, password, salt)
    user_id = create_user(con, user)


def main():
    """ create table of users, initialize connection, insert/display/truncate
    """
    sql_create_users_table = '''CREATE TABLE IF NOT EXISTS users(
                    id integer PRIMARY KEY,
                    login text NOT NULL,
                    password text NOT NULL,
                    salt text NOT NULL)'''

    con = create_connection()

    if con is not None:
        create_table(con, sql_create_users_table)
    else:
        print("Error - cannot connect to the database")

    with con:
        insert_user(con)
        display_users(con)
        # truncate(con)


if __name__ == '__main__':
    main()
