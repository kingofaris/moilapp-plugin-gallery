from src.plugin_interface import PluginInterface
from models.model_apps import Model
from PyQt6 import QtCore, QtGui, QtWidgets
from .ui_main import Ui_Main
from .ui_stackedwidget import Ui_Form
from .ui_viewer import Ui_Viewer
from .search_model import DDGImageSearch, ImageDownload
import os, numpy, cv2, copy

class VideoThread(QtCore.QThread):
    change_pixmap_signal = QtCore.pyqtSignal(numpy.ndarray)

    def __init__(self, cap):
        super().__init__()
        self._run_flag = True
        self.mutex = QtCore.QMutex()
        self.cap = cap

    def run(self):
        while self._run_flag:
            img = self.cap.frame()
            self.change_pixmap_signal.emit(img)

    def stop(self):
        with QtCore.QMutexLocker(self.mutex):
            self._run_flag = False

class AddImageFiles(QtCore.QThread):
    add_pixmap = QtCore.pyqtSignal(str, str, str)

    def __init__(self, image_files, full_path):
        super().__init__()
        self.files = image_files
        self.path = full_path

    def run(self):
        path = self.path
        for image_file in self.files:
            full_path = os.path.join(path, image_file)
            self.add_pixmap.emit(image_file, full_path, full_path)
        self.quit()

