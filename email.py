class Email():

    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    def mark_as_read(self):
        self.has_been_read = True

inbox = []

def populate_inbox(email_address, subject_line, email_content):
    email = Email(email_address, subject_line, email_content)
    inbox.append(email)

def list_emails():
    print('\nEMAILS:')
    for i, email in enumerate(inbox, 1):
        print(i, email.subject_line)
    print()

def read_email(i):
    print()             # i-1 for index number
    print(f'{inbox[i-1].subject_line}\t\t\t{inbox[i-1].email_address}')
    print('-'*80)
    print(inbox[i-1].email_content)
    inbox[i-1].mark_as_read()

populate_inbox('admin@hyperiondev.com', 
               'Welcome to HyperionDev!',
               '''Dear Student,
               \nWelcome to HyperionDev
               \nBest,\nHyperionDev'''
               )

populate_inbox('admin@hyperiondev.com', 
               'Your submission has been reviewed',
               '''Hi,
               \nYour submission was reviewed successfully
               \nRegards,\nHyperionDev'''
               )

populate_inbox('admin@hyperiondev.com', 
               'Thanks for showing up',
               '''Hi Student,
               \nOur event is now over. Thank you for coming.
               \nBest,\nHyperionDev'''
               )

while True:
    print('1. Read an email\n2. View unread emails\n3. Quit application')
    selection = input()
    if selection == '1':
        list_emails()
        try:
            print('Select number corresponding to email you want to read')
            email_selection = int(input())
            if email_selection <= 0 or email_selection > len(inbox):
                print('Error: Selected number out of range.\n')
            else:
                read_email(email_selection)
                print(f'\nEmail from {inbox[email_selection-1].email_address} marked as read')
                print()
        except ValueError:  # If typed input not a number
            print('Error: Input not a number.\n')        
    elif selection == '2':
        print('\nUNREAD EMAILS:')
        unread_emails = [email for email in inbox if not email.has_been_read]
        if not unread_emails:  # If no emails in unread_emails (empty list)
            print('Empty')
        else:
            for email in unread_emails:
                print(f'- {email.subject_line}')
        print()
    elif selection == '3':
        break
    else:
        print('Invalid choice. Please try again.')