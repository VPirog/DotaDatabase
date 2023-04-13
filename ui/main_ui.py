from database import global_init, create_session


class LoginScreen(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        global_init("dota")
        self.session = create_session()
        # self.pushButton.clicked.connect(self.load_table)
        # self.tableWidget.doubleClicked.connect(self.update_student)
        # self.tableWidget.cellChanged.connect(self.cell_changed)
        # self.pushButton_open_file.clicked.connect(self.color_dialog)
