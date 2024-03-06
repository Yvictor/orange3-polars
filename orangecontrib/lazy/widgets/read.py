import polars as pl
from Orange.data import Table
from Orange.widgets import gui
from Orange.widgets.settings import Setting
from Orange.widgets.widget import OWWidget, Input, Output, Msg


class ReadWidget(OWWidget):
    name = "Read file"
    description = "read the dataset as lazyframe"
    icon = "icons/category.svg"
    priority = 100 
    keywords = ["widget", "io", "input", "read", "data"]
    want_main_area = False
    resizing_enabled = True

    label = Setting("")

    class Outputs:
        data = Output("Data", pl.LazyFrame)


    def __init__(self):
        super().__init__()
        self.data = pl.LazyFrame()
        self.label_box = gui.lineEdit(self.controlArea, self, "label", box="Text", callback=self.commit)

    def commit(self):
        print(f"label: {self.label}")

if __name__ == "__main__":
    from Orange.widgets.utils.widgetpreview import WidgetPreview  # since Orange 3.20.0
    WidgetPreview(ReadWidget).run()