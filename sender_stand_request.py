import configuration
import requests
import data #импорт изформации из файла data

#получения апи документации
def get_docs(): #получения апи документации
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

#Логи основного сервера
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        params={"count":20})

#Получение информации из таблицы БД
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
    #Получение информации из таблицы БД

#Создание пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки


#функция на вход получает список id продуктов products_ids
def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids, #тело
                         headers=data.headers) #заголовки запроса


