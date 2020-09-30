# KIVY
from kivy.lang import Builder
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import ScreenManager, Screen

#KIVYMD
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

# Modules
import os.path as os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class Dialog:

	dialog = None

	def open(self, message=''):
		if not self.dialog:
			self.dialog = MDDialog(
				text=message,
				buttons=[
					MDFlatButton(
							text="Aceptar",
							on_press=self.close
					)
				],
			)
		self.dialog.open()

	def close(self, *args):
		self.dialog.dismiss(force=True)
		#print("Hola")


class DisplotScreen(Screen):
	title = 'COVID-AR'
	subtitle = 'Análisis de la COVID-19'

	def __init__(self, **kwargs): 
		super(DisplotScreen, self).__init__(**kwargs)
		self.dialog = Dialog()

	def get_filename(self, filename):

		# Check if filename exists
		if os.isfile(filename):

			# Get filename and extension
			filename, extension = os.splitext(filename)
			
			# Check if the file is a .csv file
			if extension == '.csv': 
				# Set seaborn theme
				sns.set_theme(style="darkgrid")

				# Read file and transform it to a dataframe object
				csv_file = pd.read_csv(filename)

				# Obtenemos la información por edad
				ages = csv_file['age']

				# Lo graficamos en un gráfico de distribución
				sns.displot(ages)

				# Show plot
				plt.show()
			else: 
				self.dialog.open("El archivo que ingresaste no tiene un formato válido")
			
		else:
			self.dialog.open('El archivo no se encontró')


class LineplotScreen(Screen):

	title = 'COVID-AR'
	subtitle = 'Análisis de la COVID-19'
	
	def __init__(self, **kwargs): 
		super(LineplotScreen, self).__init__(**kwargs)
		self.dialog = Dialog()

	def get_filename(self, filename):

		# Check if filename exists
		if os.isfile(filename):

			# Get filename and extension
			filename, extension = os.splitext(filename)

			# Check if the file is a .csv file
			if extension == '.csv':
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
				self.dialog.open("El archivo que ingresaste no tiene un formato válido") 

		else:
			self.dialog.open('El archivo no se encontró')


class HomeScreen(Screen):
	title = 'COVID-AR'
	subtitle = 'Análisis de la COVID-19'

class MainApp(MDApp):
	def build(self):
		self.title = "COVID-AR | COVID-19 Cases Analyzer"

		return Builder.load_file("kv/test.kv")

MainApp().run()
