from Course_work.components.data_base import *


class ModelCommon(object):

    OK = 'ok'
    ERROR = 'error'

    DATA_BASE = "order/json_file.html"

    def data_base_load(self):
        JSON = data_base_load(self.DATA_BASE)
        return JSON
