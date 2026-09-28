from database_file.database import database_connection

class DonorServices:

  def register(self):
    donor_id = input('Enetr a donor id')
    donor_name = input('Enter a donor name:')
    donor_age = input('Enter a age:')
    donor_blood_type = input('Enter a donor blood type:')

    connection = database_connection()

    cursor = connection.cursor()

    donor_quary = '''
                INSERT INTO donor(donor_id, donor_name, donor_age, donor_bood_type)
                VALUES(%s,%s,%s,%s)
                '''

    cursor.execute(donor_quary,donor_id,donor_name,donor_age,donor_blood_type)

    print('Data inserted sucessfully:')


    connection.commit()
    cursor.close()

  def view_donor(self):

    user_input = input('Enter a view donor name:')
    user_other = input('Enter a other table name:')


    connection = database_connection()

    cursor = connection.cursor()

    view_Quary = '''
                SELECT * 
                FROM donor
                '''
    donor = cursor.fetchall()
    if not donor:
      print('Donor not found:')
    else:
      for num in donor:
        print(num)
    connection.close()



    def update_donor(self):
      donor_id = input('Enetr a donor id')
      donor_name = input('Enter a donor name:')
      donor_age = input('Enter a age:')
      donor_blood_type = input('Enter a donor blood type:')



      donor_quary = '''
                  UPDATE donor
                  SET donor_id = ?,
                  donor_name = ?, 
                  donor_age = ?,
                  donor_blood_type = ?
                  WHERE donor_id = ? 
                  '''
      cursor.execute(donor, (donor_id,donor_name,donor_age,donor_blood_type))



    def delete_donor(self):



      sql_quary = '''
                  DELETE FROM donor
                  WHERE donor_id = ?
                  '''
      pass


    def back_menu(self):


      pass





    




    