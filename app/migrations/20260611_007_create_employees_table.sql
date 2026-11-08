CREATE TABLE IF NOT EXISTS employees (
    person_id UUID PRIMARY KEY,
    employee_code VARCHAR(20) NOT NULL UNIQUE,
    hire_date DATE NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_employees_person
        FOREIGN KEY (person_id)
        REFERENCES persons(person_id)

);

CREATE TRIGGER update_employees_updated_at
    BEFORE UPDATE ON employees
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();