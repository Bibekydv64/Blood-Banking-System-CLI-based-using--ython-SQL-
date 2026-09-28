from authentication_file.signin import SignIn_obj
from authentication_file.Signup import Signup_obj




class loginSignupInterface:

    def __init__(self):
        self.menu()

    def __str__(self):
        print(f'WELCOME TO BLOOD BANKING SYSTEM')

    def menu(self):
        user_input = input('''
                    ================================
                          WELCOME TO registration
                    ================================

                            1.Signin
                            2.signup
                            
                            ''')
        match user_input:
            case '1':
                
                SignIn_obj.signin()

            case '2':
                Signup_obj.signup()

            case _:
                print('Input Invalid!')



loginSignupInterface_obj =  loginSignupInterface()

print(loginSignupInterface)