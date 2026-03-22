CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TABLE IF NOT EXISTS transactions (
    id UUID PRIMARY KEY,
    customer_origin UUID NOT NULL,
    customer_destination UUID,
    amount DECIMAL(10,2) NOT NULL,                    
    transaction_type VARCHAR(50) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT fk_transactions_origin 
        FOREIGN KEY (customer_origin) 
        REFERENCES customers(id)
        ON DELETE RESTRICT,
    
    CONSTRAINT fk_transactions_destination 
        FOREIGN KEY (customer_destination) 
        REFERENCES customers(id) 
        ON DELETE SET NULL
);
 
CREATE INDEX IF NOT EXISTS idx_transactions_origin ON transactions(customer_origin);
CREATE INDEX IF NOT EXISTS idx_transactions_destination ON transactions(customer_destination);
CREATE INDEX IF NOT EXISTS idx_transactions_type ON transactions(transaction_type);
CREATE INDEX IF NOT EXISTS idx_transactions_date ON transactions(transaction_date);

 
CREATE TRIGGER update_transactions_updated_at 
    BEFORE UPDATE ON transactions
    FOR EACH ROW 
    EXECUTE FUNCTION update_updated_at_column();