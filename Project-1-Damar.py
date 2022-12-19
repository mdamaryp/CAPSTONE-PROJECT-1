dataPelajar = {
'202201': {
    "Nama" : "Damar", 
    "Gender" : 'L',
    'Kelas':'A', 
    'Nilai':{
        'Mat':90,
        'Bindo':80,
        'Ipa':70}
        },
'202202': {
    "Nama" : "Yulian",
    "Gender" : 'P',
    'Kelas':'A', 
    'Nilai':{
        'Mat':60,
        'Bindo':80,
        'Ipa':70}
        },
'202203': {
    "Nama" : "Prakarsa",
    "Gender" : 'L',
    'Kelas':'B', 
    'Nilai':{
        'Mat':70,
        'Bindo':75,
        'Ipa':70}
        },
'202204': {
    "Nama" : "M. Bayu",
    "Gender" : 'L',
    'Kelas':'B', 
    'Nilai':{
        'Mat':90,
        'Bindo':80,
        'Ipa':70}
        },
'202205': {
    "Nama" : "L. Messi",
    "Gender" : 'L',
    'Kelas':'C', 
    'Nilai':{
        'Mat':90,
        'Bindo':80,
        'Ipa':70}
        },
'202206': {
    "Nama" : "Firman",
    "Gender" : 'L',
    'Kelas':'C', 
    'Nilai':{
        'Mat':90,
        'Bindo':80,
        'Ipa':70}
        }

}


def cetakHeader():
    print('==================== Daftar Siswa ====================\n')
    print('NIS\t| Nama  \t| Gender \t| Kelas\t| Mat\t| BIndo\t| IPA')

#func
def tampilData(IndextampilData):
    if IndextampilData == '1':
        if len(dataPelajar) == 0:
            print('\t Belum ada data')
        else:
            cetakHeader()
            for i in dataPelajar:
                print(f"{i}\t| {dataPelajar[i]['Nama']}  \t| {dataPelajar[i]['Gender']}\t\t| {dataPelajar[i]['Kelas']} \t| {dataPelajar[i]['Nilai']['Mat']} \t| {dataPelajar[i]['Nilai']['Bindo']} \t| {dataPelajar[i]['Nilai']['Ipa']}")
    
    elif IndextampilData == '2':
        noNIS=input('Masukan Nomor NIS yang ingin dilihan : ')
        if noNIS in dataPelajar:
            cetakHeader()
            print(f"{noNIS}\t| {dataPelajar[noNIS]['Nama']}  \t| {dataPelajar[noNIS]['Gender']}\t\t| {dataPelajar[noNIS]['Kelas']} \t| {dataPelajar[noNIS]['Nilai']['Mat']} \t| {dataPelajar[noNIS]['Nilai']['Bindo']} \t| {dataPelajar[noNIS]['Nilai']['Ipa']}")
        else:
            print(f'''
            =======================================
            NIS {noNIS} BELUM TERDAFTAR PADA SISTEM
            =======================================''')
        
    elif IndextampilData == '3':
        datKelas=input('Masukan Kelas yang ingin dilihat : ')
        cetakHeader()
        listKelas=[]

        for i in dataPelajar:
            for j in dataPelajar[i]['Kelas']:
                listKelas.append(j)
        
        if datKelas.upper() in listKelas:
            for i in dataPelajar:
                if dataPelajar[i]['Kelas'] == datKelas.upper():
                    print(f"{i}\t| {dataPelajar[i]['Nama']}  \t| {dataPelajar[i]['Gender']}\t\t| {dataPelajar[i]['Kelas']} \t| {dataPelajar[i]['Nilai']['Mat']} \t| {dataPelajar[i]['Nilai']['Bindo']} \t| {dataPelajar[i]['Nilai']['Ipa']}")
        else:
            print(f''' 
            =================================================
            Data Kelas {datKelas} BELUM TERDAFTAR PADA SISTEM
            =================================================''')


