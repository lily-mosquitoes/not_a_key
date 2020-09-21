import os
import sys
import shutil
import itertools
from PyQt5 import QtWidgets, QtGui

from ui_files.filter_window import Ui_Dialog as Ui_FilterWindow
from ui_files.main_window import Ui_MainWindow

from models.model_key import Key
from models.model_reference_database import ReferenceDatabase

from algorithms import Algorithms


class FilterWindow(QtWidgets.QDialog, Ui_FilterWindow):

    def __init__(self):
        super(FilterWindow, self).__init__()
        self.setupUi(self)

        # set no close
        self._want_to_close = False

        # set reference database variable
        self.ref_database = None

        # lay out UI
        self.layoutUi()

        # start main loop
        self.mainLoop()

    # overwrite closeEvent to exit on manual close,
    # but proceed normally on button press (sets _want_to_close)
    def closeEvent(self, evnt):
        if self._want_to_close:
            try:
                self.ref_database.connection.close()
            except Exception as e:
                connection_error_handler(e)
            # use closeEvent from parent class
            super(FilterWindow, self).closeEvent(evnt)
        else:
            try:
                self.ref_database.connection.close()
            except Exception as e:
                connection_error_handler(e)
            # exit program completely
            sys.exit(0)

    def layoutUi(self):
        #
        # tool button
        self.menu = QtWidgets.QMenu()
        self.actionAddResource = QtWidgets.QAction('add resource')
        self.actionRemoveResource = QtWidgets.QAction('remove resource')
        for item in [self.actionAddResource, self.actionRemoveResource]:
            self.menu.addAction(item)
        self.toolButton.setMenu(self.menu)
        #
        # databases
        self.installed_path = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), 'installed')
        with os.scandir(self.installed_path) as dir:
            installed_resources = [d.name for d in dir if d.is_dir()]
        self.resourceBox.addItems(installed_resources)
        #
        self.read_reference_database()
        #
        # manual setup of 'sort by' combo box
        self.sortBox.addItems(['full year', 'season', 'month'])
        #
        # available algorithms come from package algorithms
        self.algorithms = Algorithms()
        #
        # set algorithm aliases
        self.algoBox.addItems(self.algorithms.available_algorithms.keys())

    def mainLoop(self):
        #
        self.actionAddResource.triggered.connect(self.addResource)
        #
        self.actionRemoveResource.triggered.connect(self.removeResource)
        #
        self.syncButton.pressed.connect(self.syncResourceDatabases)
        #
        self.resourceBox.currentIndexChanged.connect(self.read_reference_database)
        #
        self.sortBox.currentIndexChanged.connect(self.setSortBox2)
        #
        self.algoBox.currentIndexChanged.connect(self.setAlgoOptions)
        #
        self.startButton.pressed.connect(self.onStartPress)

    def read_reference_database(self):
        #
        if self.ref_database:
            try:
                self.ref_database.connection.close()
            except Exception as e:
                connection_error_handler(e)
        #
        ref_database_path = os.path.join(self.installed_path, str(self.resourceBox.currentText()), 'reference_database.db')
        #
        try:
            self.ref_database = ReferenceDatabase(path=ref_database_path)
        except Exception as e:
            connection_error_handler(e)
        #
        self.locationBox.clear()
        self.locationBox.addItems(['all states'] + self.ref_database.get_locations())

    def addResource(self):
        print('to-do: build add resource feature')
        pass

    def removeResource(self):
        #
        resource_name = str(self.resourceBox.currentText())
        resource_path = os.path.join(self.installed_path, resource_name)
        #
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(f'Are you sure you want to delete the database "{resource_name}"?')
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        choice = msg.exec_()
        if choice == QtWidgets.QMessageBox.Yes:
            try:
                self.ref_database.connection.close()
                self.ref_database = None
            except Exception as e:
                connection_error_handler(e)
            try:
                self.resourceBox.removeItem(self.resourceBox.currentIndex())
                shutil.rmtree(resource_path)
            except OSError as e:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText(f'Error: {e.filename} - {e.strerror}')
        else:
            pass

    def syncResourceDatabases(self):
        print('to-do: build sync resource databases feature')
        pass

    def setSortBox2(self):
        # the contents of the second 'sort by' combo box depend on the first
        sortBox = str(self.sortBox.currentText()) # damn thing returns QString
        # manual set up of second 'sort by' combo box
        self.sortBox2.clear()
        if sortBox == 'month':
            self.sortBox2.addItems(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
            self.sortBox2.setEnabled(True)
        elif sortBox == 'season':
            self.sortBox2.addItems(['Winter', 'Spring', 'Summer', 'Fall'])
            self.sortBox2.setEnabled(True)
        else:
            self.sortBox2.clear()
            self.sortBox2.setEnabled(False)

    def setAlgoOptions(self):
        algo = str(self.algoBox.currentText())
        if algo in self.algorithms.use_percent:
            self.algoPercent.setEnabled(True)
        else:
            self.algoPercent.setEnabled(False)

    def onStartPress(self):
        # the button needs to be disabled because it sometimes
        # reads double clicks and tries to execute these functions
        # a second time (which fails because the connection is closed,
        # but it throws errors, and that's annoying)
        self.startButton.setEnabled(False)

        location = str(self.locationBox.currentText())
        sortby = str(self.sortBox.currentText())
        sortby2 = str(self.sortBox2.currentText())

        self.abundance_matrix = self.ref_database.get_abundance_matrix(location, sortby, sortby2)

        resource_name = str(self.resourceBox.currentText())
        self.resource_path = os.path.join(self.installed_path, resource_name)

        self._want_to_close = True
        self.close()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # launch filter dialog
        self.fw = FilterWindow()
        self.fw.exec_()

        # set up params dict for chosen algorithm
        params = dict()
        # get chosen algorithm
        algorithm_alias = str(self.fw.algoBox.currentText())
        percent = self.fw.algoPercent.value() # return int
        if algorithm_alias in self.fw.algorithms.use_percent:
            params['percent'] = percent
        scoring_algorithm = self.fw.algorithms.available_algorithms[algorithm_alias]

        # connect to key (handles key_database)
        key_database_path = os.path.join(self.fw.resource_path, 'key_database.db')
        try:
            self.key = Key(key_database_path=key_database_path, scoring_algorithm=scoring_algorithm, params=params)
        except Exception as e:
            connection_error_handler(e)

        # lay out UI
        self.layoutUi()

        # start main loop
        self.mainLoop()

    # overwrite closeEvent to close the database before exiting
    def closeEvent(self, evnt):
        try:
            self.key.key_database.connection.close()
        except Exception as e:
            connection_error_handler(e)
        # exit normally
        evnt.accept()

    def layoutUi(self):
        # set indicative labels for the chosen filters
        self.locationTextLabel.setText('\t'+str(self.fw.locationBox.currentText()))
        self.sortTextLabel.setText('\t'+str(self.fw.sortBox.currentText()))
        self.sortTextLabel2.setText('\t'+str(self.fw.sortBox2.currentText()))

    def mainLoop(self):
        # setting the ref_species list
        self.ref_species = sorted(self.fw.abundance_matrix.items(), key=lambda x: x[1], reverse=True)
        #
        # setting working lists
        # all lists are of the format [ (species, abundance), (...), ...]
        self.init_list = [s for s in self.ref_species if s[0] in self.key.key_list]
        #
        self.possible_list = self.init_list.copy()
        self.mistaken_list = list()
        self.impossible_list = list()
        #
        # history keeping (for back button functionality)
        self.couplet_history = list()
        self.pl_history = list()
        self.ml_history = list()
        self.il_history = list()
        #
        # invoking first couplet
        self.get_current_couplet()
        self._enable_choose_button()
        self._enable_skip_button()
        self._enable_back_button() # just to test, should remain false
        #
        # run first display update
        self.update_couplet_display()
        self.update_lists_display()
        #
        # setting up buttons
        self.chooseButton.pressed.connect(self.onChoose)
        self.skipButton.pressed.connect(self.onSkip)
        self.backButton.pressed.connect(self.onBack)
        #
        self.zeroPicForwdButton.pressed.connect(self.onZeroPicForwd)
        self.zeroPicBackButton.pressed.connect(self.onZeroPicBack)
        self.onePicForwdButton.pressed.connect(self.onOnePicForwd)
        self.onePicBackButton.pressed.connect(self.onOnePicBack)
        #
        # setting up actions menu
        self.actionLaunchFilterWindow.triggered.connect(self.onLaunchFilterWindow)

    def _reverse(self, option):
        rev = {'0': '1', '1': '0'}
        return rev[option]

    def _select(self, option, species_list, reverse=False):
        """
        This returns species matching the option (fuzzy match, eg. 1 matches 1, 01 and 10). If reverse=True and couplet weight > 0 returns species matching the opposite option (fuzzy match, eg. 1 matches 0, 01 and 10). If reverse=True and couplet weight == 0 returns the empty list.
        """
        select_list = list()
        for sp in species_list:
            if reverse and self.key.key_database.get_weight(self.current_couplet) > 0.0 and self._reverse(option) in self.key.key_database.get_state(sp[0], self.current_couplet):
                select_list.append(sp)
            elif option in self.key.key_database.get_state(sp[0], self.current_couplet):
                select_list.append(sp)
        return select_list

    def update_lists(self, option):
        # storing current couplet
        self.couplet_history.append(self.current_couplet)
        #
        # storing current state of lists
        self.pl_history.append(self.possible_list.copy())
        self.ml_history.append(self.mistaken_list.copy())
        self.il_history.append(self.impossible_list.copy())
        #
        # building new lists
        # selects all species that match the chosen option
        new_pl = self._select(option, self.possible_list)
        # if the couplet is untrustworthy (weight > 0.0)
        # selects all species that match the opposite chosen option
        new_ml = [s for s in self._select(option, self.possible_list, reverse=True) if s not in new_pl]
        # stores all other couplets
        new_il = [s for s in self.init_list if s not in new_pl+new_ml]
        #
        # reseting lists to new
        self.possible_list = new_pl.copy()
        self.mistaken_list = new_ml.copy()
        self.impossible_list = new_il.copy()

    def get_current_couplet(self):
        species_list = self.possible_list + self.mistaken_list
        self.current_couplet = self.key.choose_new_couplet(species_list)

    def skip_current_couplet(self):
        self.current_couplet = self.key.skip_new_couplet()

    def choose_option(self, option):
        self.update_lists(option)
        self.get_current_couplet()

    def reload_last(self):
        # reload current_couplet
        self.current_couplet = self.couplet_history.pop(-1)
        #
        # reload lists
        self.possible_list = self.pl_history.pop(-1)
        self.mistaken_list = self.ml_history.pop(-1)
        self.impossible_list = self.il_history.pop(-1)

    def _enable_choose_button(self):
        if self.current_couplet != 'End of Key':
            self.chooseButton.setEnabled(True)
        else:
            self.chooseButton.setEnabled(False)

    def _enable_skip_button(self):
        if self.key.len_candidate_couplets > 1:
            self.skipButton.setEnabled(True)
        else:
            self.skipButton.setEnabled(False)

    def _enable_back_button(self):
        if len(self.couplet_history) > 0:
            self.backButton.setEnabled(True)
        else:
            self.backButton.setEnabled(False)

    def _get_cached(self, url):
        path = os.path.join(self.fw.resource_path, 'images')
        file = url.split('/')[-1]
        return  os.path.join(path, file)

    def display_picture(self, picture_list, index, widget):
        # display a picture from picture_list
        pixmap = QtGui.QPixmap(self._get_cached(picture_list[index]))
        pixmap= pixmap.scaledToWidth(300)
        widget.setPixmap(pixmap)

    def _enable_switch_images(self,):
        # zero pic
        if self.current_zero_pic+1 < len(self.zero_pic_list):
            self.zeroPicForwdButton.setEnabled(True)
        else:
            self.zeroPicForwdButton.setEnabled(False)
        #
        if self.current_zero_pic > 0:
            self.zeroPicBackButton.setEnabled(True)
        else:
            self.zeroPicBackButton.setEnabled(False)
        #
        # one pic
        if self.current_one_pic+1 < len(self.one_pic_list):
            self.onePicForwdButton.setEnabled(True)
        else:
            self.onePicForwdButton.setEnabled(False)
        #
        if self.current_one_pic > 0:
            self.onePicBackButton.setEnabled(True)
        else:
            self.onePicBackButton.setEnabled(False)

    def update_pictures_display(self):
        # enable pic switching
        self._enable_switch_images()
        #
        # show couplet pics | 0th pic is always present
        self.display_picture(self.zero_pic_list, self.current_zero_pic, self.zeroPicLabel)
        self.display_picture(self.one_pic_list, self.current_one_pic, self.onePicLabel)

    def update_couplet_display(self):
        # display couplet name
        self.coupletLabel.setText(self.current_couplet)
        #
        # End of key branch
        if self.current_couplet == 'End of Key':
            zero_text, one_text = '', ''
            zero_pic = one_pic = os.path.join(os.path.dirname(sys.argv[0]), 'cache', 'images', '_end_of_key.png')
        else:
            # get couplet info
            zero_text, zero_pic, one_text, one_pic = self.key.key_database.get_couplet(self.current_couplet)
        #
        # show couplet texts
        self.zeroTextLabel.setText(zero_text)
        self.oneTextLabel.setText(one_text)
        #
        # get images list
        self.zero_pic_list = zero_pic.split(',')
        self.one_pic_list = one_pic.split(',')
        #
        # set current shown pics (0th always exists)
        self.current_zero_pic = 0
        self.current_one_pic = 0
        #
        # show pics
        self.update_pictures_display()

    def update_lists_display(self):
        # reset pl
        self.possibleList.clear()
        for item in self.possible_list:
            self.possibleList.addItem(f'{item[0]} ({str(item[1])})')
        # reset ml
        self.mistakenList.clear()
        for item in self.mistaken_list:
            self.mistakenList.addItem(f'{item[0]} ({str(item[1])})')
        # reset il
        self.impossibleList.clear()
        for item in self.impossible_list:
            self.impossibleList.addItem(f'{item[0]} ({str(item[1])})')

    def onChoose(self):
        # get option
        if self.radioButtonZero.isChecked():
            option = '0'
        elif self.radioButtonOne.isChecked():
            option = '1'
        #
        # run key update
        self.choose_option(option)
        #
        # run display update
        self.update_couplet_display()
        self.update_lists_display()
        #
        # enable buttons
        self._enable_choose_button()
        self._enable_skip_button()
        self._enable_back_button()

    def onSkip(self):
        # run key update
        self.skip_current_couplet()
        #
        # run display update
        self.update_couplet_display()

    def onBack(self):
        # run key update
        self.reload_last()
        #
        # run display update
        self.update_couplet_display()
        self.update_lists_display()
        #
        # enable buttons
        self._enable_choose_button()
        self._enable_skip_button()
        self._enable_back_button()

    def onZeroPicForwd(self):
        # set current zero pic
        self.current_zero_pic += 1
        #
        # show pics
        self.update_pictures_display()

    def onZeroPicBack(self):
        # set current zero pic
        self.current_zero_pic -= 1
        #
        # show pics
        self.update_pictures_display()

    def onOnePicForwd(self):
        # set current one pic
        self.current_one_pic += 1
        #
        # show pics
        self.update_pictures_display()

    def onOnePicBack(self):
        # set current one pic
        self.current_one_pic -= 1
        #
        # show pics
        self.update_pictures_display()

    def onLaunchFilterWindow(self):
        # restart program
        self.close()
        self.__init__()
        self.show()

####
def connection_error_handler(e):
    error_dialog = QtWidgets.QMessageBox()
    error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
    error_dialog.setText('connection failed with following error:\n\nerr code: {}\nerr msg.: {}\n\ncontact your database admin'.format(e.args[0], e.args[1]))
    sys.exit(error_dialog.exec_())

####
def main():
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
