


class InterfaceFeature:

    def menu(self):
        user_input = input('''
                    ==================================
                       WELCOME TO BLOOD BANK SYSTEM
                    ==================================
                    1. DONOR MANAGEMENT
                    2. BLOOD INVENTORY
                    3. BLOOD REQUEST
                    4. VIEW HISTORY
                    5. EXIST
                    CHOSE ONE:
                        ''')

        match user_input:
            case '1':
                pass

            case '2':
                pass

            case '3':
                pass

            case '4':
                pass

            case '5':
                print('Program Exit sucessfuly')

            case _:
                print('Invalid input!')




InterfaceFeature_obj = InterfaceFeature()