def hapusData():
    tampilData('1')
    nis = str(input('Masukkan NIS siswa yang ingin dihapus : '))
    if nis in dataPelajar:
        while True:
            konfirmasi_hapus = input(f'Apakah anda yakin ingin menghapus data siswa dengan NIS {nis}? ketikan Y/T : ')
            if konfirmasi_hapus.lower() == 'y':
                del dataPelajar[nis]
                break
            elif konfirmasi_hapus.lower() == 't':
                subMenu3()
                break
            else:
                print('''
                ===================================
                Masukan Konfirmasi dengan benar Y/T
                ===================================
                ''')
    else:
        print('''
        ===========================================================================
        NIS yang anda masukan tidak ada yang sesuai. Silahkan input NIS yang sesuai
        ===========================================================================
        ''')
    print('Daftar siswa\n')
    tampilData('1')


def inputData():
    lanjut1=''
    lanjut2=''
    while True:
        nis = input('Masukkan NIS Pelajar : ')
        if nis in dataPelajar:
            print(f'''
        ===========================================
        Data dengan NIS {nis} sudah ada dalam data!
        ===========================================''')
            #home()
            break
        elif nis.isnumeric() == False:
            print(f'''
        =======================================
        Data NIS hanya bisa diisi dengan angka!
        =======================================''')
            break
        elif len(nis) != 6:
            print(f'''
        ===============================================
        NIS yang anda inputkan harus berisi 6 kode unik
        ===============================================''')
            break
        else:
            lanjut1='y'
            break
    
    while lanjut1 == 'y':
        nama = str(input('Masukkan Nama Siswa : '))
        while True:
            #Gender
            gender = str(input("Masukan Gender Siswa L / P: "))
            if gender.lower() == 'l' or gender.lower() == 'p':
                break

        while True:
            kelas = input('Masukan Kelas Siswa : ')
            if kelas.isalpha() == False:
                print('''
            ==============================
            Masukan kelas sebagai Alphabet 
            ==============================''')
            else:
                break

        while True:
            nilaiMat = input('Masukan Nilai Matematika : ')
            if nilaiMat.isnumeric() == False:
                print('Nilai hanya boleh angka 0 - 100 ')
            elif int(nilaiMat) > 100 or int(nilaiMat) < 0:
                print('Nilai hanya boleh range 0 - 100 ')
            else:
                break

        while True:
            nilaiBIndo = input('Masukan Nilai Bahasa Indonesia : ')
            if nilaiBIndo.isnumeric() == False:
                print('Nilai hanya boleh angka 0 - 100 ')
            elif int(nilaiBIndo) > 100 or int(nilaiBIndo) < 0:
                print('Nilai hanya boleh range 0 - 100 ')
            else:
                break

        while True:
            nilaiIPA = input('Masukan Nilai IPA : ')
            if nilaiIPA.isnumeric() == False:
                print('Nilai hanya boleh angka 0 - 100 ')
            elif int(nilaiIPA) > 100 or int(nilaiIPA) < 0:
                print('Nilai hanya boleh range 0 - 100 ')
            else:
                lanjut2='y'
                break
        lanjut1=''
    
    
    while lanjut2 =='y':
        konfir = input('''
        ================================================
        Apakah anda yakin melakukan input data ? Y/T : ''')
        if konfir.lower() == 'y':
            dataPelajar.update({
            nis:{
                'Nama': nama,
                'Gender': gender.upper(),
                'Kelas': kelas.upper(),
                'Nilai': {'Mat':int(nilaiMat),'Bindo':int(nilaiBIndo),'Ipa':int(nilaiIPA)}}
            })
            tampilData('1')
            break
        elif konfir.lower() == 't':
            tampilData('1')
            lanjut2=''
        else:
            print('''
                ===================
                Masukan jawaban Y/T 
                ===================''')


