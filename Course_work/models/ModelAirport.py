from Course_work.components.data_base import *
from Course_work.models.ModelCommon import *

class ModelAirport(ModelCommon):

    DATA_BASE = "JSON/airports.json"

    PAGE_ADD = "order/add_order.html"


    def detail(self, id):
        air = self.data_base_load()
        air = air['airports'][id]
        resp = {
            'name': air['name'],
            'flights': air['flights']
        }

        return resp



    def getAirLineList(self):
        airports = self.data_base_load()
        len_air = len(airports['airports'])
        num_cell = len_air + (len_air % 3)

        if len_air % 3 == 0:
            p = 0
        elif len_air % 3 == 1:
            p = 2
        elif len_air % 3 == 2:
            p = 1
        len_air_r = len_air + p
        air_list = []

        for i in range(0, len_air_r - 3, 3):
            rand_str = [airports['airports'][i], airports['airports'][i + 1], airports['airports'][i + 2]]
            air_list.append(rand_str)
        if p == 0:
            air_list.append([airports['airports'][len_air_r - 3], airports['airports'][len_air_r - 2],
                             airports['airports'][len_air_r - 1]])
        elif p == 1:
            air_list.append([airports['airports'][len_air_r - 3], airports['airports'][len_air_r - 2], 0])
        elif p == 2:
            air_list.append([airports['airports'][len_air_r - 3], 0, 0])

        return air_list
