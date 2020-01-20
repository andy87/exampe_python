from Course_work.components.data_base import *
from Course_work.models.ModelCommon import *

class ModelOrder(ModelCommon):

    DATA_BASE = "JSON/order.json"

    PAGE_ADD = "order/add_order.html"



    def create(self, request, position = "user"):

        req = request.POST
        Login = req.get("login")
        Pass = req.get("password")

        json = data_base_load(self.DATA_BASE)

        if (Login in json['users']):
            resp = {
                'status': self.ERROR,
                'error': 'Пользователь уже зрегистрирован',
                'redirect': '/error'
            }
        else:
            json['users'].append({
                "login": Login,
                "id": len(json['users']) + 1,
                "password": Pass,
                "position": position,
                "status": "true"
            })

            data_base_update(self.DATA_BASE, json)

            session = request.session
            user = json['users'][-1]

            session.set_expiry(86400)
            session['id'] = user['id']
            session['login'] = user['login']
            session['position'] = user['position']
            session['status'] = user['status']

            resp = {
                'status': self.OK,
                'redirect': '/account'
            }

        return resp

