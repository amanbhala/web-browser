import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
from PyQt5.QtWebEngineWidgets import *
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView()                 #To enable the web engine 
        self.browser.setUrl(QUrl('http://google.com'))  #To set the URL of our browser
        self.setCentralWidget(self.browser)
        self.showMaximized()                            #So that the browser is in full window mode.
      
        #nav bar
        navbar = QToolBar()                            #A nav bar is created 
        self.addToolBar(navbar)                        #To add the nav bar in the browser

        back_btn = QAction('Back', self)                  #Back button, back button's functionality
        back_btn.triggered.connect(self.browser.back)     #What happens when the back button is pressed
        navbar.addAction(back_btn)                        #Adding the back button in the browser

        forward_btn = QAction('Forward', self)            #Forward Button, forward button's functionality
        forward_btn.triggered.connect(self.browser.forward)   #What happens when the forward button is pressed
        navbar.addAction(forward_btn)                         #Adding the forward button in the browser

        reload_btn = QAction('Reload', self)            #Reload Button, reload button's functionality
        reload_btn.triggered.connect(self.browser.reload)  #What happens when the reload button is pressed
        navbar.addAction(reload_btn)                           #Adding the reload button in the browser

        home_btn = QAction('Home', self)                #Home Button, home button's functionality
        home_btn.triggered.connect(self.navigate_home)   #What happens when the home button is pressed
        navbar.addAction(home_btn)                      #Adding the home button in the browser

        self.url_bar = QLineEdit()                     #Adding a URL bar so that searching can happen.
        self.url_bar.returnPressed.connect(self.navigate_to_url)    #when enter is pressed we want to navigate to the url
        navbar.addWidget(self.url_bar)                    #To add the search bar in the browser

        self.browser.urlChanged.connect(self.update_url)   #To call the update_url function if url is changed.

    def navigate_home(self):                                    #This function will be called when the user clicks on home button.
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):                                #This function will be called whenever searching is done in the browser.
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):                                 #This function will be called whenever url is changed.
        self.url_bar.setText(q.toString())
         
app = QApplication(sys.argv)
QApplication.setApplicationName('My Cool Browser')
window = MainWindow() 
app.exec_() 