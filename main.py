import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QStatusBar, QWidget, QVBoxLayout, QHBoxLayout, QComboBox

# PySide6.QtWidgets.MainWindow を継承した MainWindow クラスの定義
class MainWindow(QMainWindow):
    # コンストラクタ(初期化)
    def __init__(self):
        # 親クラスのコンストラクタの呼び出し
        super().__init__()

        # スクリーンサイズの取得
        screen = QApplication.primaryScreen()
        screen_rect = screen.availableGeometry()  # 利用可能な画面スペースを取得
        screen_width = screen_rect.width()
        screen_height = screen_rect.height()

        # ウィンドウの初期サイズを設定 (横幅を1/4, 縦幅を1/2)
        window_width = screen_width // 4
        window_height = screen_height // 2
        self.setGeometry(screen_width / 2.0 - window_width / 2.0, screen_height / 2.0 - window_height / 2.0, window_width, window_height)  # type: ignore # 固定サイズに設定

        # ウィンドウタイトル設定
        self.setWindowTitle('Unit-Calculator for URAKATA')

        # メインウィジェットの作成と設定
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 垂直レイアウトの作成
        main_layout = QVBoxLayout(central_widget)
        

        # ボタン用の横レイアウトの作成
        button_layout = QHBoxLayout()

        # 「実行」ボタンの生成と設定
        self.btn_run = QPushButton('実行', self)
        button_layout.addWidget(self.btn_run)

        # 「クリア」ボタンの生成と設定
        self.btn_clear = QPushButton('クリア', self)
        button_layout.addWidget(self.btn_clear)

        # ボタンレイアウトをメインレイアウトに追加
        main_layout.addLayout(button_layout)

        # ステータスバー
        self.sb_status = QStatusBar()
        self.setStatusBar(self.sb_status)
        self.sb_status.setSizeGripEnabled(False)
        self.sb_status.showMessage('プログラムを起動しました。')

        # コンボボックスを表示するメソッド
        main_layout = self.centralWidget().layout()  # 行 53 修正
        self.SetCombobox()

        main_layout.addWidget(self.combobox1)        # type: ignore # 行 62 修正
        main_layout.addWidget(self.combobox2)        # type: ignore # 行 63 修正

    # コンボボックスは別のメソッドに分けました
    def SetCombobox(self):
        # コンボボックスを使うことを宣言
        self.combobox1 = QComboBox(self)
        self.combobox2 = QComboBox(self)

        # コンボボックスの入力を無効
        self.combobox1.setEditable(False)
        self.combobox2.setEditable(False)

        # 追加順にIDが0から割り振られる
        self.combobox1.addItem("メートル[cm]")         # ID: 0
        self.combobox1.addItem("ミリ[mm]")                 # ID: 1
        self.combobox1.addItem("センチ[cm]")   # ID: 2
        self.combobox1.addItem("キロ[km]")     # ID: 3
        self.combobox1.addItem("インチ[in]")         # ID: 4
        self.combobox1.addItem("フィート[ft]")
        self.combobox1.addItem("ヤード[yd]")
        self.combobox1.addItem("すん[寸]")
        self.combobox1.addItem("しゃく[尺]")
        self.combobox1.addItem("けん[間]")
        self.combobox1.addItem("り[里]")
        self.combobox1.addItem("こうねん[光年]")
        self.combobox1.addItem("かいり[海里]")

        self.combobox2.addItem("メートル[cm]")         # ID: 0
        self.combobox2.addItem("ミリ[mm]")                 # ID: 1
        self.combobox2.addItem("センチ[cm]")   # ID: 2
        self.combobox2.addItem("キロ[km]")     # ID: 3
        self.combobox2.addItem("インチ[in]")         # ID: 4
        self.combobox2.addItem("フィート[ft]")
        self.combobox2.addItem("ヤード[yd]")
        self.combobox2.addItem("すん[寸]")
        self.combobox2.addItem("しゃく[尺]")
        self.combobox2.addItem("けん[間]")
        self.combobox2.addItem("り[里]")
        self.combobox2.addItem("こうねん[光年]")
        self.combobox2.addItem("かいり[海里]")

        # コンボボックスの選択中のIDが変更されたら呼び出す処理
        self.combobox1.currentIndexChanged.connect(
            self.CallbackCurrentindexchangedCombobox)

        self.combobox2.currentIndexChanged.connect(
            self.CallbackCurrentindexchangedCombobox)

    # コンボボックスの選択中のIDが変更されたら実行する処理
    def CallbackCurrentindexchangedCombobox(self):
        print(self.combobox1.currentIndex())  # 選択中のIDを表示
        print(self.combobox1.currentText())  # 選択中の文字列を表示
        print(self.combobox2.currentIndex())  # 選択中のIDを表示
        print(self.combobox2.currentText())  # 選択中の文字列を表示

        

# 本体
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
