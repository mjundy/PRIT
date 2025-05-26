const itemForm = document.getElementById('itemForm');

// Event listener untuk menambahkan data melalui form
itemForm.addEventListener('submit', function(event) {
    event.preventDefault();

    const tanggalPR = document.getElementById('tanggalPR').value;
    const partNumber = document.getElementById('partNumber').value;
    const partName = document.getElementById('partName').value;
    const uom = document.getElementById('uom').value;
    const qty = document.getElementById('qty').value;
    const status = document.getElementById('status').value;

    // Ambil data yang ada di localStorage dan tambahkan data baru
    const items = JSON.parse(localStorage.getItem('items') || '[]');
    items.push({ tanggalPR, partNumber, partName, uom, qty, status });
    localStorage.setItem('items', JSON.stringify(items));

    // Kembali ke halaman utama
    window.location.href = 'index.html';
});
