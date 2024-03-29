import re
from datetime import datetime
import json
import locale
import pygame
import os


class App:
    def __init__(self):
        self.Levels, self.Users, self.Fonts, self.Config, self.Colours = "", "", "", "", ""
        self.bag = {}
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.cwd = os.path.dirname(os.path.abspath(__file__))
        self.load_all()

    def load_all(self):
        self.load_Colours()
        self.load_Config()
        self.load_Fonts()
        self.load_Levels()
        self.load_Users()

    def load_Levels(self):
        with open(os.path.join(self.cwd, 'levels.json')) as data:
            self.Levels = type("Levels", (), json.load(data))

    def load_Users(self):
        with open(os.path.join(self.cwd, 'users.json')) as data:
            self.Users = type("Users", (), json.load(data))

    def load_Fonts(self):
        with open(os.path.join(self.cwd, 'details.json')) as data:
            self.Fonts = type("Fonts", (), json.load(data)['fonts'])

    def load_Config(self):
        with open(os.path.join(self.cwd, 'details.json')) as data:
            self.Config = type("Config", (), json.load(data)['config'])

    def load_Colours(self):
        with open(os.path.join(self.cwd, 'details.json')) as data:
            self.Colours = type("Colours", (), json.load(data)['colours'])


class Helpers:

    @staticmethod
    def number_format(number):
        locale.setlocale(locale.LC_ALL, 'en_US')
        return locale.format("%d", number, grouping=True)

    @staticmethod
    def current_time():
        return datetime.now().strftime('%I:%M %p')

    @staticmethod
    def validate(text):
        regex = re.compile(r'^[A-Za-z]{3}\d{3}$')
        if regex.match(text):
            return text
        else:
            return False

    @staticmethod
    def smart_translate(self, text_string):
        try:
            new_string = re.search("{(.*?)}", text_string)
            if new_string:
                for i in new_string.groups():
                    text_string = text_string.replace("{" + i + "}", str(eval(i)), 3)
                return text_string
            else:
                return text_string
        except Exception as e:
            print('[ERROR] could not evaluate smart attribute string. ')
        finally:
            return text_string

    @staticmethod
    def font(app, font, size):
        cwd = os.path.dirname(os.path.abspath(__file__))
        return pygame.font.Font(os.path.join(cwd, '../resources/fonts/') + getattr(app.Fonts, font), size)
