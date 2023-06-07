import sys
from PyQt6 import QtGui, QtCore, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
class showTime(QDialog):
  def __init__(self):

    super(showTime, self).__init__()
    self.resize(500, 400)
    self.setWindowTitle("label显示时间")
    self.label = QLabel(self)
    self.label.setFixedWidth(200)
    self.label.move(90, 80)

    # 动态显示时间在label上
    timer = QTimer(self)
    timer.timeout.connect(self.showtime)
    timer.start()
  def showtime(self):
    datetime = QDateTime.currentDateTime()
    text = datetime.toString()
    self.label.setText("   "+ text)

if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  my = showTime()
  my.show()
  sys.exit(app.exec())