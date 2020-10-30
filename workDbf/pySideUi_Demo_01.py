from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog
from PySide2.QtUiTools import QUiLoader


class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui/test.ui')

        self.ui.importButton.clicked.connect(self.handleCalc)

    def handleCalc(self):
        filePaths, _ = QFileDialog.getOpenFileNames(
            self.ui,  # 父窗口对象
            "选择你要上传的DBF",  # 标题
            r"d:",  # 起始目录
            "数据类型 (*.DBF )"  # 选择类型过滤项，过滤内容在括号中
        )

        self.ui.ksh.setText("1000617210501221")
        self.ui.sfzh.setText("130429199409260065")
        self.ui.xm.setText("张寻")
        QMessageBox.about(self.ui,
                          '统计结果',
                          f'''薪资20000 以上的有：\n{"aaaa"}
                    \n薪资20000 以下的有：\n{"aaaa"}'''
                          )


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
