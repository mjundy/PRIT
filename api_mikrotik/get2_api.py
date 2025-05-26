from routeros_api import RouterOsApiPool

# Ganti IP, username, dan password sesuai dengan konfigurasi MikroTik kamu
host = '10.35.38.2'
username = 'get_api'
password = 'Frina123'  # ganti dengan password yang benar

try:
    # Buat koneksi ke MikroTik
    api_pool = RouterOsApiPool(host, username=username, password=password, plaintext_login=True)
    api = api_pool.get_api()

    # Ambil data interface
    netwatch_resource = api.get_resource('/tool/netwatch')
    netwatch_entries = netwatch_resource.get()

    # Tampilkan hasilnya
    print("Daftar Netwatch:")
    for entry in netwatch_entries:
        print(entry)

    # Tutup koneksi
    api_pool.disconnect()

except Exception as e:
    print("Gagal mengambil data Netwatch:")
    print(e)