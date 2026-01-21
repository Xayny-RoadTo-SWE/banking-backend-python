CREATE_USER = """
INSERT INTO users (nome) VALUES (%s);
"""

GET_BALANCE = """
    SELECT saldo from users where user_id = %s
"""

UPDATE_BALANCE = """
    UPDATE users SET saldo = saldo + %s WHERE id = %s
"""

WITHDRAW = """
    UPDATE users SET saldo = saldo - %s WHERE id = %s
"""

TRANSFER = """
    SELECT saldo FROM users WHERE id = %s FOR UPDATE
"""

TRANSFER_BALANCE = """
    SELECT id FROM users WHERE id = %s
"""

WITHDRAW_AMOUNT = """
    UPDATE users SET saldo = saldo - %s WHERE user_id = %s
"""

