import tkinter as tk  # 导入tkinter模块
import tkinter.scrolledtext as tst


class Application(tk.Frame):  # 定义GUI类，派生于Frame类
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)  # 调用父类的构造函数
        self.grid()  # 调用组件的pack方法，调整其显示位置和大小
        self.createWidgets()  # 对象方法声明

    def createWidgets(self):  # 对象方法定义
        # text文本框
        self.textEdit = tst.ScrolledText(self, width=80, height=20)  # 创建text组件
        self.textEdit.grid(row=0, column=0, rowspan=6)
        # 打开按钮
        self.btnOpen = tk.Button(self, text="打开", command=self.funcOpen)  # 创建打开按钮
        self.btnOpen.grid(row=1, column=1)
        # 保存按钮
        self.btnSave = tk.Button(self, text="保存", command=self.funcSave)  # 创建保存按钮
        self.btnSave.grid(row=2, column=1)
        # 颜色按钮
        self.btnColor = tk.Button(self, text="颜色", command=self.funcColor)  # 创建颜色选择按钮
        self.btnColor.grid(row=3, column=1)
        # 退出按钮
        self.btnQuit = tk.Button(self, text="退出", command=self.funcQuit)  # 创建退出按钮
        self.btnQuit.grid(row=4, column=1)

    def funcOpen(self):  # 定义事件处理函数，打开文件
        self.textEdit.delete(1.0, tk.END)  # 清空text组件内的内容
        fname = tk.filedialog.askopenfilename(filetypes=[("Python源文件", ".py")])
        with open(fname, 'r', encoding="utf-8") as f1:  # 打开文件
            str1 = f1.read()  # 读入文件内容到str1中
        self.textEdit.insert(0.0, str1)  # 插入内容到text文本框中

    def funcSave(self):  # 定义事件处理函数，保存文件
        str1 = self.textEdit.get(1.0, tk.END)
        fname = tk.filedialog.asksaveasfilename(filetypes=[("Python源文件", ".py")])
        with open(fname, 'w', encoding="utf-8") as f1:  # 打开文件
            f1.write(str1)

    def funcColor(self):  # 定义事件处理函数，设置颜色
        t, c = tk.colorchooser.askcolor(title="设置颜色")
        self.textEdit.config(bg=c)

    def funcQuit(self):  # 定义事件处理函数，退出程序
        root.destroy()


root = tk.Tk()  # 创建一个Tk跟窗口组件root
root.title("简单文本编辑器")
app = Application(master=root)  # 创建Application的对象实例
app.mainloop()  # 调用组件mainloop方法，进入事件循环