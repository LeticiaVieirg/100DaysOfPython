AGENDA ={}

def show_contacts(): 
    if AGENDA:
        for contact in AGENDA:
            contact_search(contact)
            print('='*10)
    else: 
        print('=')
        print("There are no contacts registered in the adrees book!")

def contact_search (contact):
    try:
        print('Name: ', contact)
        print('Phone number: ', AGENDA[contact]['Phone nummber'])
        print('Email: ', AGENDA[contact]['Email'])    
    except KeyError:
        print('='*10)
        print(f'The contact {contact} is not in the Agenda!')
    except Exception as error: 
        print('An unexpected error happened.')
        print(error)
        
        register=input('Want to register? Y/N: ')
        if register=='Y':
            contact=input('Enter a name: ')
            phone_number=input('Enter a email: ')
            email=input('Enter a email: ')
            edit_contact(contact, phone_number, email)

        else:
            print('='*10)
            print('Back to menu...')

def edit_contact(contact, phone_number, email):
    AGENDA[contact]={
        'Phone Number': phone_number,
        'Email': email,
    }
    

def read_details_contact():
    phone_number = input('Enter a number: ')
    email = input('Enter a email: ')
    return phone_number, email


def include_edite_contact (contact, phone_number, email):
    AGENDA[contact] = {
        'Phone number': phone_number,
        'Email': email,
}
    save_agenda()
    print(f'===SUCESS==='
          f'\nContato: {contact.upper()} Added successfully! ')
    print('-' *20)
