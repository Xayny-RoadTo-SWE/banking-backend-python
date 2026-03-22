CREATE TABLE IF NOT EXISTS customers (
    id UUID PRIMARY KEY,                          
    full_name VARCHAR(255) NOT NULL,                    
    birth_date DATE NOT NULL,
    document_type VARCHAR(32) NOT NULL,
    document_number VARCHAR(128) NOT NULL UNIQUE,  
    manager_id UUID,                    
    deleted_at TIMESTAMP,                  
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   

    CONSTRAINT fk_customers_manager 
        FOREIGN KEY (manager_id) 
        REFERENCES users(id)  
        ON DELETE SET NULL
);

-- Índices para busca rapida
CREATE INDEX IF NOT EXISTS idx_customers_full_name ON customers(full_name);
CREATE INDEX IF NOT EXISTS idx_customers_document_type ON customers(document_type);
CREATE INDEX IF NOT EXISTS idx_customers_document_number ON customers(document_number);
CREATE INDEX IF NOT EXISTS idx_customers_birth_date ON customers(birth_date);

-- Trigger para atualizar o updated_at automaticamente (Padrão Postgres)
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
    EXECUTE PROCEDURE update_updated_at_column();