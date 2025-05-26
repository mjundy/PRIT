const itemForm = document.getElementById('itemForm');

// Event listener untuk menambahkan data melalui form
itemForm.addEventListener('submit', async function(event) {
    event.preventDefault();

    const tanggalPR = document.getElementById('tanggalPR').value;
    const partNumber = document.getElementById('partNumber').value || "-";
    const partName = document.getElementById('partName').value;
    const uom = document.getElementById('uom').value;
    const qty = document.getElementById('qty').value;
    const status = document.getElementById('status').value;

    // Kirim data ke server
    await fetch('/api/items', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ tanggalPR, partNumber, partName, uom, qty, status })
    });

    // Kembali ke halaman utama
    window.location.href = 'index.html';
});
