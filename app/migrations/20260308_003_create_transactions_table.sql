DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_type
        WHERE typname = 'transaction_type_enum'
    ) THEN
        CREATE TYPE transaction_type_enum AS ENUM (
            'DEPOSIT',
            'WITHDRAW',
            'TRANSFER_IN',
            'TRANSFER_OUT'
        );
    END IF;
END $$;

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id UUID PRIMARY KEY DEFAULT gen_random_uuid(), 
    account_id UUID NOT NULL,
    related_account_id UUID REFERENCES accounts(account_id),
    amount NUMERIC (15,2) NOT NULL
    CHECK (amount > 0),                    

    transaction_type transaction_type_enum NOT NULL,
    
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    
    CONSTRAINT fk_transactions_account
        FOREIGN KEY (account_id) 
        REFERENCES accounts(account_id)
        ON DELETE RESTRICT
);
 
    CREATE INDEX idx_transactions_account_date 
    ON transactions(account_id, created_at DESC);