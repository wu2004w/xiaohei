from login import Ui_MainWindow as LoginUi

from PyQt5 import QtWidgets

class MainWindow(LoginUi,QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.close)
        self.commandLinkButton.clicked.connect(lambda :QtWidgets.QMessageBox.information(self,'官网','https://www.baidu.com'))
        #管理员和普通用户登录
        self.radioButton.toggled.connect(lambda :QtWidgets.QMessageBox.information(self,'提示',f'您选择的是{"管理员" if self.radioButton.isChecked() else "普通用户"}登录'))
        self.pushButton_3.clicked.connect(self.show_permission)
        title_list = ['代总经理','代人事经理']
        self.comboBox.addItems(title_list)
        #comboBox选项修改时，弹窗显示当前选项
        self.comboBox.currentIndexChanged.connect(lambda :QtWidgets.QMessageBox.information(self,'提示',f'您选择的是{self.comboBox.currentText()}'))
        #listWidget添加选项，赵六
        self.listWidget.addItem('赵六')
        #listWidget双击事件
        self.listWidget.itemDoubleClicked.connect(self.listWidget_double_clicked)

    # 定义一个listWidget双击事件函数,双击时调用
    def listWidget_double_clicked(self):
        # 创建一个窗口，用于显示用户双击内容，并且可以编辑
        selected_item = self.listWidget.currentItem()
        if selected_item:
            text = selected_item.text()
            dialog = QtWidgets.QDialog(self)
            dialog.setWindowTitle('编辑内容')

            # 创建一个输入框，用于编辑职位
            line_edit = QtWidgets.QLineEdit(text, dialog)
            line_edit.setGeometry(10, 10, 280, 30)

            # 创建一个按钮用于保存编辑的内容
            save_button = QtWidgets.QPushButton('保存', dialog)
            save_button.setGeometry(100, 50, 100, 30)
            save_button.clicked.connect(lambda: self.save_edit(dialog, line_edit, selected_item))

            dialog.exec_()

    def save_edit(self, dialog, line_edit, selected_item):
        new_text = line_edit.text()
        if new_text:
            selected_item.setText(new_text)
            dialog.accept()


    #定义一个login函数，用于处理登录逻辑
    def login(self):
        #弹窗显示输入的用户名和密码
        user = self.lineEdit.text()
        password = self.lineEdit_2.text()
        QtWidgets.QMessageBox.information(self, '登录信息', '用户名：%s\n密码：%s' % (user, password))

    #定义一个show_permission函数，用于显示权限
    def show_permission(self):
        permissions = []
        if self.checkBox.isChecked():
            permissions.append(self.checkBox.text())
        if self.checkBox_2.isChecked():
            permissions.append(self.checkBox_2.text())
        if self.checkBox_3.isChecked():
            permissions.append(self.checkBox_3.text())
        QtWidgets.QMessageBox.information(self, '权限', '您选择的权限有：%s' % ','.join(permissions))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())