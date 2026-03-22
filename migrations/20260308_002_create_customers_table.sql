CREATE TABLE IF NOT EXISTS customers (
    id uuid DEFAULT uuidv7() PRIMARY KEY,                         
    birth_date TIMESTAMP NOT NULL,
    document_type VARCHAR(32) NOT NULL,
    document_number VARCHAR(128) NOT NULL UNIQUE,
    amount DECIMAL(10,2) DEFAULT 0,                    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP      
);

-- Índices para performance
CREATE INDEX IF NOT EXISTS idx_customers_full_name ON customers(full_name);
CREATE INDEX IF NOT EXISTS idx_customers_document_type ON customers(document_type);
CREATE INDEX IF NOT EXISTS idx_customers_document_number ON customers(document_number);
CREATE INDEX IF NOT EXISTS idx_customers_birth_date ON customers(birth_date);

-- Trigger para atualizar updated_at automaticamente
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_customers_updated_at 
    BEFORE UPDATE ON customers
    FOR EACH ROW 
    EXECUTE FUNCTION update_updated_at_column();S idx_customers_document_number ON customers(document_number);