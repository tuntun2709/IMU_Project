from PySide6.QtWidgets import QTableWidget, QLineEdit, QPushButton, QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import Qt

import random, string, sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()


        self.query = QLineEdit()
        self.query.setPlaceholderText("Search...")
        self.query.textChanged.connect(self.search)
        

        n_rows = 52
        n_cols = 4

        self.table = QTableWidget()
        self.table.setRowCount(n_rows)
        self.table.setColumnCount(n_cols)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)  
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for c in range(0, n_rows):
            for r in range(0, n_cols):
                s = ''.join(random.choice(string.ascii_lowercase) for n in range(10))
                i = QTableWidgetItem(s)
                self.table.setItem(c, r, i)
                print(c,r,s)

        self.table.sortItems(0)
        layout = QVBoxLayout()

        layout.addWidget(self.query)
        layout.addWidget(self.table)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

    def search(self, s):
        # clear current selection.
        self.table.setCurrentItem(None)

        if not s:
            # Empty string, don't search.
            return

        matching_items = self.table.findItems(s, Qt.MatchStartsWith)
        # print(len(matching_items))
        if matching_items:
            # we have found something
            item = matching_items[0]  # take the first
            self.table.setCurrentItem(item)
            self.table.scrollToItem(item, QAbstractItemView.PositionAtTop)


app = QApplication(sys.argv)
w = MainWindow()
w.show()

app.exec()