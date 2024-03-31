from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton,
    QLabel, QLineEdit
)
from PyQt5.QtCore import Qt, pyqtSignal
import matplotlib.pyplot as plt
class CustomTableWidget(QTableWidget):
    enterPressed = pyqtSignal()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.enterPressed.emit()
        else:
            super().keyPressEvent(event)
class GraphApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300,600)
        self.setWindowTitle("Plot X vs Y")
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)
        self.create_initial_layout()

        self.setCentralWidget(self.central_widget)
    def create_initial_layout(self):
        self.table = CustomTableWidget()
        self.table.setRowCount(5)  # Set initial rows
        self.table.setColumnCount(2)  # X and Y columns
        self.table.setHorizontalHeaderLabels(['X', 'Y'])
        self.layout.addWidget(self.table)

        self.add_row_button = QPushButton("Add Row")
        self.add_row_button.clicked.connect(self.add_row)
        self.layout.addWidget(self.add_row_button)

        self.xlabel_label = QLabel("X-axis Label:")
        self.layout.addWidget(self.xlabel_label)
        self.xlabel = QLineEdit()
        self.layout.addWidget(self.xlabel)

        self.ylabel_label = QLabel("Y-axis Label:")
        self.layout.addWidget(self.ylabel_label)
        self.ylabel = QLineEdit()
        self.layout.addWidget(self.ylabel)

        self.title_label = QLabel("Graph Title:")
        self.layout.addWidget(self.title_label)
        self.title = QLineEdit()
        self.layout.addWidget(self.title)

        self.submit_button = QPushButton("Generate Graph")
        self.submit_button.clicked.connect(self.generate_graph)
        self.layout.addWidget(self.submit_button)

        self.clear_button = QPushButton("Clear Entries")
        self.clear_button.clicked.connect(self.clear_entries)
        self.layout.addWidget(self.clear_button)

        self.table.enterPressed.connect(self.move_to_next_cell)
    def generate_graph(self):
        x_values = []
        y_values = []
        for row in range(self.table.rowCount()):
            x_item = self.table.item(row, 0)
            y_item = self.table.item(row, 1)
            if x_item and y_item:
                x_values.append(float(x_item.text() if x_item.text() else 0))
                y_values.append(float(y_item.text() if y_item.text() else 0))
        # Plotting the graph using Matplotlib
        plt.plot(x_values, y_values)
        plt.xlabel(self.xlabel.text())
        plt.ylabel(self.ylabel.text())
        plt.title(self.title.text())
        plt.tight_layout()
        plt.show()
    def clear_entries(self):
        self.table.clearContents()
    def move_to_next_cell(self):
        current_row = self.table.currentRow()
        current_column = self.table.currentColumn()
        if current_column == 0:  # Filling X values
            next_column = current_column
            next_row = (current_row + 1) % self.table.rowCount()
            self.table.setCurrentCell(next_row, next_column)
        elif current_column == 1:  # Filling Y values
            next_column = current_column
            next_row = (current_row + 1) % self.table.rowCount()
            self.table.setCurrentCell(next_row, next_column)
    def add_row(self):
        current_row_count = self.table.rowCount()
        self.table.setRowCount(current_row_count + 1)
if __name__ == "__main__":
    app = QApplication([])
    window = GraphApp()
    window.show()
    app.exec()



