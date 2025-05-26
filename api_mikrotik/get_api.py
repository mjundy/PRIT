from routeros_api import RouterOsApiPool

api_pool = RouterOsApiPool('172.16.1.30', username='testing_api', password='Frina123')
api = api_pool.get_api()

interfaces = api.get_resource('/interface').get()
for i in interfaces:
    print(i['name'])

api_pool.disconnect()
