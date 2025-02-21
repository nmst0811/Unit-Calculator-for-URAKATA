import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QStatusBar, QWidget, QVBoxLayout, QHBoxLayout

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

# 本体
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
