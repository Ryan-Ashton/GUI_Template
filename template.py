from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.boxlayout import MDBoxLayout

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase

from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast

from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDFlatButton, MDRoundFlatIconButton
from kivy.uix.textinput import TextInput 
from kivy.uix.widget import Widget

import pandas as pd


class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class Example(MDApp):

    featureOne = ObjectProperty(None)
    featureTwo = ObjectProperty(None)

    def build(self):
      return Builder.load_file('template.kv')

    def on_start(self):
      ''''''
      # for i in ["first tab", "second tab", "third tab"]:
      #     self.root.ids.tabs.add_widget(Tab(text=f"{i}"))

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
      instance_tab.ids.label.text = "" # Can add text here

#########################################################################
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            ext=[".csv", ".xlsx"])


    def file_manager_open(self):
        self.file_manager.show(r'C:\Users\Admin\OneDrive\Documents')  # output manager to the screen
        self.manager_open = True


    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''
        self.exit_manager()
        # toast(path)

        # Use "path" to get the path of file selected from file manager, then can feed it into pandas
        df = pd.read_excel(path)
        df.to_csv("I DID IT.csv")


    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = True
        self.file_manager.close()   

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


    def btn(self):

        # Get the text inputs from the kivy file

        featureOne = self.root.ids.featureOne
        featureTwo = self.root.ids.featureTwo

        print(featureOne.text, featureTwo.text)



    class ScrollableLabel(ScrollView):
        text = StringProperty('')

Example().run()