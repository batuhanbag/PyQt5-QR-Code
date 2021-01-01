from PyQt5.QtWidgets import *

from PyQt5 import QtCore

from PyQt5.QtGui import *
import time
from QRW_python import Ui_MainWindow

import urllib.parse
import urllib.request


class QR(QMainWindow):

    def __init__(self):

        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit_icerik.setPlaceholderText("Örnek(www.batuhanbag.com)")
        self.ui.lineEdit_qrboyut.setValidator(QIntValidator(0,3000,self))


        self.ui.pushButton_process.clicked.connect(self.process)

        self.ui.actionHakkinda.triggered.connect(self.hakkinda)


    def process(self):

        try:
            for i in range(101):
                time.sleep(0.05)
                self.ui.progressBar.setValue(i)

            size = self.ui.lineEdit_qrboyut.text()

            veri = self.ui.lineEdit_icerik.text()

            isim = self.ui.lineEdit_isim.text()


            isim = isim + ".png"

            veriler = {
             'size': size + "x" + size,
             'data': veri

            }


            Parametreler = urllib.parse.urlencode(veriler)

            api_link = "https://api.qrserver.com/v1/create-qr-code/?"+ Parametreler

            urllib.request.urlretrieve(api_link, isim)

            QMessageBox.about(self, "QR Kod ", "QR Succes")
            self.ui.lineEdit_icerik.clear()
            self.ui.lineEdit_isim.clear()
            self.ui.lineEdit_qrboyut.clear()
        except:
            QMessageBox.critical(self,"Kritik","Bir Hata Oluştu..")


    def hakkinda(self):

        QMessageBox.about(self, "Batuhan", "Bu Box'ı <b>Batuhan Bağ</b> hazırlamıştır"
                                           "<br><br>"
                                           "<b>Batuhan Bağ İletişim:</b>"
                                           "<br>"
                                           "<a href=\"mailto:batuhannbagg@gmail.com\">batuhannbagg@gmail.com</a>"
                                           "</font>"
                          )

app = QApplication([])
window = QR()
window.show()
app.exec_()