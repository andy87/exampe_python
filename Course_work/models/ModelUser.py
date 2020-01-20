from Course_work.components.data_base import *
from Course_work.models.ModelCommon import *

class ModelUser(ModelCommon):

    DATA_BASE = "JSON/users.json"

    PAGE_ADD = "user/add_user.html"



    def create(self, request, position = "user"):

        req = request.POST
        Login = req.get("login")
        Pass = req.get("password")

        json = self.data_base_load()

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

            user = json['users'][-1]

            self.update_session(self, request, user)

            resp = {
                'status': self.OK,
                'redirect': '/account'
            }

        return resp



    def Authorize(self, request):
        JSON = self.data_base_load()
        users = JSON['users']
        req = request.POST
        # Проверка входа в систему
        Login = req.get("login")
        Pass = req.get("password")
        error = 'Неправильно введён логин или пароль'
        #       checkFunc = "none"

        for user in users:
            if user['login'] == Login and user['password'] == Pass:
                self.update_session(self, request, user)
                return True

        return False



    def update_session(self, request, user):
        session = request.session

        session.set_expiry(86400)
        session['id'] = user['id']
        session['login'] = user['login']
        session['position'] = user['position']
        session['status'] = user['status']
