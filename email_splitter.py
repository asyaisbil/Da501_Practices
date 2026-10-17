email = input("Your e-mail:")
if email.count("@") == 1:
    if email[0] != "@" or email[-1] != "@":
        idx_at = email.index("@")
        if email[idx_at+1:].count(".") >= 1:
            idx_dot = email.index(".")
            if len(email[idx_dot+1:]) == 2 or len(email[idx_dot+1:]) == 3:
                username = email.split("@")[0]
                domain = email.split("@")[1]
                print(username, domain, end="\n")
            else:
                print("Invalid e-mail!")
        else:
            print("Invalid e-mail!")
    else:
        print("Invalid e-mail!")
else:
    print("Invalid e-mail!")


email = input("Please enter an e-mail address: ")
valid = False
if email.count("@") == 1 and email[0] != "@" and email[-1] != "@":
    parts = email.split("@")
    domain = parts[1]
    if "." in domain:
        last = domain.split(".")[-1]
        if 2 <= len(last) <= 3 and last.isalpha():
            valid = True
if valid:
    print(parts[0])
    print(domain)
else:
    print("Invalid e-mail!")
