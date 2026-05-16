import pytest
from security.auth_handler import sign_jwt, decode_jwt

def test_generate_and_decode_token():
    # 1. Geramos um token para um e-mail de teste
    test_email = "alex@sunfire.com"
    token_response = sign_jwt(test_email)
    
    token = token_response["access_token"]
    
    # 2. Tentamos decodificar esse mesmo token
    decoded_payload = decode_jwt(token)
    
    # 3. Verificamos se o e-mail dentro do token é o mesmo que enviamos
    assert decoded_payload["user_id"] == test_email
    assert "exp" in decoded_payload

def test_decode_invalid_token():
    # Testamos se um token falso retorna None ou dict vazio conforme seu código
    invalid_token = "token_que_nao_existe_123"
    payload = decode_jwt(invalid_token)
    
    assert payload is None or payload == {}