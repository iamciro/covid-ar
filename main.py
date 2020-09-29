from kivy.lang import Builder
from kivy.uix.modalview import ModalView

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.uix.filemanager import MDFileManager

class LineplotScreen(Screen):
	title = 'COVID-AR'
	subtitle = 'Análisis de la COVID-19 en Argentina'

class HomeScreen(Screen):
	title = 'COVID-AR'
	subtitle = 'Análisis de la COVID-19 en Argentina'

class MainApp(MDApp):
	def build(self):
		self.title = "COVID-AR | COVID-19 Analyzer for Argentina"

		return Builder.load_file("kv/test.kv")

MainApp().run()