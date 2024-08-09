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

def delete_contact(contact):
    try:
        AGENDA.pop(contact)
        save_agenda()
        print('='*20)
        print(f'Contact {contact} deleted sucessfully!')
        print('='*20)
        
    except KeyError:
        print('='*20)
        print('Non-existent contact.')
    except Exception as error:
        print('Unexpeted error.')
        print(error)

def export_contacts(file_agenda):
    try: 
        with open(file_agenda, 'w') as file:
            for contact in AGENDA:
                phone_number=AGENDA[contact]['Phone Number']
                email=AGENDA[contact]['Email']
                file.write(f'{contact}, {phone_number}, {email}\n')
            print('Exported Agenda successfully!')
    except Exception as error:
        print('Error exporting contacts.')
        print(error)


def save_agenda():
    export_contacts('database.csv')


def import_contacts (file_agenda):
    try: 
        with open(file_agenda, 'r') as file:
            lines=file.readlines()
            for line in lines:
                details=line.strip().split(',')

                name=details[0]
                phone_number=details[1]
                email=details[2]

                include_edite_contact(name, phone_number, email)
    except FileNotFoundError:
        print('File dont founded.')
    except Exception as error:
        print('Unexpedted error. ')
        print(error)
        
def load_agenda():
    try:
        with open('database.csv', 'r') as file:
            lines=file.readlines()
            for line in lines:
                details=line.strip().split(',')
                
                name=details[0]
                phone_number=details[1]
                email=details[2]

                AGENDA[name]={
                    'Phone Number': phone_number,
                    'Email'=email
                }
            print('Load database sucessfully. ')
            print('f{len(AGENDA)} Loaded contacts')
    except FileNotFoundError: 
        print('File not founded.')
    except Exception as error:
        print('Unexpedted error.')
        print(error)

def menu():
    print('='*20)
    print('1 - Show contacts in agenda')
    print('2 - Search contact')
    print('3 - Include contact')
    print('4 - Edit contact')
    print('5 - Delete contact')
    print('6 - Export contact for CSV. ')
    print('7 - Import contact for CSV. ')
    print('0 - Close Agenda')
    print('-' * 20)


    load_agenda()
    while True:
        menu()

        option=input('Choice a option: ')
        if option =='1':
            show_contacts()
        elif option =='2':
            contact=input('Enter a name of the contact: ')
            contact_search(contact)
        elif option =='3':
            contact=input('Enter a name of the contact: ')
            
            try:
                AGENDA[contact]
                print('Existing contact.')
            except KeyError:
                phone_number, email=read_details_contact()
                include_edite_contact(contact, phone_number, email)
        elif option=='4':
            contact=input('Enter a name of the contact: ')

            try: 
                AGENDA[contact]
                print('Editing existing contact. ', contact)
                phone_number, email=read_details_contact()
                include_edite_contact(contact, phone_number, email)
            except KeyError:
                print('Unexpeted contact. ')
    
    elif option == '5':
        contact = input('Enter a name of the contact: ')
        delete_contact(contact)
    elif opcao == '6':
        file_agenda = input('Enter a name of the exported file: ')
        export_contacts(file_agenda)
    elif opcao == '7':
        file_agenda = input('Enter a name of the imported file:  ')
        import_contacts(file_agenda)
    elif opcao == '0':
        print('=' * 20)
        print('Close program.')
        print('=' * 20)
        break
    else:
        print('Invalid option. ')









