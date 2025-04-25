from PyQt5.QtCore import QThread, pyqtSignal, QTimer, Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox

class WorkThread(QThread):
    update_progress = pyqtSignal(int)
    update_status = pyqtSignal(str)
    error_message = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        # initialize here

    def run(self):
        """
        Overrides the QThread method to do your work.
        
        """
        try:
            # Show the status message on the UI.
            self.update_status.emit("Status: Start to ...")
            # Do something.
          
            data_list = # your real data set
            total_item: int = len(data_list)
            for iter, data in enumerate(data_list):
                # Update the progress bar.
                progress_value: int = int((iter + 1) / total_item * 100)
                self.update_progress.emit(progress_value)
            
            self.update_status.emit("Status: Finish task.")
            self.quit()
        except Exception as e: 
            self.error_message.emit(f"Unexpected Exception: \n{e}")
            self.quit()





class MainWindowController(QMainWindow, UI_window):
    def __init__(self) -> None:
        # initialize here
        super().__init__()
        self.worker = None
        self.target_value = 0
        self.timer = QTimer(self)
    
    def MsgBox(self, title: str, content: str, icon: int) -> None:
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(content)
        msg.setIcon(icon)
        msg.addButton(QMessageBox.Ok)
        msg.setTextInteractionFlags(Qt.TextSelectableByMouse)
        msg.exec()

    def Start(self):
        self.worker = WorkThread()
        self.worker.finished.connect(self.worker_finished)
        self.worker.update_progress.connect(self.animate_progress_bar)
        self.worker.update_status.connect(self.update_status_value)
        self.worker.error_message.connect(self.error_message_value)
        self.timer.timeout.connect(self.update_progress_bar)

        self.worker.start()



    def worker_finished(self) -> None:
        # Do something when finish the job. (e.g. show message, export file...etc)
        
    # region Update Status
    def animate_progress_bar(self, val):
        self.target_value = val
        self.timer.start(50)
    
    def update_progress_bar(self):
        curr_val = self.progressBar.value()
        if curr_val < self.target_value:
            self.progressBar.setValue(curr_val + 1)
        else:
            self.timer.stop()
    
    def update_status_value(self, text):
        self.statusLabel.setText(text)
    
    def error_message_value(self, text) -> None:
        self.MsgBox("Task Error", text, 3)
        self.close()
    
    # endregion
