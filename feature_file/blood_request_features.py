




class BloodRequestFeatures:

    def menu(self):
        user_input = input('''
                ======================================================
                        WELCOME TO DONOR MANAGEMENT
                ======================================================
                        1. CREATE REQUEST
                        2. VIEW RQUEST
                        3. APPROVE REQUEST
                        4. REJECT REQUEST
                        5. BACK
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
                pass
            case _:

                print('Invalid input!')



BloodRequestFeatures_obj = BloodRequestFeatures()