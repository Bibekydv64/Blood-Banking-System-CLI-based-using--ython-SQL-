import mysql.connector as sql

def database_connection():

    connection = sql.connect(
                    host = 'localhost',
                    user = 'root',
                    database = 'blood_banking_database'
                            )

    cursor = connection.cursor()

    registration_table = '''
                CREATE TABLE IF NOT EXISTS registration
                (
                registration_ID INTEGER AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(256) NOT NULL,
                password VARCHAR(256) NOT NULL,
                email VARCHAR(256) UNIQUE NOT NULL,
                gender VARCHAR(256) NOT NULL,
                age INTEGER NOT NULL
                )
                '''

    doner_table_quary = '''
        CREATE TABLE IF NOT EXISTS donor
                (
                donor_id INTEGER NOT NULL PRIMARY KEY,
                donor_name VARCHAR(256) NOT NULL,
                donor_email VARCHAR(256) NOT NULL,
                donor_age INTEGER NOT NULL,
                donor_bood_type VARCHAR(256) NOT NULL
                )
                '''
                
    inventory_collection_table_quary = '''
            CREATE TABLE IF NOT EXISTS inventory_collection
                    (
                    blood_id INTEGER AUTO_INCREMENT PRIMARY KEY,
                    blood_type VARCHAR(256) NOT NULL,
                    blood_quality INTEGER NOT NULL
                    )
                    '''
 
    request_table_quary = '''
                    CREATE TABLE IF NOT EXISTS request
                            (
                            request_id INTEGER AUTO_INCREMENT PRIMARY KEY,
                            hospital_name VARCHAR(256) NOT NULL,
                            patient_name VARCHAR(256) NOT NULL,
                            patient_age INTEGER NOT NULL,
                            patient_blood_type VARCHAR(256) NOT NULL,
                            donor_name VARCHAR(256) NOT NULL,
                            donor_age INTEGER NOT NULL,
                            donor_blood_type VARCHAR(256) NOT NULL
                            )
                            '''

        
    cursor.execute(registration_table)
    cursor.execute(doner_table_quary)
    cursor.execute(inventory_collection_table_quary)
    cursor.execute(request_table_quary)

    connection.commit()
    cursor.close()
    print('connection sucessfully')

    return connection


if __name__ == '__main__':
    database_connection()




    

    