# KIVY
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#KIVYMD
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

# Modules
import os.path as os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ASSETS
from assets import texts as txt
from assets.helpers import Dialog


class DisplotScreen(Screen):

	# Plot info
	plot_title = ''
	column_to_plot = ''
	xlabel = ''
	ylabel = ''

	def __init__(self, **kwargs): 
		super(DisplotScreen, self).__init__(**kwargs)
		self.dialog = Dialog()

	# Verify data
	def verify_textinput_data(self,file, column_to_plot):

		incorrect_data = False

		if len(file) == 0:
			incorrect_data = True
		elif len(column_to_plot) == 0:
			incorrect_data = True

		return incorrect_data

	def get_plot(self, file, column_to_plot, xlabel, ylabel,
				 plot_title):

		# Check data
		incorrect_data = self.verify_textinput_data(file, column_to_plot)

		try:
			if incorrect_data == False:
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

						# Class attributes
						self.plot_title = plot_title
						self.column_to_plot = column_to_plot
						self.xlabel = xlabel
						self.ylabel = ylabel

						# We get data by the column_to_plot arg
						data = csv_file[self.column_to_plot]

						# We plot data in a displot
						dp = sns.displot(data)

						# Set plot info
						dp.set(title=self.plot_title, xlabel=self.xlabel, ylabel=self.ylabel)

						# Show plot
						plt.show()
					else: 
						#print("Archivo no valido")
						self.dialog.open(txt.DIALOG_FILE_NOT_VALID)
					
				else:
					#print("Archivo no encontrado")
					self.dialog.open(txt.DIALOG_FILE_NOT_FOUND)
			else:
				#print("Data incorrecta")
				self.dialog.open(txt.DIALOG_INCORRECT_DATA)

		except KeyError as e:
			#print("Columna incorrecta")
			self.dialog.open(txt.DIALOG_KEY_ERROR)


class LineplotScreen(Screen):

	# Plot info
	plot_title = ''
	x_axis = ''
	y_axis = ''
	xlabel = ''
	ylabel = ''
	
	def __init__(self, **kwargs): 
		super(LineplotScreen, self).__init__(**kwargs)
		self.dialog = Dialog()

	# Verify data
	def verify_textinput_data(self,file, x_axis, y_axis):

		incorrect_data = False

		if len(file) == 0:
			incorrect_data = True
		elif len(x_axis) == 0:
			incorrect_data = True
		elif len(y_axis) == 0:
			incorrect_data = True

		return incorrect_data


	def get_plot(self, file, x_axis, y_axis, xlabel, ylabel,
				 plot_title):

		# Check data
		incorrect_data = self.verify_textinput_data(file, x_axis, y_axis)

		try:
			if incorrect_data == False:
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

						# Class attributes
						self.plot_title = plot_title
						self.x_axis = x_axis
						self.y_axis = y_axis
						self.xlabel = xlabel
						self.ylabel = ylabel

						# Plot dataframe
						#lp = sns.lineplot(data=csv_file, x="month", y="cases_number", sort=False)
						lp = sns.lineplot(data=csv_file, x=self.x_axis, y=self.y_axis, sort=False)

						lp.set(title = self.plot_title, xlabel=self.xlabel, ylabel=self.ylabel)

						# Show plot
						plt.show()
					else: 
						self.dialog.open(txt.DIALOG_FILE_NOT_VALID) 

				else:
					self.dialog.open(txt.DIALOG_FILE_NOT_FOUND)
			else:
				#print("Data incorrecta")
				self.dialog.open(txt.DIALOG_INCORRECT_DATA_LINEPLOT)
		except ValueError as e:
			self.dialog.open(txt.DIALOG_KEY_ERROR_LINEPLOT)


class HomeScreen(Screen):
	pass

class MainApp(MDApp):
	def build(self):
		self.title = txt.APP_NAME

		return Builder.load_file("kv/test.kv")

MainApp().run()
