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

        # テキストボックス
        self.tb_log = QTextEdit(self)
        self.tb_log.setPlaceholderText('(ここに実行ログを表示します)')
        main_layout.addWidget(self.tb_log)

        # ステータスバー
        self.sb_status = QStatusBar()
        self.setStatusBar(self.sb_status)
        self.sb_status.setSizeGripEnabled(False)
        self.sb_status.showMessage('プログラムを起動しました。')

        # コンボボックスを表示するメソッド
        self.SetCombobox()

    # コンボボックスは別のメソッドに分けました
    def SetCombobox(self):
        # コンボボックスを使うことを宣言
        self.combobox = QComboBox(self)

        # コンボボックスの入力を無効
        self.combobox.setEditable(False)

        # 追加順にIDが0から割り振られる
        self.combobox.addItem("メートル[cm]")         # ID: 0
        self.combobox.addItem("ミリ[mm]")                 # ID: 1
        self.combobox.addItem("センチ[cm]")   # ID: 2
        self.combobox.addItem("キロ[km]")     # ID: 3
        self.combobox.addItem("インチ[in]")         # ID: 4
        self.combobox.addItem("フィート[ft]")
        self.combobox.addItem("ヤード[yd]")
        self.combobox.addItem("すん[寸]")
        self.combobox.addItem("しゃく[尺]")
        self.combobox.addItem("けん[間]")
        self.combobox.addItem("り[里]")
        self.combobox.addItem("こうねん[光年]")
        self.combobox.addItem("かいり[海里]")

        # コンボボックスの選択中のIDが変更されたら呼び出す処理
        self.combobox.currentIndexChanged.connect(
            self.CallbackCurrentindexchangedCombobox)

    # コンボボックスの選択中のIDが変更されたら実行する処理
    def CallbackCurrentindexchangedCombobox(self):
        print(self.combobox.currentIndex())  # 選択中のIDを表示
        print(self.combobox.currentText())  # 選択中の文字列を表示

# 本体
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
