from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QScrollArea, QWidget, QVBoxLayout

app = QApplication([])

window = QMainWindow()
window.resize(800, 400)
window.move(300, 310)
window.setWindowTitle('薪资统计')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10, 25)
textEdit.resize(300, 350)


def handleCalc():
    print('统计按钮被点击了')


button = QPushButton('统计', window)
button.move(380, 80)
button.clicked.connect(handleCalc)

w = QWidget()
window.setCentralWidget(w)

topFiller = QWidget()
topFiller.move(380, 2000)
topFiller.setMinimumSize(400, 2000)  #######设置滚动条的尺寸
for filename in range(20):
    MapButton = QPushButton(topFiller)
    MapButton.setText(str(filename))
    MapButton.move(filename * 10, filename * 40)
##创建一个滚动条
scroll = QScrollArea()
scroll.setWidget(topFiller)

vbox = QVBoxLayout()
vbox.addWidget(scroll)
vbox.addWidget(textEdit)
vbox.addWidget(button)
w.setLayout(vbox)

window.show()

app.exec_()