def updateData(jenisUbah):
    if jenisUbah == '1':
        nis = input('Masukan nis : ')
        if nis in dataPelajar:
            print(f"{nis}\t| {dataPelajar[nis]['Nama']}  \t| {dataPelajar[nis]['Gender']}\t\t| {dataPelajar[nis]['Kelas']} \t| {dataPelajar[nis]['Nilai']['Mat']} \t| {dataPelajar[nis]['Nilai']['Bindo']} \t| {dataPelajar[nis]['Nilai']['Ipa']}")
            while True:
                konfir = input('Apakah anda ingin melanjutkan update data tersebut, Y/T : ')
                if konfir.lower() == 'y':
                    nama = input('Masukkan Nama Siswa : ')
                    while True:
                        #Gender
                        gender = str(input("Masukan Gender Siswa L / P: "))
                        if gender == 'l' or gender == 'L' or gender == 'p' or gender == 'P':
                            break
                    
                    while True:
                        kelas = input('Masukan Kelas Siswa : ')
                        if kelas.isalpha() == False:
                            print('Masukan kelas sebagai Alphabet ')
                        else:
                            break
                    
                    
                    while True:
                        nilaiMat = input('Masukan Nilai Matematika : ')
                        if nilaiMat.isnumeric() == False:
                            print('Nilai hanya boleh angka 0 - 100 ')
                        elif int(nilaiMat) > 100 or int(nilaiMat) < 0:
                            print('Nilai hanya boleh range 0 - 100 ')
                        else:
                            break
                        
                    while True:
                        nilaiBIndo = input('Masukan Nilai Bahasa Indonesia : ')
                        if nilaiBIndo.isnumeric() == False:
                            print('Nilai hanya boleh angka 0 - 100 ')
                        elif int(nilaiBIndo) > 100 or int(nilaiBIndo) < 0:
                            print('Nilai hanya boleh range 0 - 100 ')
                        else:
                            break

                    while True:
                        nilaiIPA = input('Masukan Nilai IPA : ')
                        if nilaiIPA.isnumeric() == False:
                            print('Nilai hanya boleh angka 0 - 100 ')
                        elif int(nilaiIPA) > 100 or int(nilaiIPA) < 0:
                            print('Nilai hanya boleh range 0 - 100 ')
                        else:
                            break
                    
                    while True:
                        konfir = input('Apakah anda yakin ingin mengupdate data ini? Y/T : ')
                        if konfir.lower() == 'y':
                            dataPelajar.update({
                                nis:{
                                    'Nama': nama,
                                    'Gender': gender.upper(),
                                    'Kelas': kelas.upper(),
                                    'Nilai': {'Mat':nilaiMat,'Bindo':nilaiBIndo,'Ipa':nilaiIPA}}
                                })
                            tampilData('1')
                            print('''
                                ==============================
                                    DATA SUDAH TERUPDATE
                                ==============================
                                ''')
                            break
                        elif konfir.lower() == 't':
                            break
                    break
                elif konfir.lower() == 't':
                    print('''
                            ========================
                                BATAL DI UPDATE
                            ========================
                        ''')
                    break
        else:
            print('''
            ===================================================
                DATA NIS YANG ANDA INPUTKAN TIDAK TERDAFTAR
            ===================================================
            ''')


    elif jenisUbah == '2':
        nis = input('Masukan nis : ')
        if nis in dataPelajar:
            print(f"{nis}\t| {dataPelajar[nis]['Nama']}  \t| {dataPelajar[nis]['Gender']}\t\t| {dataPelajar[nis]['Kelas']} \t| {dataPelajar[nis]['Nilai']['Mat']} \t| {dataPelajar[nis]['Nilai']['Bindo']} \t| {dataPelajar[nis]['Nilai']['Ipa']}")
            while True:
                konfir = input('Apakah anda ingin melanjutkan update data tersebut, Y/T : ')
                if konfir.lower() == 'y':
                    while True:
                        subUpdate()
                        kolomPilihan = input('Masukan kolom data yang ingin di update : ')
                        kolomData=["Nama","Gender","Kelas","Nilai"]
                        kolomNilai=["Mat","Bindo","Ipa"]
                        if kolomPilihan.capitalize() in kolomData:
                            if kolomPilihan.capitalize() == 'Nilai':
                                subUpdateNilai()
                                kolomPilihNilai = input('Masukan Nilai yang akan di update : ')
                                if kolomPilihNilai.capitalize() in kolomNilai:
                                    while True:
                                        newNilai = input('Masukan Nilai Baru : ')
                                        if newNilai .isnumeric() == False:
                                            print('Nilai hanya boleh angka 0 - 100 ')
                                        elif int(newNilai ) > 100 or int(newNilai ) < 0:
                                            print('Nilai hanya boleh range 0 - 100 ')
                                        else:
                                            break
                                    konfir = input('Apakah anda yakin ingin mengupdate data ini? Y/T : ')
                                    if konfir.lower() == 'y':
                                        dataPelajar[nis][kolomPilihan.capitalize()][kolomPilihNilai.capitalize()] = int(newNilai)
                                        tampilData('1')
                                        print('''
                                            ==============================
                                                DATA SUDAH TERUPDATE
                                            ==============================
                                            ''')
                                        break
                                    elif konfir.lower() == 't':
                                        print('''
                                            ========================
                                                BATAL DI UPDATE
                                            ========================
                                            ''')
                                        break
                                    else:
                                        print('''
                                            =====================
                                                MASUKAN Y/T
                                            =====================
                                            ''')
                                break
                        
                        
                            elif kolomPilihan.capitalize() == 'Gender':
                                while True:
                                    valueBaru = input("Masukan Gender Siswa L / P: ").upper()
                                    if str(valueBaru.lower()) == 'l' or str(valueBaru.lower()) == 'p':
                                        break
                            
                            elif kolomPilihan.capitalize() == 'Nama':
                                valueBaru = input("Masukan pembaruan nama siswa : ").capitalize()
                            
                            elif kolomPilihan.capitalize() == 'Kelas':
                                while True:
                                    valueBaru = input('Masukan Kelas Siswa : ').upper()
                                    if valueBaru.isalpha() == False:
                                        print('Masukan kelas sebagai Alphabet ')
                                    else:
                                        break
                            
                            while True:
                                konfir = input('Apakah anda yakin ingin mengupdate data ini? Y/T : ')
                                if konfir.lower() == 'y':
                                    dataPelajar[nis][kolomPilihan.capitalize()] = valueBaru
                                    tampilData('1')
                                    print('''
                                        ==============================
                                            DATA SUDAH TERUPDATE
                                        ==============================
                                        ''')
                                    break
                                elif konfir.lower() == 't':
                                    print('''
                                        ========================
                                            BATAL DI UPDATE
                                        ========================
                                        ''')
                                    break
                        elif kolomPilihan == '0':
                            break
                        else:
                            print('''
                                        ==========================================
                                            Masukan kolom yang akan di update
                                            (Nama, Gender, Kelas, Nilai)
                                        ==========================================
                                        ''')
                    break
                elif konfir.lower() == 't':
                    break
        else:
            print('''
            ===================================================
                DATA NIS YANG ANDA INPUTKAN TIDAK TERDAFTAR
            ===================================================
            ''')


