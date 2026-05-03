from PySide6.QtWidgets import (
    QDialog, QFormLayout, QLineEdit, QSpinBox,
    QComboBox, QPushButton, QVBoxLayout, QDateEdit, QMessageBox
)

class FinanceDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tambah / Edit Data")

        layout = QVBoxLayout()
        form = QFormLayout()

        self.title = QLineEdit()

        self.amount = QSpinBox()
        self.amount.setMaximum(1_000_000_000)

        self.type = QComboBox()
        self.type.addItems(["Pemasukan", "Pengeluaran"])

        self.category = QComboBox()
        self.category.addItems(["Makan", "Transport", "Hiburan", "Lainnya"])

        self.date = QDateEdit()
        self.date.setCalendarPopup(True)

        form.addRow("Keterangan", self.title)
        form.addRow("Jumlah (Rp)", self.amount)
        form.addRow("Tipe", self.type)
        form.addRow("Kategori", self.category)
        form.addRow("Tanggal", self.date)

        btn = QPushButton("Simpan")
        btn.clicked.connect(self.validate)

        layout.addLayout(form)
        layout.addWidget(btn)
        self.setLayout(layout)

    def validate(self):
        if not self.title.text().strip():
            QMessageBox.warning(self, "Validasi", "Keterangan wajib diisi")
            return
        if self.amount.value() <= 0:
            QMessageBox.warning(self, "Validasi", "Jumlah harus > 0")
            return
        self.accept()

    def get_data(self):
        return (
            self.title.text(),
            self.amount.value(),
            self.type.currentText(),
            self.category.currentText(),
            self.date.date().toString("yyyy-MM-dd")
        )