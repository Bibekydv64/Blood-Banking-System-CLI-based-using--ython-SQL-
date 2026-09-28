from database_file.database import database_connection



class Signup:

    def signup(self):
        print("====WELCOME TO RESISTATION=======")
        name = input('Enter a Name:')
        password = input('Enter a Password:')
        email = input('Enter a Email:')
        gender = input('enter a gender:')
        age = input('Enter a age:')


        connection = database_connection()

        cursor = connection.cursor()

        signup_quary1 = '''
                    INSERT INTO registration(name, password, email, gender, age)
                    VALUES(%s,%s,%s,%s,%s)
                        '''

        cursor.execute(signup_quary1,(name,password,email,gender,age))

        connection.commit()
        cursor.close()
        connection.close()



Signup_obj = Signup()

        



