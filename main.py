import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk


def show_notification(message, color):
    root = tk.Tk()
    root.title("Server Status")
    root.geometry("300x100")

    label = tk.Label(root, text=message, fg=color)
    label.config(font=("Poppins", 18, "bold"))
    label.pack(pady=30)

    root.after(2000, root.destroy)  # Close the window after 3 seconds (3000 milliseconds)

    root.mainloop()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(QtCore.QSize(329, 236))
        self.setMinimumSize(QtCore.QSize(329, 236))

        self.start_button = QPushButton("Start Server", self)
        self.start_button.setGeometry(50, 50, 200, 50)
        self.start_button.clicked.connect(self.start_server) 

        self.stop_button = QPushButton("Stop Server", self)
        self.stop_button.setGeometry(50, 120, 200, 50)
        self.stop_button.clicked.connect(self.stop_server)

        self.server_process = None

    def start_server(self):
        if self.server_process is None or self.server_process.poll() is not None:
            self.server_process = subprocess.Popen(["python", "manage.py", "runserver"])
            print("Server started.")

            show_notification("Server started", "green")


    def stop_server(self):
        if self.server_process is not None and self.server_process.poll() is None:
            self.server_process.terminate()
            print("Server stopped.")

            show_notification("Server stopped", "red")


        self.server_process = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.setMinimumSize(QSize(329, 182))
    # window.setMaximumSize(QSize(329, 182))
    window.setWindowTitle("Django Server Control")
    window.setGeometry(100, 100, 300, 200)
    window.show()
    sys.exit(app.exec_())
