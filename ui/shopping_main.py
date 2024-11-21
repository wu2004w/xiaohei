import sys
from PyQt5.QtWidgets import QApplication, QWidget
from shopping import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets


class ShoppingWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 创建一个数据模型实例，后续用于添加多条数据
        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)
        self.comboBox.addItem("电脑")
        self.comboBox.addItem("手机")
        self.comboBox.addItem("平板")
        self.pushButton.clicked.connect(self.add_to_list)
    def add_to_list(self):
        product_name = self.comboBox.currentText()
        quantity = self.spinBox.value()
        unit_price = 0
        if product_name == "电脑":
            unit_price = 5000
        elif product_name == "手机":
            unit_price = 3000
        elif product_name == "平板":
            unit_price = 4000
        total_price = unit_price * quantity
        info = f"商品：{product_name}，数量：{quantity}，总价：{total_price}"

        item = QtGui.QStandardItem(info)
        self.model.appendRow(item)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShoppingWidget()
    window.show()
    sys.exit(app.exec())