CREATE TABLE IF NOT EXISTS customers (
    person_id UUID PRIMARY KEY,                                          
    manager_id UUID,

    risk_profile VARCHAR(20)
    DEFAULT 'LOW'
    CHECK (
        risk_profile IN (
            'LOW',
            'MEDIUM',
            'HIGH'
    )
),

    customer_since DATE DEFAULT CURRENT_DATE,
    
    status VARCHAR(20)
        NOT NULL DEFAULT 'ACTIVE'
        CHECK (
            status IN (
                'ACTIVE',
                'INACTIVE',
                'BLOCKED'
            )
        ),

    deleted_at TIMESTAMP,  

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   

    CONSTRAINT fk_customer_person
    FOREIGN KEY (person_id)
    REFERENCES persons(person_id),



    CONSTRAINT fk_customer_manager
    FOREIGN KEY (manager_id)
    REFERENCES employees(person_id)
);

CREATE INDEX IF NOT EXISTS idx_customers_manager_id
ON customers(manager_id);

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
    EXECUTE FUNCTION update_updated_at_column();