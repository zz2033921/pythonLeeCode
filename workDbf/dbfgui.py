#导入tkinter模块
import tkinter
#创建主窗口
win = tkinter.Tk()
win.title("Hello World")
#创建标签
tkinter.Label(win, text="Hello World").pack()
#启动主循环
win.mainloop()