def nilaiAKhir():
    while True:
        nilaiMinimal = input('Masukan nilai minimum kelulusan : ')
        if nilaiMinimal.isnumeric() == False:
            print('Nilai hanya boleh angka 0 - 100 ')
        elif int(nilaiMinimal) > 100 or int(nilaiMinimal) < 0:
            print('Nilai hanya boleh range 0 - 100 ')
        else:
            break
    print('Daftar Siswa\n')
    print('NIS\t| Nama  \t\t| Gender \t| Kelas\t| Mat\t| Bindo\t| IPA\t| NILAI AKHIR\t| NILAI MINIMUM\t|STATUS KELULUSAN')
    print('=========================================================================================================================')
    
    for i in dataPelajar:
        status=''
        rata_nilai  = (f'{(int(dataPelajar[i]["Nilai"]["Mat"])+int(dataPelajar[i]["Nilai"]["Bindo"])+int(dataPelajar[i]["Nilai"]["Ipa"]))/len(dataPelajar[i]["Nilai"])}')
        if float(rata_nilai) >= int(nilaiMinimal):
            status = 'Lulus'
        else:
            status = 'Tidak Lulus'
        print(f"{i}\t| {dataPelajar[i]['Nama']}  \t\t| {dataPelajar[i]['Gender']}\t\t| {dataPelajar[i]['Kelas']} \t| {dataPelajar[i]['Nilai']['Mat']} \t| {dataPelajar[i]['Nilai']['Bindo']} \t| {dataPelajar[i]['Nilai']['Ipa']}\t| {round(float(rata_nilai),2)}\t\t| {nilaiMinimal}\t\t| {status}")


