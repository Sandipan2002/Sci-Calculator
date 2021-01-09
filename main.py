from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
#
from math import*
import webbrowser
from random import randint as rand 

π=(22/7)
deg=π/180
__version__="1.0.0"
class MyGrid(GridLayout):
	ip=ObjectProperty(None)
	op=ObjectProperty(None)
	def print_same(self,printable):
		x=self.ip.text 
		y=x+printable
		self.ip.text=y
	def send_mail(self):
		webbrowser.open("mailto:yishu1729@gmail.com?subject=Feedback Of Smart Calculator Of Sandipan&body=Tell me how can I improve this app.")
	def backspace(self):
		x=self.ip.text
		y=list(x)
		if len(y)!=0:
			del y[-1]
		d="".join(y)
		self.ip.text=d
	def clear_all(self):
		self.ip.text=""
		self.op.text=""
	def send_call(self):
		x=self.ip.text
		webbrowser.open("tel:"+x)
	def web_search(self):
		x=self.ip.text
		x=x.replace("+","%2B")
		webbrowser.open("https://www.google.com/search?q="+x)
	def calculate_answer(self):
		x=self.ip.text
		try:
			y=eval(x)
		except Exception as e:
			y=e
		self.op.text=str(y)


class CalApp(App):
	def build(self):
		return MyGrid()


if __name__ == '__main__':
	CalApp().run()