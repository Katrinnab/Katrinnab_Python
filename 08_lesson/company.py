import requests


class Company:
    def __init__(self, company, login, password):
        self.company = company
        self.login = login
        self.password = password
        self.base_url = 'https://ru.yougile.com/api-v2'
        self.key_id = ''

    def authorization(self):
        authorize = {
            'login': f"{self.login}",
            'password': f"{self.password}",
            'name': self.company
        }
        headers = {
                    'Content-Type': 'application/json'
                    }
        response = requests.post(self.base_url+'/auth/companies',
                                 json=authorize,
                                 headers=headers)
        return response.json()

    def get_company_keys(self, response):
        self.key_id = response.get("content")[0]["id"]

        authorize = {
            'login': f"{self.login}",
            'password': f"{self.password}",
            'companyId': self.key_id
        }
        headers = {
                'Content-Type': 'application/json'
        }
        response = requests.post(self.base_url+'/auth/keys/get',
                                 json=authorize,
                                 headers=headers)
        return response.json()

    def get_API_Key(self, response):
        company_keys = self.get_company_keys(response)
        print('company_keys = ', company_keys)
        self.API_Key = company_keys[0].get('key')

    def get_project_list(self):
        if self.API_Key:
            headers = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + self.API_Key
                }
            response = requests.get(self.base_url + '/projects',
                                    headers=headers)
            return response.json()
        else:
            return None

    def add_project(self, params_to_add=None):
        if self.API_Key:
            headers = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + self.API_Key
                }
            response = requests.post(self.base_url + '/projects',
                                     json=params_to_add,
                                     headers=headers)
            return response.json()
        else:
            return None

    def get_project(self, id):
        if self.API_Key:
            headers = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + self.API_Key
                }
            response = requests.get(self.base_url + f'/projects/{id}',
                                    headers=headers)
            return response.json()
        else:
            return None

    def get_project_field(self, id, name):
        # lst_projects = self.get_project_list().get('content')
        lst_projects = self.get_project_list()['content']
        for dct in lst_projects:
            if dct.get('id', '') == id:
                return dct.get(name, '')
        return None

    def update_project(self, id, params_to_update):
        if self.API_Key:
            headers = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + self.API_Key
                }
            response = requests.put(self.base_url + f'/projects/{id}',
                                    json=params_to_update,
                                    headers=headers)
            return response.json()

    def delete_project(self, id):
        if self.API_Key:
            data = {
                    "title": "Smart Co and etc.",
                    "deleted": True,
                    }
            headers = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + self.API_Key
                }
            response = requests.put(self.base_url + f'/projects/{id}',
                                    json=data,
                                    headers=headers)
            return response.json()