def home():
    print(f'''
        Selamat Datang di data Siswa

        List Fitur :
        1. Menampilkan data siswa
        2. Menambah data siswa
        3. Menghapus data siswa
        4. Update data siswa
        5. Review nilai
        6. Exit Program''')

def subUpdate():
    print(f'''
    =====================================================
        Kolom data yang akan dilakukan Update Data:
                Nama, Gender, Kelas, Nilai
        
                    0. Back Home

        Masukkan bagian apa yang ingin diupdate
    ====================================================== ''')

def subUpdateNilai():
    print(f'''
        Kolom data yang akan dilakukan Update Data Nilai
               inputkan sesuai nama di bawah ini
                    Mat , Bindo , Ipa
        
            Tekan 0 jika ingin kembali ke Home
                    0. Back Home


        Masukkan bagian apa yang ingin diupdate : ''')

def subMenu1():
    print(f'''
        List Fitur Read Data:
        1. Menampilkan Semua data siswa
        2. Menampilkan berdasarkan NIS data siswa
        3. Menampilkan berdasarkan Kelas data siswa
        0. Back Home
        ''')

def subMenu2():
    print(f'''
        List Fitur input Data:
        1. input data siswa
        0. Back Home
        ''')

def subMenu3():
    print(f'''
        List Fitur Hapus Data:
        1. Hapus data siswa
        0. Back Home
        ''')

def subMenu4():
    print(f'''
        List Fitur Update Data:
        1. Update Semua data siswa berdasarkan NIS
        2. Update data tertentu berdasarkan NIS
        0. Back Home
        ''')

def subMenu5():
    print(f'''
        Fitur olah data nilai:
        1. Menampilkan olah nilai data siswa
        0. Back Home
        ''')

def pilihOpsi():
    pilOp = input(f'''
    ================================
        Masukan pilihan anda : ''')
    return pilOp


exitId =''
while (True) and exitId =='' :
    home()
    pilihanMenu = input(f'''
    ================================
        Masukan pilihan menu : ''')
    
    if(pilihanMenu == '1') :
        while True:
            subMenu1()
            pilih = pilihOpsi()
            if pilih == '1':
                tampilData('1')
            elif pilih == '2':
                tampilData('2')
            elif pilih == '3':
                tampilData('3')
            elif pilih == '0':
                break
            else:
                print('''
            =================================
            MASUKAN PILIHAN MENU ANTARA 0 - 3
            =================================
                ''')
    elif(pilihanMenu == '2') :
        while True:
            subMenu2()
            pilih = pilihOpsi()
            if pilih == '1':
                inputData()
            elif pilih == '0':
                break
            else:
                print('''
            =================================
            MASUKAN PILIHAN MENU ANTARA 1 / 0
            =================================
                ''')
    elif(pilihanMenu == '3') :
        while True:
            subMenu3()
            pilih = pilihOpsi()
            if pilih == '1':
                hapusData()
            elif pilih == '0':
                break
            else:
                print('''
            =================================
            MASUKAN PILIHAN MENU ANTARA 1 / 0
            =================================
                ''')
    elif(pilihanMenu == '4') :
        while True:
            subMenu4()
            pilih = pilihOpsi()
            if pilih == '1':
                updateData('1')
            elif pilih == '2':
                updateData('2')
            elif pilih == '0':
                break
            else:
                print('''
            =================================
            MASUKAN PILIHAN MENU ANTARA 0 - 7
            =================================
                ''')
    elif(pilihanMenu == '5'):
        while True:
            subMenu5()
            pilih = pilihOpsi()
            if pilih == '1':
                nilaiAKhir()
            elif pilih == '0':
                break
            else:
                print('''
            =================================
            MASUKAN PILIHAN MENU ANTARA 1 / 0
            =================================
                ''')
    elif(pilihanMenu == '6') :
        while True:
            print('''Apakah anda ingin keluar program ? Y/T ''')
            pilih = pilihOpsi()
            if pilih.lower() == 't':
                break
            elif pilih.lower() == 'y':
                exitId ='0'
                break
            else:
                print('''
            =================================
            MASUKAN PILIHAN MENU ANTARA Y / T
            =================================
                ''')
    else:
        print(f'''
    ========================
        Masukan angka 1-6
    ========================''')
