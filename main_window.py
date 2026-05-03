from PySide6.QtWidgets import *
from PySide6.QtGui import QColor
from dialog_finance import FinanceDialog
from database import Database
from config import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_NAME)
        self.resize(1000, 550)

        self.db = Database()
        self.setup_ui()
        self.load_data()

    def setup_ui(self):
        central = QWidget()
        layout = QVBoxLayout()

        # Title
        title = QLabel(APP_NAME)
        title.setStyleSheet("font-size:20px; font-weight:bold;")

        # Summary saldo
        self.saldo_label = QLabel("Total Saldo: Rp 0")
        self.saldo_label.setStyleSheet("font-size:16px; font-weight:bold; color:#1f3b5b;")

        # Buttons
        self.add_btn = QPushButton("Tambah")
        self.edit_btn = QPushButton("Edit")
        self.delete_btn = QPushButton("Hapus")

        # Filter
        self.filter_box = QComboBox()
        self.filter_box.addItems(["Semua", "Pemasukan", "Pengeluaran"])
        self.filter_box.currentTextChanged.connect(self.load_data)

        # Search
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Cari...")
        self.search_input.textChanged.connect(self.load_data)

        # Table
        self.table = QTableWidget(0, 7)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Keterangan", "Jumlah", "Tipe", "Kategori", "Tanggal", "Saldo"]
        )
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Event
        self.add_btn.clicked.connect(self.add_data)
        self.edit_btn.clicked.connect(self.edit_data)
        self.delete_btn.clicked.connect(self.delete_data)

        # Layout
        layout.addWidget(title)
        layout.addWidget(self.saldo_label)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.edit_btn)
        layout.addWidget(self.delete_btn)
        layout.addWidget(self.filter_box)
        layout.addWidget(self.search_input)
        layout.addWidget(self.table)

        central.setLayout(layout)
        self.setCentralWidget(central)

        self.statusBar().showMessage(f"{STUDENT_NAME} | {STUDENT_NIM}")
        self.setup_menu()

    def setup_menu(self):
        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        help_menu = menu.addMenu("Bantuan")

        file_menu.addAction("Keluar", self.close)
        help_menu.addAction("Tentang", self.show_about)

    def show_about(self):
        QMessageBox.information(
            self,
            "Tentang",
            f"{APP_NAME}\n\n"
            "Aplikasi pencatatan pemasukan dan pengeluaran anak kos.\n\n"
            f"Nama: {STUDENT_NAME}\nNIM: {STUDENT_NIM}"
        )

    def add_data(self):
        dialog = FinanceDialog()
        if dialog.exec():
            self.db.add_data(dialog.get_data())
            self.load_data()

    def edit_data(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data dulu")
            return

        data_id = int(self.table.item(row, 0).text())

        dialog = FinanceDialog()
        dialog.title.setText(self.table.item(row, 1).text())
        dialog.amount.setValue(int(self.table.item(row, 2).text()))
        dialog.type.setCurrentText(self.table.item(row, 3).text())
        dialog.category.setCurrentText(self.table.item(row, 4).text())

        if dialog.exec():
            self.db.update_data(data_id, dialog.get_data())
            self.load_data()

    def delete_data(self):
        row = self.table.currentRow()
        if row < 0:
            return

        confirm = QMessageBox.question(self, "Konfirmasi", "Hapus data?")
        if confirm == QMessageBox.Yes:
            data_id = int(self.table.item(row, 0).text())
            self.db.delete_data(data_id)
            self.load_data()

    def load_data(self):
        keyword = self.search_input.text().lower()
        filter_type = self.filter_box.currentText()
        data = self.db.get_data()

        self.table.setRowCount(0)

        saldo = 0

        for row_data in data:
            if keyword not in str(row_data).lower():
                continue

            if filter_type != "Semua" and row_data[3] != filter_type:
                continue

            row = self.table.rowCount()
            self.table.insertRow(row)

            amount = int(row_data[2])
            tipe = row_data[3]

            if tipe == "Pemasukan":
                saldo += amount
            else:
                saldo -= amount

            for col, val in enumerate(row_data):
                self.table.setItem(row, col, QTableWidgetItem(str(val)))

            self.table.setItem(row, 6, QTableWidgetItem(f"Rp {saldo}"))

            color = QColor("#2ecc71") if tipe == "Pemasukan" else QColor("#e74c3c")
            for col in range(7):
                self.table.item(row, col).setBackground(color)

        self.saldo_label.setText(f"Total Saldo: Rp {saldo}")