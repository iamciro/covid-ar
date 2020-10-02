# KIVYMD
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

# ASSETS
from assets import texts as txt

# Class to open and close dialog
class Dialog:

	dialog = None

	# Open dialog
	def open(self, message=''):
		self.dialog = MDDialog(
			text=message,
			buttons=[
				MDFlatButton(
						text=txt.DIALOG_BUTTON_TEXT,
						on_press=self.close
				)
			],
		)
		self.dialog.open()

	# Close dialog
	def close(self, *args):
		self.dialog.dismiss(force=True)
