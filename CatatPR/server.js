const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const PORT = 3000;

// Buat koneksi ke database SQLite
const db = new sqlite3.Database('./database.db', (err) => {
    if (err) {
        console.error(err.message);
    }
    console.log('Connected to the SQLite database.');
});

// Buat tabel jika belum ada
db.run(`CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tanggalPR TEXT,
    partNumber TEXT NULL,
    partName TEXT,
    uom TEXT,
    qty INTEGER,
    status TEXT
)`);

// Middleware
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'public')));

// API endpoint untuk mendapatkan data
app.get('/api/items', (req, res) => {
    db.all("SELECT * FROM items", [], (err, rows) => {
        if (err) {
            res.status(400).json({"error": err.message});
            return;
        }
        res.json({
            "data": rows
        });
    });
});

// API endpoint untuk menambahkan data
app.post('/api/items', (req, res) => {
    const { tanggalPR, partNumber, partName, uom, qty, status } = req.body;
    const query = `INSERT INTO items (tanggalPR, partNumber, partName, uom, qty, status) VALUES (?, ?, ?, ?, ?, ?)`;
    const params = [tanggalPR, partNumber, partName, uom, qty, status];
    db.run(query, params, function(err) {
        if (err) {
            res.status(400).json({"error": err.message});
            return;
        }
        res.json({
            "message": "success",
            "data": { id: this.lastID, tanggalPR, partNumber, partName, uom, qty, status }
        });
    });
});

// API endpoint untuk memperbarui status
app.put('/api/items/:id', (req, res) => {
    const { status } = req.body;
    const query = `UPDATE items SET status = ? WHERE id = ?`;
    db.run(query, [status, req.params.id], function(err) {
        if (err) {
            res.status(400).json({"error": err.message});
            return;
        }
        res.json({
            message: "Status updated successfully",
            data: { id: req.params.id, status }
        });
    });
});

// Jalankan server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
