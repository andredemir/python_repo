import sqlite3
import string
from random import random
from cryptography.fernet import Fernet
from tkinter import *


def generatePasswort():
    passwort_zeichen = string.ascii_letters + string.digits + string.punctuation
    newPasswort = []
    newString = ""
    for i in range(0, 16):
        newPasswort.append(passwort_zeichen[int(random() * passwort_zeichen.__len__())])
    return newString.join(newPasswort)


db_name = "NewPasswords.db"
key = Fernet.generate_key()
fernet = Fernet(key)


def add_password(db_name, website, username):
    password = generatePasswort()
    encrypted_password = encrypt_password(password)
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("INSERT INTO passwords VALUES (?, ?, ?)", (website, username, encrypted_password))
    conn.commit()
    conn.close()


def create_table(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords
                 (website text, username text, password text)''')
    conn.commit()
    # Verbindung beenden
    conn.close()


def delete_password(db_name, website, username):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("DELETE FROM passwords WHERE website=? AND username=?", (website, username))
    conn.commit()
    conn.close()


def change_password(db_name, website, username, password):
    encrypted_password = encrypt_password(password)
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("UPDATE passwords SET password=? WHERE website=? AND username=?",
              (encrypted_password, website, username))
    conn.commit()
    conn.close()


def get_password(db_name, website, username):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT password FROM passwords WHERE website=? AND username=?", (website, username))
    result = c.fetchone()
    conn.close()
    if result:
        return decrypt_password(result[0])
    else:
        return None


def encrypt_password(password):
    encoded_password = password.encode()
    encrypted_password = fernet.encrypt(encoded_password)
    return encrypted_password


def decrypt_password(encrypted_password):
    decrypted_password = fernet.decrypt(encrypted_password)
    return decrypted_password.decode()


def main():
    create_table(db_name)
    delete_password(db_name, "www.google.de", "test")
    change_password(db_name, "www.google.de", "user", "babapasswort")
    add_password(db_name, "www.google.de", "user")


if __name__ == "__main__":
    main()
