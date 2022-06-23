def transaksi():
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
        listharga = row[2]
    
    total = 0
    while True:
        a = int(input("Masukkan kode barang \t: ")) 
        b = int(input("Masukkan jumlah barang \t: "))
        while True :
            cursor.execute('''SELECT * from produk WHERE id_produk = %s'''%(a))
            orderbarang = cursor.fetchall()
            for x in orderbarang:
                hargabarang = x[2] * b
                hargaorder = hargabarang
                print(print(x[1]," : ", hargabarang))
                total += int(hargaorder)
                print("Total belanjaan : ",total)             
                again = str.upper(input("Apakah ingin menambah produk? (Y/T) : "))
                if again == "Y":
                    print()
                elif again == "T":
                    break
            break
        
        '''konfirmasi = str.upper(input("Konfirmasi pesanan : (Y/T)"))
        if konfirmasi == "Y":
            print("Y")
        else:
            print()
        '''

transaksi()