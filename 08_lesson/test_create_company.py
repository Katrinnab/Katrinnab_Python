from company import Company
import pytest

base_url = 'https://ru.yougile.com/api-v2'
login = 'katrinnab@yandex.ru'
password = 'Artem2005'


@pytest.fixture()
def company():
    comp = Company('My Project', 'katrinnab@yandex.ru', 'Artem2005')
    auth = comp.authorization()
    comp.get_API_Key(auth)
    yield comp


def test_projects(company):
    # Проверка API ключа
    assert company.API_Key != ''

    # Получить список проектов
    project_list = company.get_project_list()
    before_count = len(project_list.get('content'))

    # Добавление проекта
    params_to_add = {
                        "title": "My New Project",
    }
    project = company.add_project(params_to_add)
    id_project = project.get('id')
    project = company.get_project(id_project)

    assert company.get_project(id_project)['title'] == 'My New Project'
    assert company.get_project(id_project)['timestamp'] != ''

    # Новый список проектов
    project_list = company.get_project_list()
    after_count = len(project_list.get('content'))

    # Проверка добавления проекта
    assert after_count - before_count == 1

    # Получить данные о проекте
    project = company.get_project(id_project)

    # Обновить проект
    data = {
            "title": "Smart Co and nothing else",
            }
    company.update_project(id_project, data)
    new_name = 'Smart Co and nothing else'
    assert company.get_project(id_project)['title'] == new_name
    assert company.get_project(id_project)['timestamp'] != ''

    # Задать проекту пустое имя
    data = {
            "title": "",
            }
    company.update_project(id_project, data)
    assert id_project != ''

    # Получить список проектов
    project_list = company.get_project_list()
    before_count = len(project_list.get('content'))

    # Удалить проект
    company.delete_project(id_project)
    deleted_project = company.get_project(id_project)
    assert deleted_project['deleted'] is True

    project_list = company.get_project_list()
    after_count = len(project_list.get('content'))
    assert before_count - after_count == 1

    # Проект без данных
    params_to_add = None
    project = company.add_project(params_to_add)
    id_project = project.get('id')
    project = company.get_project(id_project)
    assert id_project != ''


# test_projects(company)
