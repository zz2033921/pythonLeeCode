from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog
from PySide2.QtUiTools import QUiLoader
import dbf

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
            "选择你要导入的DBF",  # 标题
            r"d:",  # 起始目录
            "数据类型 (*.DBF )"  # 选择类型过滤项，过滤内容在括号中
        )
        print(filePaths)
        print(type(filePaths))
        curDbf = self.getDBf(str(filePaths[0]))
        self.ui.ksh.setText(curDbf['KSH'])
        self.ui.sfzh.setText(curDbf['SFZH'])
        self.ui.xm.setText(curDbf['XM'])
        # QMessageBox.about(self.ui,
        #                   '统计结果',
        #                   f'''薪资20000 以上的有：\n{"aaaa"}
        #             \n薪资20000 以下的有：\n{"aaaa"}'''
        #                   )
        # print(self.getDBf())

    def getDBf(self, filePath):
        src_filename = filePath

        src_table = dbf.Table(
            filename=src_filename,
            codepage='cp936',
        )

        src_table.open()

        tempList = []
        for cc in src_table.field_names:
            # print(cc)
            tempList.append(cc)

        for i in src_table:
            # 这里的i并不是一个列表，而是一个数据结构，可以通过以下的方式转化为列表
            record_len = len(i)
            one_data_list = i[0:record_len]
            one_data = list(one_data_list)

        dbfDict = {}
        for index, value in enumerate(one_data):
            dbfDict[tempList[index]] = value.strip()

        return dbfDict

    def setJbxx(self, curDbf):
        # TODO
        return 0

    def setWorkFirst(self, curDbf):
        # TODO
        return 0

    def setWorkSec(self, curDbf):
        # TODO
        return 0

    def setZdzx(self, curDbf):
        # TODO
        return 0

    def getAllMsg(self):
        # TODO
        return 0

    def saveAllMsgToDbf(self):
        # TODO
        return 0
app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
