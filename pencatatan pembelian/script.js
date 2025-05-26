const itemForm = document.getElementById('itemForm');
const itemList = document.getElementById('itemList');

let itemCount = 0;

// Fungsi untuk menambahkan data ke tabel dan localStorage
function addItem(tanggalPR, partNumber, partName, uom, qty, status) {
    itemCount++;
    
    // Buat baris baru di tabel
    const row = document.createElement('tr');
    row.innerHTML = `
        <td>${itemCount}</td>
        <td>${tanggalPR}</td>
        <td>${partNumber}</td>
        <td>${partName}</td>
        <td>${uom}</td>
        <td>${qty}</td>
        <td>
            <select class="status-dropdown" onchange="updateStatus(${itemCount - 1}, this.value)">
                <option value="Sent to Purchase" ${status === 'Sent to Purchase' ? 'selected' : ''}>Sent to Purchase</option>
                <option value="Received" ${status === 'Received' ? 'selected' : ''}>Received</option>
                <option value="Canceled" ${status === 'Canceled' ? 'selected' : ''}>Canceled</option>
            </select>
        </td>
        <td><span class="delete-btn" onclick="deleteItem(this)">Hapus</span></td>
    `;
    itemList.appendChild(row);

    // Simpan data di localStorage
    saveToLocalStorage();
}

// Fungsi untuk menyimpan data tabel ke localStorage
function saveToLocalStorage() {
    const items = [];
    itemList.querySelectorAll('tr').forEach((row, index) => {
        const cells = row.querySelectorAll('td');
        items.push({
            no: index + 1,
            tanggalPR: cells[1].innerText,
            partNumber: cells[2].innerText,
            partName: cells[3].innerText,
            uom: cells[4].innerText,
            qty: cells[5].innerText,
            status: cells[6].querySelector('select').value, // Ambil nilai dari dropdown
        });
    });
    localStorage.setItem('items', JSON.stringify(items));
}

// Fungsi untuk memuat data dari localStorage
function loadFromLocalStorage() {
    const items = JSON.parse(localStorage.getItem('items') || '[]');
    items.forEach(item => addItem(item.tanggalPR, item.partNumber, item.partName, item.uom, item.qty, item.status));
}

// Fungsi untuk memperbarui status di tabel dan localStorage saat dropdown diubah
function updateStatus(index, newStatus) {
    const items = JSON.parse(localStorage.getItem('items') || '[]');
    items[index].status = newStatus; // Perbarui status di item yang sesuai
    localStorage.setItem('items', JSON.stringify(items)); // Simpan kembali ke localStorage
}

// Fungsi untuk menghapus data dari tabel dan localStorage
function deleteItem(element) {
    element.parentElement.parentElement.remove();
    itemCount--;
    saveToLocalStorage();
}

// Event listener untuk menambahkan data melalui form
itemForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const tanggalPR = document.getElementById('tanggalPR').value;
    const partNumber = document.getElementById('partNumber').value;
    const partName = document.getElementById('partName').value;
    const uom = document.getElementById('uom').value;
    const qty = document.getElementById('qty').value;
    const status = document.getElementById('status').value;
    
    addItem(tanggalPR, partNumber, partName, uom, qty, status);

    // Reset form
    itemForm.reset();
});

// Load data dari localStorage saat halaman pertama kali dibuka
loadFromLocalStorage();
