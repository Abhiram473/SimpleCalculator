import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtGui import QIcon

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Calculator")
        self.setGeometry(500, 500, 400, 300)
        self.setWindowIcon(QIcon("CalculatorIcon.png"))

        self.initialize_ui()

    def initialize_ui(self):
        self.num1_input = QLineEdit(self)
        self.num1_input.setPlaceholderText("Enter First Number ")
        self.num2_input = QLineEdit(self)
        self.num2_input.setPlaceholderText("Enter Second Number ")
        self.operation_input = QLineEdit(self)
        self.operation_input.setPlaceholderText("Enter The Operator To Perform Operation")

        self.result_label = QLabel("Result:", self)

        self.calculate_button = QPushButton("Calculate", self)
        self.calculate_button.clicked.connect(self.calculate)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.clicked.connect(self.clear_values)

        layout = QVBoxLayout()
        layout.addWidget(self.num1_input)
        layout.addWidget(self.num2_input)
        layout.addWidget(self.operation_input)
        layout.addWidget(self.result_label)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.clear_button)

        self.setLayout(layout)

    def calculate(self):
        try:
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())
            operation = self.operation_input.text()

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2
            else:
                self.show_message("Invalid operation. Please enter +, -, *, or /.")
                return

            self.result_label.setText(f"Result: {result}")

        except ValueError:
            self.show_message("Invalid input. Please enter valid numbers.")
        except ZeroDivisionError:
            self.show_message("Cannot divide by zero.")

    def clear_values(self):
        self.num1_input.clear()
        self.num2_input.clear()
        self.operation_input.clear()
        self.result_label.clear()

    def show_message(self, message):
        msg_box = QMessageBox()
        msg_box.setText(message)
        msg_box.exec_()


def main():
    app = QApplication(sys.argv)
    calculator_app = CalculatorApp()
    calculator_app.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
