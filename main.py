# KIVY
from kivy.lang import Builder
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import ScreenManager, Screen

#KIVYMD
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

# Modules
import os.path as os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class DisplotScreen(Screen):
	title = 'COVID-AR'
	subtitle = 'Análisis de la COVID-19'

class LineplotScreen(Screen):

	title = 'COVID-AR'
	subtitle = 'Análisis de la COVID-19'

	dialog = None

	def show_alert_dialog(self):
		if not self.dialog:
			self.dialog = MDDialog(
				text="El archivo no se encontró",
				buttons=[
					MDFlatButton(
						text="Aceptar",
						on_press=self.dialog_close
					)
				],
			)
		self.dialog.open()

	def dialog_close(self, *args):
		self.dialog.dismiss(force=True)
		
	def get_filename(self, filename):

		# Check if filename exists
		if os.isfile(filename):

			# Set seaborn theme
			sns.set_theme(style="darkgrid")

			# Read file and transform it to a dataframe object
			csv_file = pd.read_csv(filename)

			# Plot dataframe
			lp = sns.lineplot(data=csv_file, x="month", y="cases_number", sort=False)

			lp.set(xlabel="Mes", ylabel="Número de casos")

			# Show plot
			plt.show()
		else:
			self.show_alert_dialog()


class HomeScreen(Screen):
	title = 'COVID-AR'
	subtitle = 'Análisis de la COVID-19'

class MainApp(MDApp):
	def build(self):
		self.title = "COVID-AR | COVID-19 Cases Analyzer"

		return Builder.load_file("kv/test.kv")

MainApp().run()