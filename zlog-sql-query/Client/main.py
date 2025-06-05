import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from json import loads
from ui import Ui_Dialog
from api import query

app = QApplication(sys.argv)
window = QDialog()


class UI(Ui_Dialog):
    def run_query(self):
        nicks = self.nicks.text()
        if ' ' in nicks:
            nicks = nicks.split(' ')
        response = query(
            nicks,
            self.channel.text(),
            self.datestart.dateTime().toPyDateTime(),
            self.dateend.dateTime().toPyDateTime()
        )
        results = loads(response.text)
        body = results['body']

        row_count = len(body)
        self.output.setColumnCount(3)
        self.output.setRowCount(row_count)
        headers = ['created_at', 'nick', 'message']
        self.output.setHorizontalHeaderLabels(headers)

        for row in range(row_count):  # add items from array to QTableWidget
            for column, title in enumerate(headers):
                self.output.setItem(row, column, QTableWidgetItem(body[row][title]))


ui = UI()
ui.setupUi(window)
ui.query.clicked.connect(ui.run_query)

window.show()
sys.exit(app.exec_())
