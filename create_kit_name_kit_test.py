import sender_stand_request
import data

# Función que cambia los valores en el parámetro "name"
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Función para obtener el token de autenticación
def get_new_user_token():
    user_token = sender_stand_request.authToken
    assert user_token.status_code == 201
    assert user_token.json()["authToken"] != ""
    return user_token

# Función de prueba positiva
def positive_assert(name):
    current_body = get_kit_body(name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(current_body,auth_token)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name

# Función de prueba negativa (No se transmiten los datos)
def negative_assert_code_400(name):
    current_body = get_kit_body(name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(current_body,auth_token)
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"
    assert kit_response.json()["message"] == "El nombre debe contener sólo letras latino, " \
                                             "un espacio y un guión. " \
                                             "De 2 a 15 caracteres"

#Prueba 1 Creación de un kit. El parametro "name" contiene 1 caracter
def test_create_kit_1_caracter_in_name_get_success_response():
    positive_assert("a")

#Prueba 2 Creación de un kit. El parametro "name" contiene 511 caracteres
def test_create_kit_511_caracters_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabC")

#Prueba 3 Creación de un kit. El parametro "name" contiene 0 caracteres
def test_create_kit_0_caracter_in_name_get_fail_response():
    negative_assert_code_400("")

#Prueba 4 Creación de un kit. El parametro "name" contiene 512 caracteres
def test_create_kit_512_caracters_in_name_get_fail_response():
    negative_assert_code_400("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcD")

#Prueba 5 Creación de un kit. El parametro "name" contiene caracteres especiales
def test_create_kit_especial_caracters_in_name_get_success_response():
    positive_assert("\"№%@\",")

#Prueba 6 Creación de un kit. El parametro "name" contiene espacios
def test_create_kit_space_caracter_in_name_get_success_response():
    positive_assert("A Aaa")

#Prueba 7 Creación de un kit. El parametro "name" contiene números
def test_create_kit_number_caracters_in_name_get_success_response():
    positive_assert("1234")

#Prueba 8 Creación de un kit. El parametro "name" no pasa en la solicitud
def test_create_kit_blank_espace_in_name_get_fail_response():
    current_body = data.kit_body.copy()
    current_body.pop("name")
    negative_assert_code_400(current_body)

#Prueba 9 Creación de un kit. El parametro "name" contiene un parametro diferente
def test_create_kit_diferent_caracter_in_name_get_fail_response():
    negative_assert_code_400(1234)