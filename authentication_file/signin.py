from database_file.database import database_connection
from Signup import Signup_obj


class SignIn:

    def signin(self):
        username_input = input('Enter username:')
        userpassword_input = input('Enter password:')

        connection = database_connection()
        cursor = connection.cursor()

        signin_quary1 = '''
                        SELECT name, password
                        FROM registration
                        WHERE name = %s and password = %s
                        '''
        cursor.execute(signin_quary1,(username_input, userpassword_input))

        result = cursor.fetchone()

        if result:
            print('login Sucessfully:')

        else:
            Signup_obj.signup()
            

SignIn_obj = SignIn()
