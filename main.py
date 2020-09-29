from kivy.lang import Builder
from kivy.uix.modalview import ModalView

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.uix.filemanager import MDFileManager

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
			print("El archivo NO se encontró")


class HomeScreen(Screen):
	title = 'COVID-AR'
	subtitle = 'Análisis de la COVID-19'

class MainApp(MDApp):
	def build(self):
		self.title = "COVID-AR | COVID-19 Cases Analyzer"

		return Builder.load_file("kv/test.kv")

MainApp().run()