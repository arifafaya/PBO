class Kasir:
    def __init__(self, idlogin = None, passwordlogin = None, namakasirlogin = None, teleponkasirlogin = None) :
        self.idlogin = idlogin
        self.passwordlogin = passwordlogin
        self.namakasirlogin = namakasirlogin
        self.teleponkasirlogin = teleponkasirlogin

    def loginKasir(self):
        try:
            import mysql.connector
            conn = mysql.connector.connect(
            host = 'localhost',
            database = 'kelompok2_kasir',
            user = 'root',
            password = ''
            )
            cursor = conn.cursor()
            print("==============")
            print("LOGIN AS ADMIN")
            print("==============")
            idconfirm = input("Masukkan ID : ")
            passwordconfirm = input("Masukkan Password : ")
            cursor.execute('''SELECT * from adminkasir WHERE id_kasir = %s'''%(idconfirm))
            resultlogin = cursor.fetchall()
            for row in resultlogin:
                self.idlogin = row[0]
                self.passwordlogin = row [1]
                self.namakasirlogin = row[2]
                self.teleponkasirlogin = row[3]
                if str(self.idlogin) == str(idconfirm) and str(self.passwordlogin) == (passwordconfirm) :
                    print("\nLogin Berhasil\n")
                else:
                    print("\nPassword Salah\n")
        except:
            print("\nPassword Salah\n")

        
Kasir().loginKasir()