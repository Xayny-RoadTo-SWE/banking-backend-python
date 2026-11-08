CREATE TABLE IF NOT EXISTS persons(
    person_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    full_name VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE, 
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(20),
    sex CHAR(1),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices para busca rapida
CREATE INDEX IF NOT EXISTS idx_person_full_name ON persons(full_name);
CREATE INDEX IF NOT EXISTS idx_customers_birth_date ON persons(birth_date);
