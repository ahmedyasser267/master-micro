import pytest
from gui_program import FunctionPlotter

@pytest.fixture
def app(qtbot):
    test_app = FunctionPlotter()
    qtbot.addWidget(test_app)
    return test_app

def test_plot_function(app, qtbot):
    # Set up input values
    app.input_line_edit.setText("x**2")
    app.min_line_edit.setText("0")
    app.max_line_edit.setText("5")

    # Click the plot button
    qtbot.mouseClick(app.plot_button, QtCore.Qt.LeftButton)

    # Verify that the plot is displayed correctly
    assert len(app.plt.figure.axes) == 1

if __name__ == "__main__":
    pytest.main()
