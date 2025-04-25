# PyQt5_Tips
Some tips for pyqt5. <br>
All you need just ```python``` (which support PyQt5) and **Qt Designer**.


## PasswordVisibility
Add _QAction_ into _Qlineedit_ to make this workable.

## SplashScreen
Start-up view made by _QSplashScreen_.

## LeftSideBar
You can use a _Qpushbutton_ to control the left side bar (To show or to hide). <br>
Use signal/slots editor in the **Qt Designer** to make this workable.

## QThread_usage
Make a general QThread usage. <br>
You can do the long-time-consuming task separated by the main thread preventing from the UI stuck.
Also show the message, progress value on the UI.
