from cryptography.fernet import Fernet


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            app, user, passw = data.split("|")
            print("app:", app, "| User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    app_name = input('Account Name: ')
    user_name = input('User Name: ')
    pwd = input("Password: ")


    with open('passwords.txt', 'a') as f:
        f.write(app_name + "|" + user_name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
'''
def master_key():
    master_key = 'thisismasterkey'
    with open('mpassword.txt', 'a') as f:
        f.write(fer.encrypt(master_key.encode()).decode() + "\n")

master_key()
'''
#reading master key from file

with open('mpassword.txt', 'r') as f:
    for line in f.readlines():
        data = line.rstrip()
        m_key = fer.decrypt(data.encode()).decode()

master_key = input('enter the master key: ')
if master_key == m_key:
    print('-'* 10 + "\n" + 'MENU' + "\n" + "1. ADD \n2. VIEW \n3. Quite" + "\n" + '-'*10)
    while True:

        mode = input(
            "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
        if mode == "q":
            break

        if mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid mode.")
            continue

else:
    print('better luck next timebla')

