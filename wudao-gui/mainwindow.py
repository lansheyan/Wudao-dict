from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

from mainwindow_ui import *
from GuiDraw import GuiDraw


class MainWindow(QMainWindow):
    ui = None
    mainWindow = None

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setup_ui()

    def setup_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.line_edit_typed()
        p3 = QPalette()
        p3.setColor(QPalette.Background, QColor('#300A24'))
        p3.setColor(QPalette.Base, QColor('#300A24'))
        self.ui.textBrowser.setPalette(p3)
        self.ui.statusbar.showMessage('Github, Inc. @2016')
        self.ui.lineEdit.returnPressed.connect(self.search_bt_clicked)
        self.ui.search_b.clicked.connect(self.search_bt_clicked)

    def line_edit_typed(self):
        sl = ['a', 'air', 'airplane']
        com = QCompleter(sl)
        com.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.lineEdit.setCompleter(com)

    def search_bt_clicked(self):
        pt = '<span style=\" font-size:12pt; font-weight:600; color:#FF0c32;\" > %s </span>'
        self.ui.textBrowser.setHtml(pt % 'haha' + '<p>hh</p>')
        g = GuiDraw()
        import json
        f = open('../wudao-dict/test.in', 'r')
        wi = json.load(f)
        f.close()
        g.draw_zh_text(wi, True)
        self.ui.textBrowser.setHtml(g.html)
        print('search')


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
