email = input("Enter your personal or official email-id:").strip()
user_name = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
print("Your username is '{}' while domain name is '{}'".format(user_name,domain_name))
