import sqlite3
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from next_window import Ui_OtherWindow, __init__, show_popup, request

threads = []


class Ui_MainWindow(object):
    def loaddata(self):
        sqliteConnection = sqlite3.connect('BazaDanych.db')
        sqlite_select_query = """SELECT * from Filmy"""
        result = sqliteConnection.execute(sqlite_select_query)
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        sqliteConnection.close()

    def exportJSON(self):
        sqliteConnection = sqlite3.connect('BazaDanych.db')
        sqlite_select_query = """SELECT * FROM Filmy"""
        cursor = sqliteConnection.cursor()
        result = cursor.execute(sqlite_select_query)
        items = []
        for row in result:
            items.append({'tytul': row[0],
                          'opis': row[1],
                          'kategoria': row[2],
                          'dlugosc_filmu': row[3],
                          'id_filmu': row[4],
                          'link_do_filmu': row[5],
                          'data_publikacji': row[6],
                          'link_do_kanalu': row[7],
                          'link_do_miniaturki': row[8],
                          'liczba_wyswielen': row[9],
                          'liczba_likow': row[10],
                          'liczba_dislikow': row[11],
                          'liczba_komentarzy': row[12],
                          'tagi': row[13]})
        sqliteConnection.close()
        with open('BazaDanych.json', 'w') as outfile:
            json.dump('Filmy:', outfile)
            json.dump(items, outfile, sort_keys=True, indent=4, separators=(',', ': '))

        show_popup("Wykonano zadanie!", "Baza zostala pomyslnie wyeksportowana do pliku JSON")

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 0, 611, 561))
        self.tableWidget.setRowCount(1000)
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(
            ['Nazwa', 'Opis', 'Kategoria', 'Czas trwania', 'Id', 'Adres filmu', 'Data publikacji',
             'Adres kanału', 'Miniatura', 'Liczba wyświetleń', 'Liczba like\'ów', 'Liczba dislike\'ów',
             'Liczba komentarzy', 'Tagi'])
        self.Load_data = QtWidgets.QPushButton(self.centralwidget)
        self.Load_data.setGeometry(QtCore.QRect(640, 10, 151, 41))
        self.Load_data.setObjectName("Load_data")
        self.Load_data.clicked.connect(self.loaddata)

        self.Create_json = QtWidgets.QPushButton(self.centralwidget)
        self.Create_json.setGeometry(QtCore.QRect(640, 160, 151, 41))
        self.Create_json.setObjectName("Create_json")
        self.Create_json.clicked.connect(self.exportJSON)


        self.Sort = QtWidgets.QComboBox(self.centralwidget)
        self.Sort.setGeometry(QtCore.QRect(640, 60, 151, 41))
        self.Sort.setObjectName("Sort")
        self.Sort.addItem("")
        self.Sort.addItem("")
        self.Sort.addItem("")
        self.Sort.addItem("")
        self.Sort.addItem("")
        self.Sort.addItem("")
        self.Sort.addItem("")
        self.Sort.addItem("")
        self.Sort.addItem("")

        def szukaj_tytul(self):
            sqliteConnection = sqlite3.connect('BazaDanych.db')
            sqlite_select_query = """SELECT tytul from Filmy """
            result = sqliteConnection.execute(sqlite_select_query)
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            sqliteConnection.close()

        def liczba_wys(self):
            sqliteConnection = sqlite3.connect('BazaDanych.db')
            sqlite_select_query = """SELECT tytul, liczba_wyswielen from Filmy """
            result = sqliteConnection.execute(sqlite_select_query)
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            sqliteConnection.close()

        def liczba_likow(self):
            sqliteConnection = sqlite3.connect('BazaDanych.db')
            sqlite_select_query = """SELECT tytul, liczba_likow from Filmy """
            result = sqliteConnection.execute(sqlite_select_query)
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            sqliteConnection.close()

        def wszystko(self):
            sqliteConnection = sqlite3.connect('BazaDanych.db')
            sqlite_select_query = """SELECT * from Filmy """
            result = sqliteConnection.execute(sqlite_select_query)
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            sqliteConnection.close()
        self.Sort.currentIndexChanged.connect(lambda: sortuj(self))

        def wybierz(self):
            cb = str(self.comboBox1.currentText())
            if cb == "Tytul":
                szukaj_tytul(self)
            if cb == "Liczba wyswietlen":
                liczba_wys(self)
            if cb == "Liczba likow":
                liczba_likow(self)
            if cb == "Wszystko":
                wszystko(self)

        def sortuj_tytul(self):
            sqliteConnection = sqlite3.connect('BazaDanych.db')
            sqlite_select_query = """SELECT * FROM Filmy ORDER BY tytul"""
            result = sqliteConnection.execute(sqlite_select_query)
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            sqliteConnection.close()

        def sortuj_dlugosc(self):
            sqliteConnection = sqlite3.connect('BazaDanych.db')
            sqlite_select_query = """SELECT * FROM Filmy ORDER BY dlugosc_filmu"""
            result = sqliteConnection.execute(sqlite_select_query)
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            sqliteConnection.close()

        def sortuj_kategoria(self):
            sqliteConnection = sqlite3.connect('BazaDanych.db')
            sqlite_select_query = """SELECT * FROM Filmy ORDER BY kategoria"""
            result = sqliteConnection.execute(sqlite_select_query)
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            sqliteConnection.close()

        def sortuj_data(self):
            sqliteConnection = sqlite3.connect('BazaDanych.db')
            sqlite_select_query = """SELECT * FROM Filmy ORDER BY data_wstawienia"""
            result = sqliteConnection.execute(sqlite_select_query)
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            sqliteConnection.close()

        def sortuj_wyswietlenia(self):
            sqliteConnection = sqlite3.connect('BazaDanych.db')
            sqlite_select_query = """SELECT * FROM Filmy ORDER BY liczba_wyswielen"""
            result = sqliteConnection.execute(sqlite_select_query)
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            sqliteConnection.close()

        def sortuj_like(self):
            sqliteConnection = sqlite3.connect('BazaDanych.db')
            sqlite_select_query = """SELECT * FROM Filmy ORDER BY liczba_likow"""
            result = sqliteConnection.execute(sqlite_select_query)
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            sqliteConnection.close()

        def sortuj_dislike(self):
            sqliteConnection = sqlite3.connect('BazaDanych.db')
            sqlite_select_query = """SELECT * FROM Filmy ORDER BY liczba_dislikow"""
            result = sqliteConnection.execute(sqlite_select_query)
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            sqliteConnection.close()

        def sortuj_komentarze(self):
            sqliteConnection = sqlite3.connect('BazaDanych.db')
            sqlite_select_query = """SELECT * FROM Filmy ORDER BY liczba_komentarzy"""
            result = sqliteConnection.execute(sqlite_select_query)
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            sqliteConnection.close()

        def sortuj(self):
            cb = str(self.Sort.currentText())
            if cb == "Tytuł":
                sortuj_tytul(self)
            elif cb == "Kategoria":
                sortuj_kategoria(self)
            elif cb == "Czas trwania filmu":
                sortuj_dlugosc(self)
            elif cb == "Data dodania filmu":
                sortuj_data(self)
            elif cb == "Liczba wyświetleń":
                sortuj_wyswietlenia(self)
            elif cb == "Liczba like'ów":
                sortuj_like(self)
            elif cb == "Liczba dislike'ów":
                sortuj_dislike(self)
            elif cb == "Liczba komentarzy":
                sortuj_komentarze(self)

        self.search_films = QtWidgets.QPushButton(self.centralwidget)
        self.search_films.setGeometry(QtCore.QRect(640, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_films.setFont(font)
        self.search_films.setObjectName("search_films")

        self.search_films.clicked.connect(self.openWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionBaza_danych = QtWidgets.QAction(MainWindow)
        self.actionBaza_danych.setObjectName("actionBaza_danych")

        self.actionBaza_danych.triggered.connect(lambda: stworz())
        self.actionBaza_danych.triggered.connect(
            lambda: show_popup("Stworzono bazę!", "Stworzono bazę o nazwie: BazaDanych"))

        self.actionTabela = QtWidgets.QAction(MainWindow)
        self.actionTabela.setObjectName("actionTabela")

        self.actionTabela.triggered.connect(lambda: stworz_tab())
        self.actionTabela.triggered.connect(
            lambda: show_popup("Stworzono tabele!", "Stworzono tabelę o nazwie: Filmy"))

        self.actionPolaczanie = QtWidgets.QAction(MainWindow)
        self.actionPolaczanie.setObjectName("actionPolaczanie")

        self.actionPolaczanie.triggered.connect(lambda: polaczenie())
        self.actionPolaczanie.triggered.connect(
            lambda: show_popup("Nawiązano połączenie!", "Nawiązano połączenie z bazą o nazwie: BazaDanych"))

        self.actionUsun_tabele = QtWidgets.QAction(MainWindow)
        self.actionUsun_tabele.setObjectName("actionUsun_tabele")

        self.actionUsun_tabele.triggered.connect(lambda: usun_tabele())
        self.actionUsun_tabele.triggered.connect(
            lambda: show_popup("Usunieto tabele!", "Usunieto tabele o nazwie: Filmy"))

        self.actionImie1 = QtWidgets.QAction(MainWindow)
        self.actionImie1.setObjectName("actionImie1")

        self.actionImie2 = QtWidgets.QAction(MainWindow)
        self.actionImie2.setObjectName("actionImie2")

        self.actionImie3 = QtWidgets.QAction(MainWindow)
        self.actionImie3.setObjectName("actionImie3")

        self.actionImie4 = QtWidgets.QAction(MainWindow)
        self.actionImie4.setObjectName("actionImie4")

        self.menuNew.addAction(self.actionBaza_danych)
        self.menuNew.addAction(self.actionTabela)
        self.menuNew.addAction(self.actionPolaczanie)
        self.menuEdit.addAction(self.actionUsun_tabele)
        self.menuHelp.addAction(self.actionImie2)
        self.menuHelp.addAction(self.actionImie4)
        self.menuHelp.addAction(self.actionImie3)
        self.menuHelp.addAction(self.actionImie1)
        self.menubar.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Filmy"))
        self.Load_data.setText(_translate("MainWindow", "Wczytaj dane"))
        self.Create_json.setText(_translate("MainWindow", "Eksportuj do JSON"))
        self.Sort.setItemText(0, _translate("MainWindow", "Sortuj"))
        self.Sort.setItemText(1, _translate("MainWindow", "Tytuł"))
        self.Sort.setItemText(2, _translate("MainWindow", "Kategoria"))
        self.Sort.setItemText(3, _translate("MainWindow", "Czas trwania filmu"))
        self.Sort.setItemText(4, _translate("MainWindow", "Data dodania filmu"))
        self.Sort.setItemText(5, _translate("MainWindow", "Liczba wyświetleń"))
        self.Sort.setItemText(6, _translate("MainWindow", "Liczba like'ów"))
        self.Sort.setItemText(7, _translate("MainWindow", "Liczba dislike'ów"))
        self.Sort.setItemText(8, _translate("MainWindow", "Liczba komentarzy"))
        self.search_films.setText(_translate("MainWindow", "Wyszkukaj filmy"))
        self.menuNew.setTitle(_translate("MainWindow", "Nowy"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edytuj"))
        self.menuHelp.setTitle(_translate("MainWindow", "Pomoc"))
        self.actionBaza_danych.setText(_translate("MainWindow", "Baza danych"))
        self.actionBaza_danych.setStatusTip(_translate("MainWindow", "Stworz baze danych"))
        self.actionTabela.setText(_translate("MainWindow", "Tabela"))
        self.actionTabela.setStatusTip(_translate("MainWindow", "Stworz tabele"))
        self.actionPolaczanie.setText(_translate("MainWindow", "Polaczanie"))
        self.actionPolaczanie.setStatusTip(_translate("MainWindow", "Stworz tabele"))
        self.actionUsun_tabele.setText(_translate("MainWindow", "Usun tabele"))
        self.actionUsun_tabele.setStatusTip(_translate("MainWindow", "Usun tabele"))
        self.actionImie2.setText(_translate("MainWindow", "Mateusz Durlak"))
        self.actionImie2.setStatusTip(_translate("MainWindow", "mateusz.durlak@student.put.poznan.pl"))
        self.actionImie4.setText(_translate("MainWindow", "Hubert Jankowski"))
        self.actionImie4.setStatusTip(_translate("MainWindow", "hubert.jankowski@student.put.poznan.pl"))
        self.actionImie3.setText(_translate("MainWindow", "Łukasz Kowalik"))
        self.actionImie3.setStatusTip(_translate("MainWindow", "lukasz.t.kowalik@student.put.poznan.pl"))
        self.actionImie1.setText(_translate("MainWindow", "Tomasz Musiałek"))
        self.actionImie1.setStatusTip(_translate("MainWindow", "tomasz.musialek@student.put.poznan.pl"))

# Tworze nowa baze
def stworz():
    sqliteConnection = sqlite3.connect('BazaDanych.db')
    cursor = sqliteConnection.cursor()

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    cursor.close()


def polaczenie():
    sqliteConnection = sqlite3.connect('BazaDanych.db')
    cursor = sqliteConnection.cursor()


# Tworze tabele ktora bedzie przetrzymywac dane wyszukiwan
def stworz_tab():
    sqliteConnection = sqlite3.connect('BazaDanych.db')
    sqlite_create_table_query = '''CREATE TABLE Filmy (
                                tytul TEXT NOT NULL,
                                opis TEXT NOT NULL,
                                kategoria TEXT NOT NULL,
                                dlugosc_filmu TEXT NOT NULL,
                                id_filmu TEXT NOT NULL,
                                link_do_filmu TEXT NOT NULL,
                                data_wstawienia TEXT NOT NULL,
                                link_do_kanalu TEXT NOT NULL,
                                link_do_miniaturki TEXT NOT NULL,
                                liczba_wyswielen INT NOT NULL,
                                liczba_likow INT NOT NULL,
                                liczba_dislikow INT NOT NULL,
                                liczba_komentarzy INT NOT NULL,
                                tagi TEXT NOT NULL,
                                UNIQUE(tytul));'''

    cursor = sqliteConnection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    cursor.close()


def usun_tabele():
    sqliteConnection = sqlite3.connect('BazaDanych.db')
    sqlite_create_table_query = "DROP TABLE Filmy;"
    cursor = sqliteConnection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()


# funkcja sluzy do wyswietlania tabeli w programie
def readSqliteTable():
    sqliteConnection = sqlite3.connect('BazaDanych.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")
    sqlite_select_query = """SELECT * from Filmy"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Total rows are:  ", len(records))
    print("Printing each row")
    for row in records:
        print("Tytul: ", row[0])
        print("Opis: ", row[1])
        print("Kategoria: ", row[2])
        print("Dlugosc filmu: ", row[3])
        print("ID filmu: ", row[4])
        print("Link do filmu: ", row[5])
        print("Data wstawienia filmu: ", row[6])
        print("Link do kanalu: ", row[7])
        print("Link do miniaturki: ", row[8])
        print("Liczba wyswietlen: ", row[9])
        print("Liczba likow: ", row[10])
        print("Liczba dislikow: ", row[11])
        print("Liczba komentarzy: ", row[12])
        print("Tagi: ", row[13])

        print("\n")
    cursor.close()


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


__init__()
main()

