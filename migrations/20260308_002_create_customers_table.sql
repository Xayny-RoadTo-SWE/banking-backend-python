CREATE TABLE IF NOT EXISTS customers (
    id BIGSERIAL PRIMARY KEY,                          
    full_name VARCHAR(255) NOT NULL,                   
    birth_date TIMESTAMP NOT NULL,
    document_type VARCHAR(32) NOT NULL,
    document_number VARCHAR(128) NOT NULL UNIQUE,
    amount DECIMAL(10,2) DEFAULT 0,                     
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP      
 
CREATE INDEX IF NOT EXISTS idx_customers_full_name ON customers(full_name);
CREATE INDEX IF NOT EXISTS idx_customers_document_type ON customers(document_type);
CREATE INDEX IF NOT EXIST-- migrations/20260308_002_create_customers_table.sql
-- Versão para PostgreSQL

CREATE TABLE IF NOT EXISTS customers (
    id BIGSERIAL PRIMARY KEY,                          -- AUTO_INCREMENT → BIGSERIAL
    full_name VARCHAR(255) NOT NULL,                   -- 256 → 255 (padrão PostgreSQL)
    birth_date TIMESTAMP NOT NULL,
    document_type VARCHAR(32) NOT NULL,
    document_number VARCHAR(128) NOT NULL UNIQUE,
    amount DECIMAL(10,2) DEFAULT 0,                    -- FLOAT → DECIMAL (mais preciso para dinheiro)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP     -- Removeu ON UPDATE (não existe no PostgreSQL)
);

-- Índices para performance
CREATE INDEX IF NOT EXISTS idx_customers_full_name ON customers(full_name);
CREATE INDEX IF NOT EXISTS idx_customers_document_type ON customers(document_type);
CREATE INDEX IF NOT EXISTS idx_customers_document_number ON customers(document_number);
CREATE INDEX IF NOT EXISTS idx_customers_birth_date ON customers(birth_date);

-- Trigger para atualizar updated_at automaticamente (opcional, mas recomendado)
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
CREATE INDEX IF NOT EXISTS idx_customers_birth_date ON customers(birth_date);

 
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
    EXECUTE FUNCTION update_updated_at_column();