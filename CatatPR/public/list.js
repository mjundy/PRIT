const itemList = document.getElementById('itemList');

// Fungsi untuk memuat data dari server
async function loadItems() {
    const response = await fetch('/api/items');
    const data = await response.json();

    itemList.innerHTML = ''; // Kosongkan daftar sebelum memuat data baru
    data.data.forEach((item, index) => addItem(item, index + 1));
}

// Fungsi untuk menambahkan data ke tabel
function addItem(item, no) {
    const row = document.createElement('tr');
    row.innerHTML = `
        <td>${no}</td>
        <td>${item.tanggalPR}</td>
        <td>${item.partNumber}</td>
        <td>${item.partName}</td>
        <td>${item.uom}</td>
        <td>${item.qty}</td>
        <td>
            <select onchange="updateStatus(${item.id}, this.value)">
                <option value="Sent to Purchase" ${item.status === 'Sent to Purchase' ? 'selected' : ''}>Sent to Purchase</option>
                <option value="Received" ${item.status === 'Received' ? 'selected' : ''}>Received</option>
                <option value="Canceled" ${item.status === 'Canceled' ? 'selected' : ''}>Canceled</option>
            </select>
        </td>
        <td><span class="btn btn-danger onclick="deleteItem(${item.id})">Delete</span></td>
    `;
    itemList.appendChild(row);
}

// Fungsi untuk memperbarui status
async function updateStatus(id, newStatus) {
    await fetch(`/api/items/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ status: newStatus })
    });
}

// Muat data saat halaman dibuka
loadItems();
