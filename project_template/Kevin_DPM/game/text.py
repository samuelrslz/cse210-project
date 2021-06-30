import arcade

class Text():
    

    def __init__(self, text, x, y):
        
        self.text = text
        self._x = x
        self._y = y

    def set_x(self, x):
        self._x = x

    def get_x(self):
        return self._x
    
    def set_y(self, y):
        self._y = y

    def get_y(self):
        return self._y
        
    def set_text(self, text):
        self._x = text

    def get_text(self):
        return self._text