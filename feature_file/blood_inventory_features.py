



class BloodInventery:

    def menu(self):
        user_input = input('''
                ======================================================
                        WELCOME TO BLOOD INVENTORY MANAGEMENT
                ======================================================
                        1. ADD BLOOD
                        2. VIEW DONORS STOCK
                        3. SEARCH BLOOD
                        4. REMOVE DONOR
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




BloodInventery_obj = BloodInventery()