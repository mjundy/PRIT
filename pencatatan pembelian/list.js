const itemList = document.getElementById('itemList');
let itemCount = 0;

// Fungsi untuk memuat data dari localStorage
function loadFromLocalStorage() {
    const items = JSON.parse(localStorage.getItem('items') || '[]');
    items.forEach((item, index) => addItem(item, index + 1));
}

// Fungsi untuk menambahkan data ke tabel
function addItem(item, no) {
    itemCount++;

    const row = document.createElement('tr');
    row.innerHTML = `
        <td>${no}</td>
        <td>${item.tanggalPR}</td>
        <td>${item.partNumber}</td>
        <td>${item.partName}</td>
        <td>${item.uom}</td>
        <td>${item.qty}</td>
        <td>
            <select class="status-dropdown" onchange="updateStatus(${no - 1}, this.value)">
                <option value="Sent to Purchase" ${item.status === 'Sent to Purchase' ? 'selected' : ''}>Sent to Purchase</option>
                <option value="Received" ${item.status === 'Received' ? 'selected' : ''}>Received</option>
                <option value="Canceled" ${item.status === 'Canceled' ? 'selected' : ''}>Canceled</option>
            </select>
        </td>
        <td><span class="delete-btn" onclick="deleteItem(this)">Hapus</span></td>
    `;
    itemList.appendChild(row);
}

// Fungsi untuk memperbarui status di localStorage
function updateStatus(index, newStatus) {
    const items = JSON.parse(localStorage.getItem('items') || '[]');
    items[index].status = newStatus;
    localStorage.setItem('items', JSON.stringify(items));
}

// Fungsi untuk menghapus data dari tabel dan localStorage
function deleteItem(element) {
    const rowIndex = element.parentElement.parentElement.rowIndex - 1;
    element.parentElement.parentElement.remove();
    const items = JSON.parse(localStorage.getItem('items') || '[]');
    items.splice(rowIndex, 1);
    localStorage.setItem('items', JSON.stringify(items));
    itemCount--;
}

// Muat data dari localStorage saat halaman pertama kali dibuka
loadFromLocalStorage();
