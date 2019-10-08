
def get_emails():
    email=''
    listi= []
    while email!='q':
        email=input('Email address: ')
        if email !='q':
            listi.append(email)
    return listi

def get_names_and_domains(x):
    return [tuple(y.split('@')) for y in x]

# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)