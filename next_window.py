import googleapiclient.discovery
import googleapiclient.errors
import sqlite3
import datetime
import isodate as isodate
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

youtube = None


def insertVaribleIntoTable(tytul, opis, kategoria, dlugosc_filmu, id_filmu, link_do_filmu, data_wydania_filmu, link_do_kanalu, link_do_miniaturki, liczba_wyswietlen, liczba_likow, liczba_dislikow, l_komentarzy, tagi):
    sqliteConnection = sqlite3.connect('BazaDanych.db')
    cursor = sqliteConnection.cursor()
    try:
        sqlite_insert_with_param = """INSERT INTO 'Filmy'
                        ('tytul', 'opis', 'kategoria', 'dlugosc_filmu', 'id_filmu', 'link_do_filmu', 'data_wstawienia', 'link_do_kanalu', 'link_do_miniaturki', 'liczba_wyswielen', 'liczba_likow', 'liczba_dislikow', 'liczba_komentarzy', 'tagi') 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

        data_tuple = (tytul, opis, kategoria, dlugosc_filmu, id_filmu, link_do_filmu, data_wydania_filmu, link_do_kanalu, link_do_miniaturki, liczba_wyswietlen, liczba_likow, liczba_dislikow, l_komentarzy, tagi)

        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
    except:
        print('Błąd - film znajduje się już w bazie danych')
    cursor.close()



def show_popup(text, text2):
    msq = QMessageBox()
    msq.setWindowTitle("Info")
    msq.setText(text)
    msq.setIcon(QMessageBox.Information)
    msq.setInformativeText(text2)
    x = msq.exec()

def __init__():
    api_service_name = "youtube"
    api_version = "v3"

    global youtube
    youtube = googleapiclient.discovery.build(api_service_name, api_version,
                                            developerKey='AIzaSyBlzZsxyUDdJSkuavWMD7_l5EuYCAS4QYM')


def request(title):
    titles = []
    descriptions = []
    categories = []
    durations = []
    ids = []
    links = []
    publishDate = []
    channels = []
    thumbnails = []
    views = []
    likes = []
    dislikes = []
    comments = []
    tags = []

    request = youtube.search().list(q=title, part='snippet', type='video', maxResults=10)
    response = request.execute()

    for item in response['items']:
        titles.append(item['snippet']['title'])
        # descriptions.append(item['snippet']['description'])
        ids.append(item['id']['videoId'])
        videoId = item['id']['videoId']
        links.append('https://www.youtube.com/watch?v=' + videoId)
        #publishDate.append(item['snippet']['publishedAt'])
        date = datetime.datetime.strptime((item['snippet']['publishedAt']), "%Y-%m-%dT%H:%M:%S.%fZ")
        publishDate.append(date)
        channelId = item['snippet']['channelId']
        channels.append('https://www.youtube.com/channel/' + channelId)
        thumbnails.append(item['snippet']['thumbnails']['high']['url'])

        request2 = youtube.videos().list(id=item['id']['videoId'], part='snippet, statistics, contentDetails')
        response2 = request2.execute()
        for item in response2['items']:
            try:
                descriptions.append(item['snippet']['description'])
            except:
                descriptions.append('Brak')
            dur = isodate.parse_duration(item['contentDetails']['duration'])
            durations.append(str(dur))
            try:
                views.append(int(item['statistics']['viewCount']))
            except:
                views.append('Brak')
            try:
                likes.append(int(item['statistics']['likeCount']))
            except:
                likes.append('Brak')
            try:
                dislikes.append(int(item['statistics']['dislikeCount']))
            except:
                dislikes.append('Brak')
            try:
                comments.append(int(item['statistics']['commentCount']))
            except:
                comments.append('Brak')
            try:
                tagsLists = []
                tagsLists.append(item['snippet']['tags'])
                tagsString = ''
                for list in tagsLists:
                    for tag in list:
                        tagsString += tag
                        tagsString += ', '
                tags.append(tagsString)
            except:
                tags.append('Brak')
            try:
                categoryId = (item['snippet']['categoryId'])

                if categoryId == '1':
                    categories.append('Film i animacja')
                elif categoryId == '2':
                    categories.append('Samochody i pojazdy')
                elif categoryId == '10':
                    categories.append('Muzyka')
                elif categoryId == '15':
                    categories.append('Zwierzęta')
                elif categoryId == '17':
                    categories.append('Sport')
                elif categoryId == '19':
                    categories.append('Podróże i wydarzenia')
                elif categoryId == '20':
                    categories.append('Gaming')
                elif categoryId == '22':
                    categories.append('Ludzie i blogi')
                elif categoryId == '23':
                    categories.append('Komedia')
                elif categoryId == '24':
                    categories.append('Rozrywka')
                elif categoryId == '25':
                    categories.append('Wiadomości i polityka')
                elif categoryId == '26':
                    categories.append('Poradniki i styl')
                elif categoryId == '27':
                    categories.append('Edukacja')
                elif categoryId == '28':
                    categories.append('Nauka i technologia')
                elif categoryId == '29':
                    categories.append('Społeczne i non-profit')
                else:
                    categories.append('Brak')
            except:
                categories.append('Brak')



    for u in range(10):
        insertVaribleIntoTable(titles[u], descriptions[u], categories[u], durations[u], ids[u], links[u],
                               publishDate[u],
                               channels[u], thumbnails[u], views[u], likes[u], dislikes[u], comments[u], tags[u])



class Ui_OtherWindow(object):
    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(161, 220)
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 131, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 40, 131, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 70, 131, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 100, 131, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(30, 130, 91, 41))
        self.SearchButton.setObjectName("SearchButton")


        def printthis(self):
            text = self.lineEdit.text()
            text2 = self.lineEdit_2.text()
            text3 = self.lineEdit_3.text()
            text4 = self.lineEdit_4.text()
            inputs = []
            i = 0
            if text:
                inputs.append(text)
                i = i + 1
            if text2:
                inputs.append(text2)
                i = i + 1
            if text3:
                inputs.append(text3)
                i = i + 1
            if text4:
                inputs.append(text4)
                i = i + 1

            for x in range(i):
                title = inputs[x]
                request(title)

            show_popup("Wykonano zadanie!", "Wszystkie dane zostały poprawnie dodane do bazy")


        self.SearchButton.clicked.connect(lambda: printthis(self))

        OtherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 161, 21))
        self.menubar.setObjectName("menubar")
        OtherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "MainWindow"))
        self.SearchButton.setText(_translate("OtherWindow", "Szukaj"))
        self.SearchButton.setShortcut(_translate("MainWindow", "Return"))
