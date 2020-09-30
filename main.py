# KIVY
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#KIVYMD
from kivymd.app import MDApp
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

	# Plot info
	plot_title = ''
	column_to_plot = ''
	xlabel = ''
	ylabel = ''

	def __init__(self, **kwargs): 
		super(DisplotScreen, self).__init__(**kwargs)
		self.dialog = Dialog()

	def get_plot(self, file, column_to_plot, xlabel, ylabel,
				 plot_title):

		# Check if filename exists
		if os.isfile(file):

			# Get filename and extension
			filename, extension = os.splitext(file)
			
			# Check if the file is a .csv file
			if extension == '.csv': 
				# Set seaborn theme
				sns.set_theme(style="darkgrid")

				# Read file and transform it to a dataframe object
				csv_file = pd.read_csv(file)

				# Class' column_to_plot attribute
				self.plot_title = plot_title
				self.column_to_plot = column_to_plot
				self.xlabel = xlabel
				self.ylabel = ylabel

				# We get data by the column_to_plot arg
				data = csv_file[self.column_to_plot]

				# We plot data in a displot
				dp = sns.displot(data)

				dp.set(xlabel=self.xlabel, ylabel=self.ylabel)

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
