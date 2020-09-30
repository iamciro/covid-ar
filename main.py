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

# ASSETS
from assets import texts as txt

class Dialog:

	dialog = None

	# Open dialog
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

	# Close dialog
	def close(self, *args):
		self.dialog.dismiss(force=True)


class DisplotScreen(Screen):

	title = txt.APP_TITLE
	subtitle = txt.APP_SUBTITLE

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
				self.dialog.open(txt.DIALOG_FILE_NOT_VALID)
			
		else:
			self.dialog.open(txt.DIALOG_FILE_NOT_FOUND)


class LineplotScreen(Screen):

	title = txt.APP_TITLE
	subtitle = txt.APP_SUBTITLE

	# Plot info
	plot_title = ''
	x_axis = ''
	y_axis = ''
	xlabel = ''
	ylabel = ''
	
	def __init__(self, **kwargs): 
		super(LineplotScreen, self).__init__(**kwargs)
		self.dialog = Dialog()

	def get_plot(self, file, x_axis, y_axis, xlabel, ylabel,
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


class HomeScreen(Screen):
	title = txt.APP_TITLE
	subtitle = txt.APP_SUBTITLE

class MainApp(MDApp):
	def build(self):
		self.title = txt.APP_NAME

		return Builder.load_file("kv/test.kv")

MainApp().run()
