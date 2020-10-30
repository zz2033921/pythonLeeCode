import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QScrollArea, QWidget, QVBoxLayout

app = QApplication([])
window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)

w = QWidget()
window.setCentralWidget(w)

topFiller = QWidget()
topFiller.setMinimumSize(250, 2000)  #######设置滚动条的尺寸
for filename in range(20):
    MapButton = QPushButton(topFiller)
    MapButton.setText(str(filename))
    MapButton.move(10, filename * 40)
##创建一个滚动条
scroll = QScrollArea()
scroll.setWidget(topFiller)

vbox = QVBoxLayout()
vbox.addWidget(scroll)
w.setLayout(vbox)

window.statusBar().showMessage("底部信息栏")
window.resize(300, 500)

window.show()
app.exec_()

# class MainWindow(QMainWindow):
#    def __init__(self,):
#       super(QMainWindow, self).__init__()
#       self.number = 0
#
#       w = QWidget()
#       self.setCentralWidget(w)
#
#       self.topFiller = QWidget()
#       self.topFiller.setMinimumSize(250, 2000)  #######设置滚动条的尺寸
#       for filename in range(20):
#          self.MapButton = QPushButton(self.topFiller)
#          self.MapButton.setText(str(filename))
#          self.MapButton.move(10, filename * 40)
#       ##创建一个滚动条
#       self.scroll = QScrollArea()
#       self.scroll.setWidget(self.topFiller)
#
#       self.vbox = QVBoxLayout()
#       self.vbox.addWidget(self.scroll)
#       w.setLayout(self.vbox)
#
#       self.statusBar().showMessage("底部信息栏")
#       self.resize(300, 500)
#
#
# if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    window = QMainWindow()
#    mainwindow = MainWindow()
#    mainwindow.show()
#    sys.exit(app.exec_())
