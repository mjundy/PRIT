// Fungsi untuk render tabel
function renderTable(data) {
    const tableBody = document.getElementById('tableBody');
    tableBody.innerHTML = '';

    data.forEach((item, index) => {
        const row = document.createElement('tr');

        row.innerHTML = `
            <td>${index + 1}</td>
            <td>${item.tanggalPR}</td>
            <td>${item.partNumber || "-"}</td>
            <td>${item.partName}</td>
            <td>${item.uom}</td>
            <td>${item.qty}</td>
            <td>
                <select class="status-dropdown" data-id="${item.id}">
                    <option value="Sent to Purchase" ${item.status === 'Sent to Purchase' ? 'selected' : ''}>Sent to Purchase</option>
                    <option value="Received" ${item.status === 'Received' ? 'selected' : ''}>Received</option>
                    <option value="Canceled" ${item.status === 'Canceled' ? 'selected' : ''}>Canceled</option>
                </select>
            </td>
            <td><button class="delete-btn" data-id="${item.id}">Hapus</button></td>
        `;

        tableBody.appendChild(row);
    });

    // Event listener untuk dropdown status
    document.querySelectorAll('.status-dropdown').forEach(dropdown => {
        dropdown.addEventListener('change', async (event) => {
            const itemId = event.target.getAttribute('data-id');
            const newStatus = event.target.value;

            // Popup peringatan konfirmasi perubahan status
            const confirmChange = window.confirm("Apakah Anda yakin ingin mengubah status item ini?");
            if (!confirmChange) {
                // Jika pengguna membatalkan, kembalikan dropdown ke status awal
                const originalItem = data.find(item => item.id === parseInt(itemId));
                event.target.value = originalItem.status;
                return;
            }

            // Kirim permintaan ke server untuk memperbarui status jika pengguna mengonfirmasi
            await fetch(`/api/items/${itemId}/status`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ status: newStatus })
            });

            // Refresh data setelah pembaruan
            loadItems();
        });
    });

    // Event listener untuk tombol hapus
    document.querySelectorAll('.delete-btn').forEach(button => {
        button.addEventListener('click', async (event) => {
            const itemId = event.target.getAttribute('data-id');
            const confirmDelete = window.confirm("Apakah Anda yakin ingin menghapus item ini?");
            if (!confirmDelete) return;

            await fetch(`/api/items/${itemId}`, {
                method: 'DELETE'
            });

            // Refresh data setelah penghapusan
            loadItems();
        });
    });
}

// Fungsi untuk memuat item dari server
async function loadItems() {
    const response = await fetch('/api/items');
    const data = await response.json();
    renderTable(data);
}

// Memuat item saat halaman pertama kali di-load
loadItems();
