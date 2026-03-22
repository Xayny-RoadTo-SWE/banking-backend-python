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

CREATE_TRANSACTION = """
INSERT INTO transactions (
    account_id,
    transaction_type,
    amount
) VALUES (
    %s,
    %s,
    %s
)
"""

TRANSACTION_WITHDRAW = """
    INSERT INTO transactions (
        customer_origin_id,,
        amount
    ) VALUES (
        %s,
        'withdraw',
        %s
    )
"""
TRANSACTION_DEPOSIT = """
    INSERT INTO transactions (
        customer_origin_id,
        amount
    ) VALUES (
        %s,
        'deposit',
        %s
    )
"""
TRANSACTION_TRANSFER = """
    INSERT INTO transactions (
        customer_origin_id,
        customer_destination_id,
        amount
    ) VALUES (
        %s,
        %s,
        'transfer',
        %s
)
        """
TRANSACTION_GET_CUSTOMER_AMOUNT = """
    SELECT amount FROM customers WHERE id=%s
"""