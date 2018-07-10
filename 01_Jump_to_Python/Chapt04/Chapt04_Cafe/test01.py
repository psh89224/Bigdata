import sys
usernames = sys.argv[1:]

def greet_users(usernames):

    for i in usernames:
        print("Hello %s%s!" %(i[:1].upper(), i[1:]))

greet_users(usernames)