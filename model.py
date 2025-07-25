class Tugas:
    def __init__(self, id, nama, selesai=False):
        self.id = id
        self.nama = nama
        self.selesai = selesai

    def tandai_selesai(self):
        self.selesai = True
