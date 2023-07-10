import sys
import re
import matplotlib.pyplot as plt
from math import pow
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class FunctionPlotter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Function Plotter")
        self.setGeometry(100, 100, 500, 300)

        self.input_label = QLabel("Enter a function of x:")
        self.input_line_edit = QLineEdit()
        self.min_label = QLabel("Enter the minimum value of x:")
        self.min_line_edit = QLineEdit()
        self.max_label = QLabel("Enter the maximum value of x:")
        self.max_line_edit = QLineEdit()
        self.plot_button = QPushButton("Plot")

        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_line_edit)
        layout.addWidget(self.min_label)
        layout.addWidget(self.min_line_edit)
        layout.addWidget(self.max_label)
        layout.addWidget(self.max_line_edit)
        layout.addWidget(self.plot_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.plot_button.clicked.connect(self.plot_function)

    def plot_function(self):
        function = self.input_line_edit.text()
        min_x = self.min_line_edit.text()
        max_x = self.max_line_edit.text()

        # Validate input
        if not function or not min_x or not max_x:
            QMessageBox.warning(self, "Input Error", "Please enter a function and range for x.")
            return

        try:
            min_x = float(min_x)
            max_x = float(max_x)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numeric values for the range of x.")
            return

        x_values = []
        y_values = []

        # Generate x values and evaluate function
        try:
            for x in range(int(min_x), int(max_x) + 1):
                x_values.append(x)
                y_values.append(eval(self.parse_function(function, x)))
        except Exception as e:
            QMessageBox.warning(self, "Function Error", f"An error occurred while evaluating the function: {str(e)}")
            return

        # Plot the graph
        plt.plot(x_values, y_values)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Function Plot')
        plt.show()

    def parse_function(self, function, x):
        # Replace x with the value
        function = function.replace('x', str(x))

        # Replace ^ with **
        function = function.replace('^', '**')

        return function

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FunctionPlotter()
    window.show()
    sys.exit(app.exec_())
