class Produk:
    def __init__(self) -> None:
        pass
        
    def tampilProduk(self):
        import mysql.connector
        conn = mysql.connector.connect(
        host = 'localhost',
        database = 'kelompok2_kasir',
        user = 'root',
        password = ''
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produk")
        myresult = cursor.fetchall()
        print("=======================================================================")
        print("=============================Daftar Produk=============================")
        print("=======================================================================")
        print("ID \t\t\t Nama Produk \t\t\t Harga")
        for row in myresult:
            print(row[0],"\t\t\t",row[1],"\t\t",row[2])

    def tambahProduk(self):
        try :
            import mysql.connector
            conn = mysql.connector.connect(
            host = 'localhost',
            database = 'kelompok2_kasir',
            user = 'root',
            password = ''
            )
            cursor = conn.cursor()

            print("=======================================================================")
            print("=============================Tambah Produk=============================")
            print("=======================================================================")
            produkbaru = input("Masukkan nama produk : ")
            hargabaru = int(input("Masukkan harga barang : "))
            print()
            print("Berhasil menambahkan produk")
            print()

            cursor.execute('INSERT INTO produk(nama_produk,harga)VALUES("%s", %i)'%(produkbaru, hargabaru))
            conn.commit()
        except :
            print("Terjadi Kesalahan Saat Memasukkan Data !")

    def editProduk(self):
        import mysql.connector
        conn = mysql.connector.connect(
        host = 'localhost',
        database = 'kelompok2_kasir',
        user = 'root',
        password = ''
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produk")
        myresult = cursor.fetchall()
        print("=======================================================================")
        print("=============================Update Produk=============================")
        print("=======================================================================")
        print("ID \t\t\t Nama Produk \t\t\t Harga")
        for row in myresult:
            print(row[0],"\t\t\t",row[1],"\t\t",row[2])
        print()
        idedit = int(input("Pilih ID produk yang akan diedit : "))
        namaedit = str(input("Masukkan nama produk : "))
        hargaedit = int(input("Masukkan harga baru : "))
        print("\nBerhasil mengupdate produk")
        cursor.execute('''UPDATE produk SET nama_produk = %s, harga = %i WHERE id_produk = %i '''%(namaedit,hargaedit,idedit))
        val = (namaedit, hargaedit, idedit)
        conn.commit()

    def hapusProduk(self):
        import mysql.connector
        conn = mysql.connector.connect(
        host = 'localhost',
        database = 'kelompok2_kasir',
        user = 'root',
        password = ''
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produk")
        myresult = cursor.fetchall()
        print("=======================================================================")
        print("==============================Hapus Produk=============================")
        print("=======================================================================")
        print("ID \t\t\t Nama Produk \t\t\t Harga")
        for row in myresult:
            print(row[0],"\t\t\t",row[1],"\t\t",row[2])
        print()
        idhapus = int(input("Pilih ID produk yang akan dihapus : "))
        cursor.execute('''DELETE from produk WHERE id_produk = %i '''%(idhapus))
        conn.commit()
        print()
        print("Data produk berhasil dihapus")



Produk().tambahProduk() 