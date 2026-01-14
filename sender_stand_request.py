import configuration
import requests
import data

#Creacion de nuevo usuario.
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

authToken = post_new_user(data.user_body)
print(authToken.status_code)
print(authToken.json())

#Creacion de un kit para el usuario.
def post_new_client_kit(kit_body,auth_Token):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=data.kit_headers)

response = post_new_client_kit(data.kit_body,authToken)
print(response.status_code)
print(response.json())
