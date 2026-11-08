CREATE TABLE IF NOT EXISTS accounts(

    account_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id UUID NOT NULL,

    account_number VARCHAR(20) UNIQUE NOT NULL,
    balance NUMERIC(15,2) NOT NULL DEFAULT 0
        CHECK (balance >= 0),

    status VARCHAR(20) DEFAULT 'ACTIVE'
        CHECK (
            status IN (
                'ACTIVE',
                'BLOCKED',
                'CLOSED'
            )
        ),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_account_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(person_id)
);

CREATE TRIGGER update_accounts_updated_at
    BEFORE UPDATE ON accounts
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();