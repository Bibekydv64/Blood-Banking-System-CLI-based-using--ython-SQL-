


class DonorManagement:

    def menu(self):
        user_input = input('''
                ======================================================
                        WELCOME TO DONOR MANAGEMENT
                ======================================================
                        1. REGISTER DONOR
                        2. VIEW DONORS
                        3. UPDATE DONOR
                        4. DELETE DONOR
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



DonorManagement_obj = DonorManagement()