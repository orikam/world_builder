import json
from cell import Cell

class Database():
    def __init__(self, file_name) -> None:
        with open(file_name, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        if not json_object:
            return
        self.cells = {}
        data = json_object['data']
        self.nb_tiles_width = data['nb_tiles_width']
        self.nb_tiles_hight = data['nb_tiles_hight']
        self.tile_size = data['tile_size']
        self.screen_width = data['screen_width']
        self.screen_height = data['screen_height']
        for cell in json_object['objects']:
            self.cells[cell['id']] = Cell(cell['id'], cell['type'], self.tile_size, cell['file_name'])
