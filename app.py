from flask import Flask, render_template, request, redirect, url_for
from model import Tugas

app = Flask(__name__)
daftar_tugas = []
id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', tugas=daftar_tugas)

@app.route('/tambah', methods=['POST'])
def tambah():
    global id_counter
    nama = request.form.get('nama').strip()

    # Validasi input kosong
    if not nama:
        return redirect(url_for('index'))

    # Validasi duplikat (case-insensitive)
    if any(t.nama.lower() == nama.lower() for t in daftar_tugas):
        return redirect(url_for('index'))

    daftar_tugas.append(Tugas(id_counter, nama))
    id_counter += 1
    return redirect(url_for('index'))

@app.route('/selesai/<int:id>')
def selesai(id):
    for t in daftar_tugas:
        if t.id == id:
            t.tandai_selesai()
            break
    return redirect(url_for('index'))

@app.route('/hapus/<int:id>')
def hapus(id):
    global daftar_tugas
    daftar_tugas = [t for t in daftar_tugas if t.id != id]
    return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit(id):
    tugas_diedit = next((t for t in daftar_tugas if t.id == id), None)
    return render_template('edit.html', tugas=tugas_diedit)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    nama_baru = request.form.get('nama').strip()

    if not nama_baru:
        return redirect(url_for('index'))

    for t in daftar_tugas:
        if t.id == id:
            t.nama = nama_baru
            break
    return redirect(url_for('index'))

#if __name__ == '__main__':
#    app.run(debug=True)
