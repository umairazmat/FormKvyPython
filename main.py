import os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import csv
from xml.etree.ElementTree import Element, SubElement, ElementTree

class MyLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Name: '))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        self.add_widget(Label(text='Age: '))
        self.age = TextInput(multiline=False)
        self.add_widget(self.age)
        self.submit = Button(text='Submit in XML')
        self.submit.bind(on_press=self.submit_data)
        self.add_widget(self.submit)
        self.submit = Button(text='Submit in CSV')
        self.submit.bind(on_press=self.submit_data_csv)
        self.add_widget(self.submit)

    def submit_data(self, instance):
        name = self.name.text
        age = self.age.text
        data = Element('inputs')
        person = SubElement(data, 'person')
        person.set('name', name)
        person.set('age', age)
        tree = ElementTree(data)
        if not os.path.exists('data3.xml'):
            tree.write('data3.xml')
        else:
            tree.parse('data3.xml')
            root = tree.getroot()
            person = SubElement(root, 'person')
            person.set('name', name)
            person.set('age', age)
            tree.write('data3.xml')
            
    def submit_data_csv(self, instance):
        name = self.name.text
        age = self.age.text
        filename = 'data.csv'
        with open(filename, mode='a') as file:
            writer = csv.writer(file)
            writer.writerow([name, age])



class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()

