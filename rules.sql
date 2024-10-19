CREATE TABLE rules (
    id SERIAL PRIMARY KEY,
    rule_string TEXT NOT NULL,
    ast_json TEXT NOT NULL,  -- Store AST as a JSON structure
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE attributes_catalog (
    attribute_name VARCHAR(50) PRIMARY KEY,
    data_type VARCHAR(20) NOT NULL
);