class Controller(QtWidgets.QWidget):
    def __init__(self, model: Model):
        super().__init__()
        self.ui = Ui_Form()
        self.model = model

        self.editing = False
        # Hard coded default config
        self.moildev_function = 'original'
        self.moildev_anypoint_mode = 'Mode 1'
        self.moildev_panorama_mode = 'Car'
        
        self.ui.setupUi(self)
        self.ui.main = self.findChild(QtWidgets.QWidget, 'main')
        self.ui.viewer = self.findChild(QtWidgets.QWidget, 'viewer')
        Ui_Main().setupUi(self.ui.main)
        Ui_Viewer().setupUi(self.ui.viewer)

        self.set_stylesheet()

        self.ui.main.searchFrame = self.findChild(QtWidgets.QFrame, 'searchFrame')
        self.ui.main.zoomSlider = self.findChild(QtWidgets.QSlider, 'galleryZoomSlider')
        self.ui.main.selectFolderButton = self.findChild(QtWidgets.QPushButton, 'selectFolderButton')
        self.ui.main.searchImagesButton = self.findChild(QtWidgets.QPushButton, 'searchImagesButton')
        self.ui.main.searchButton = self.findChild(QtWidgets.QPushButton, 'searchButton')
        self.ui.main.openCameraButton = self.findChild(QtWidgets.QPushButton, 'openCameraButton')
        self.ui.main.galleryList = self.findChild(QtWidgets.QListWidget, 'galleryList')
        self.ui.main.imageLimit = self.findChild(QtWidgets.QSpinBox, 'imageLimit')
        self.ui.main.searchLine = self.findChild(QtWidgets.QLineEdit, 'searchLine')

        self.ui.viewer.zoomSlider = self.findChild(QtWidgets.QSlider, 'viewerZoomSlider')
        self.ui.viewer.imageLabel = self.findChild(QtWidgets.QLabel, 'imageLabel')
        self.ui.viewer.prevButton = self.findChild(QtWidgets.QPushButton, 'prevButton')
        self.ui.viewer.nextButton = self.findChild(QtWidgets.QPushButton, 'nextButton')
        self.ui.viewer.backButton = self.findChild(QtWidgets.QPushButton, 'backButton')
        self.ui.viewer.compareViewButton = self.findChild(QtWidgets.QPushButton, 'compareViewButton')
        self.ui.viewer.moildevFrame = self.findChild(QtWidgets.QFrame, 'moildevFrame')
        self.ui.viewer.moildevButton = self.findChild(QtWidgets.QPushButton, 'moildevButton')
        self.ui.viewer.navButtonsFrame = self.findChild(QtWidgets.QFrame, 'navButtonsFrame')
        self.ui.viewer.recenterButton = self.findChild(QtWidgets.QPushButton, 'recenterButton')
        self.ui.viewer.anypointButton = self.findChild(QtWidgets.QPushButton, 'anypointButton')
        self.ui.viewer.panoramaButton = self.findChild(QtWidgets.QPushButton, 'panoramaButton')
        self.ui.viewer.panoramaGroup = self.findChild(QtWidgets.QButtonGroup, 'panoramaGroup')
        self.ui.viewer.anypointGroup = self.findChild(QtWidgets.QButtonGroup, 'anypointGroup')
        self.ui.viewer.recenterGroup = self.findChild(QtWidgets.QButtonGroup, 'recenterGroup')

        self.ui.viewer.recenterButton.clicked.connect(self.set_viewer_recenter)
        self.ui.viewer.anypointButton.clicked.connect(self.set_viewer_anypoint)
        self.ui.viewer.panoramaButton.clicked.connect(self.set_viewer_panorama)

        self.ui.viewer.panoramaGroup.buttonClicked.connect(self.moildev_param_panorama)
        self.ui.viewer.anypointGroup.buttonClicked.connect(self.moildev_param_anypoint)
        self.ui.viewer.recenterGroup.buttonClicked.connect(self.moildev_param_recenter)

        self.ui.viewer.moildevButton.clicked.connect(self.toggle_moildev)
        self.ui.viewer.moildevFrame.setVisible(False)
        self.ui.viewer.compareViewButton.setVisible(False)

        self.ui.main.zoomSlider.setRange(25, 250)
        self.ui.main.zoomSlider.setSliderPosition(100)
        self.ui.main.zoomSlider.valueChanged.connect(self.set_gallery_zoom)

        self.ui.main.searchFrame.setVisible(False)
        self.ui.viewer.navButtonsFrame.setVisible(False)
        
        self.ui.main.selectFolderButton.clicked.connect(self.select_folder)
        self.ui.main.searchImagesButton.clicked.connect(self.toggle_search)
        self.ui.main.searchButton.clicked.connect(self.search_images)
        self.ui.main.openCameraButton.clicked.connect(self.open_camera)

        self.ui.main.galleryList.setIconSize(self.ui.main.galleryList.sizeHint())
        self.ui.main.galleryList.setViewMode(QtWidgets.QListWidget.ViewMode.IconMode)
        self.ui.main.galleryList.setResizeMode(QtWidgets.QListWidget.ResizeMode.Adjust)
        self.ui.main.galleryList.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.NoDragDrop)
        self.ui.main.galleryList.itemClicked.connect(self.view_image)

        self.search_image_limit = 20
        self.ui.main.imageLimit.setRange(1, 300)
        self.ui.main.imageLimit.setValue(20)
        self.ui.main.imageLimit.valueChanged.connect(self.change_image_limit)

        self.ui.viewer.zoomSlider.setRange(25, 150)
        self.ui.viewer.zoomSlider.setSliderPosition(100)
        self.ui.viewer.zoomSlider.valueChanged.connect(self.set_viewer_zoom)
        
        self.ui.viewer.backButton.clicked.connect(self.back_to_main)

        self.select_folder(startup=True)

    def set_stylesheet(self):
        [button.setStyleSheet(self.model.style_pushbutton()) for button in self.findChildren(QtWidgets.QPushButton)]
        [radio_button.setStyleSheet(self.model.style_radio_button()) for radio_button in self.findChildren(QtWidgets.QRadioButton)]
        [label.setStyleSheet(self.model.style_label()) for label in self.findChildren(QtWidgets.QLabel)]
        [label.setStyleSheet(self.model.style_frame_object()) for label in self.findChildren(QtWidgets.QFrame)]
        self.findChildren(QtWidgets.QSlider)[0].setStyleSheet(self.model.style_slider())
        self.findChildren(QtWidgets.QSpinBox)[0].setStyleSheet(self.model.style_spinbox())
        self.findChildren(QtWidgets.QCheckBox)[0].setStyleSheet(self.model.style_checkbox())
        self.findChildren(QtWidgets.QLineEdit)[0].setStyleSheet(self.model.style_line_edit())
        
    def set_gallery_zoom(self, value):
        self.ui.main.galleryList.setIconSize(QtCore.QSize(value * 0.01 * 256, value * 0.01 * 192))

    def select_folder(self, startup=False):
        self.ui.main.galleryList.clear()
        if startup:
            current_script_path = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(current_script_path, '../../../example_source')
        else:
            path = self.model.select_directory()
        if not os.path.exists(path):
            return
        if not os.path.isdir(path):
            path = os.path.dirname(path)
        
        supported_extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp']
        image_files = [file for file in os.listdir(path) if file[-4:].strip('.').lower() in supported_extensions]
        
        self.add_images_thread = AddImageFiles(image_files, path)
        self.add_images_thread.add_pixmap.connect(self.add_image_to_gallery)
        self.add_images_thread.start()
        
    def open_camera(self):
        # source_type, cam_type, source_media, parameter_name = self.model.select_media_source()
        self.cam = self.model.moil_camera('opencv_usb_cam', 0)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.findChild(QtWidgets.QFrame, 'navButtonsFrame').setVisible(False)
        self.camera_thread = VideoThread(self.cam)
        self.camera_thread.change_pixmap_signal.connect(self.update_image)
        self.camera_thread.start()
        
    def toggle_moildev(self):
        self.ui.viewer.moildevFrame.setVisible(not self.ui.viewer.moildevFrame.isVisible())
        self.ui.viewer.compareViewButton.setVisible(not self.ui.viewer.compareViewButton.isVisible())
        # self.ui.viewer.navButtonsFrame.setVisible(not self.ui.viewer.navButtonsFrame.isVisible())
        # self.moildev_param = self.model.select_parameter_name()
        self.moildev_param = 'entaniya_vr220_11'
        self.moildev = self.model.connect_to_moildev(parameter_name=self.moildev_param)

    def update_image(self, img):
        height, width, channel = img.shape
        qimage = QtGui.QImage(img.data, width, height, width * channel, QtGui.QImage.Format.Format_RGB888).rgbSwapped()
        self.viewer_pixmap = QtGui.QPixmap.fromImage(qimage)
        self.set_viewer_zoom()
    
    def toggle_search(self):
        self.ui.main.searchFrame.setVisible(not self.ui.main.searchFrame.isVisible())

    def search_images(self):
        self.ui.main.galleryList.clear()
        query = self.ui.main.searchLine.text()
        if query:
            self.search_thread = DDGImageSearch(query, self.search_image_limit)
            self.search_thread.start()
            self.search_thread.fetched.connect(self.add_image_to_gallery)
            
    def add_image_to_gallery(self, title, image_url, thumbnail):
        if type(thumbnail) == str:
            pixmap = QtGui.QPixmap(thumbnail)
        else:
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(thumbnail)
        
        item = QtWidgets.QListWidgetItem()
        item.setIcon(QtGui.QIcon(pixmap))
        item.setText(title)
        item.setWhatsThis(image_url)

        self.ui.main.galleryList.addItem(item)
        
    def view_image(self, item):
        image_uri = item.whatsThis()
        self.ui.stackedWidget.setCurrentIndex(1)
        if image_uri.startswith('http'):
            self.image_download_thread = ImageDownload(image_uri)
            self.image_download_thread.fetched.connect(self.open_viewer)
            self.image_download_thread.start()
        else:
            self.open_viewer(image_uri)

    def open_viewer(self, file_or_bytes):
        if type(file_or_bytes) == str:
            pixmap = QtGui.QPixmap(file_or_bytes)
        else:
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(file_or_bytes)
        if not self.editing:
            self.orig_pixmap = pixmap
        self.viewer_pixmap = pixmap
        self.set_viewer_zoom()

    def set_viewer_zoom(self, value=None):
        if not value:
            value = self.ui.viewer.zoomSlider.value()
        
        w = int(self.ui.viewer.imageLabel.size().width() * value * 0.01)
        h = int(self.ui.viewer.imageLabel.size().height() * value * 0.01)
        scaled = QtCore.QSize(w, h)
        pixmap = self.viewer_pixmap.scaled(scaled, aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.viewer.imageLabel.setPixmap(pixmap)

    def change_image_limit(self, value):
        self.search_image_limit = value

    def back_to_main(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.viewer.imageLabel.clear()
        self.editing = False
        try:
            self.camera_thread.stop()
            self.cam.close()
            # self.findChild(QtWidgets.QFrame, 'navButtonsFrame').setVisible(True)
        except:
            pass
            
    ### MOILDEV STUFF

    def set_viewer_recenter(self):
        self.moildev_function = 'recenter'
        self.set_viewer_moildev()
    
    def set_viewer_anypoint(self):
        self.moildev_function = 'anypoint'
        self.set_viewer_moildev()

    def set_viewer_panorama(self):
        self.moildev_function = 'panorama'
        self.set_viewer_moildev()

    def moildev_param_panorama(self, button):
        self.moildev_panorama_mode = button.text()
        self.set_viewer_moildev()

    def moildev_param_anypoint(self, button):
        self.moildev_anypoint_mode = button.text()
        self.set_viewer_moildev()

    def moildev_param_recenter(self, button):
        button.text()
        self.set_viewer_moildev()
        
    def set_viewer_moildev(self):
        image = self.orig_pixmap
        width = image.width()
        height = image.height()
        image = pixmap_to_cv2(image)
        self.editing = True
        moildev = self.moildev
        if self.moildev_function == 'anypoint':
            if self.moildev_anypoint_mode == 'Mode 1':
                anypoint_m1 = moildev.anypoint_mode1(image, 90, 180, 2)
                result = cv2.resize(anypoint_m1, (width, height))
            else:
                anypoint_m2 = moildev.anypoint_mode2(image, -90, 0, 0, 2)
                result = cv2.resize(anypoint_m2, (width, height))
        elif self.moildev_function == 'panorama':
            if self.moildev_panorama_mode == 'Car':
                panorama_car = moildev.panorama_car(image, 110, 80, 0, 0.25, 0.75, 0, 1)
                result = cv2.resize(panorama_car, (width * 2, height))
            else:
                panorama_tube = moildev.panorama_tube(image, 10, 110)
                result = cv2.resize(panorama_tube, (width, height))
        elif self.moildev_function == 'recenter':
            result = moildev.recenter(image, 110, 25, 10)
        elif self.moildev_function == 'maps anypoint':
            if self.moildev_anypoint_mode == 'Mode 1':
                map_X, map_Y = moildev.maps_anypoint_mode1(90, 180, 2)
                anypoint_maps_m1 = cv2.remap(image, map_X, map_Y, cv2.INTER_LINEAR)
                result = cv2.resize(anypoint_maps_m1, (width, height))
            else:
                map_X, map_Y = moildev.maps_anypoint_mode2(-90, 0, 0, 2)
                anypoint_maps_m2 = cv2.remap(image, map_X, map_Y, cv2.INTER_CUBIC)
                result = cv2.resize(anypoint_maps_m2, (width, height))
        else:
            self.editing = False
            self.pixmap = self.orig_pixmap
            self.set_viewer_zoom()
            return
        self.update_image(result)

def pixmap_to_cv2(pixmap):
    qimage = pixmap.toImage()
    width = qimage.width()
    height = qimage.height()
    bytes_per_line = qimage.bytesPerLine()
    image_format = qimage.format()

    if image_format == QtGui.QImage.Format.Format_RGB32:
        qimage = qimage.convertToFormat(QtGui.QImage.Format.Format_RGB888)
    ptr = qimage.constBits()
    ptr.setsize(qimage.sizeInBytes())
    arr = numpy.array(ptr).reshape(height, width, 3)
    cv2_image = cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)

    return cv2_image


class GalleryShowcase(PluginInterface):
    def __init__(self):
        super().__init__()
        self.widget = None
        self.description = "This is a plugins application"

    def set_plugin_widget(self, model):
        self.widget = Controller(model)
        return self.widget

    def set_icon_apps(self):
        return "icon.png"

    def change_stylesheet(self):
        self.widget.set_stylesheet()