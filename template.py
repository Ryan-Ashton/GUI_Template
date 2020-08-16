from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase

from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast


class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class Example(MDApp):
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
            preview=False)
        #self.ext = ['xlsx'] # Need to work out how to find excel files


    def file_manager_open(self):
        self.file_manager.show(r'C:\Users\Admin\OneDrive\Documents')  # output manager to the screen
        self.manager_open = True

    def ext(self):
      '''check''' # Need to work out how to find excel files

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

Example().run()