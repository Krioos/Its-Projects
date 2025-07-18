CREATE DOMAIN PosInteger AS INTEGER
    CHECK(VALUE > 0);

CREATE DOMAIN Valuta AS CHAR(3)
    CHECK(VALUE ~ '^[A-Z]{3}$');

CREATE TYPE Denaro AS
    (importo PosInteger, valuta Valuta);


CREATE TABLE Progetto(
    nome VARCHAR PRIMARY KEY,
    budget Denaro
);

CREATE TABLE Dipartimento(
    nome VARCHAR PRIMARY KEY,
    telefono VARCHAR
);

CREATE TABLE Impiegato(
    id INTEGER PRIMARY KEY,
    nome VARCHAR,
    cognome VARCHAR,
    data_nascita DATE,
    stipendio Denaro,
    data_afferenza DATE,
    dipartimento_afferenza VARCHAR,
    FOREIGN KEY (dipartimento_afferenza) REFERENCES Dipartimento(nome)
);

CREATE TABLE Dirige(
    direttore INTEGER,
    dipartimento VARCHAR,
    PRIMARY KEY (direttore, dipartimento),
    FOREIGN KEY (direttore) REFERENCES Impiegato(id),
    FOREIGN KEY (dipartimento) REFERENCES Dipartimento(nome)
);

CREATE TABLE Partecipa(
    id_impiegato INTEGER,
    nome_progetto VARCHAR,
    PRIMARY KEY (id_impiegato, nome_progetto),
    FOREIGN KEY (id_impiegato) REFERENCES Impiegato(id),
    FOREIGN KEY (nome_progetto) REFERENCES Progetto(nome)
);
