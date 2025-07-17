CREATE DOMAIN PosInteger AS INTEGER
    check(value > 0);

CREATE DOMAIN Valuta AS CHAR(3)
    check(value ~ '^[A-Z]{3}$');

CREATE TYPE Denaro AS
    (importo PosInteger, valuta Valuta);


CREATE TABLE Progetto(
    nome VARCHAR PRIMARY KEY,
    budget Denaro
);

CREATE TABLE Dipartimento(
    nome VARCHAR PRIMARY KEY,
    telefono VARCHAR,
    direttore INTEGER
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

CREATE TABLE Partecipa(
    id_impiegato INTEGER,
    nome_progetto VARCHAR,
    PRIMARY KEY (id_impiegato, nome_progetto),
    FOREIGN KEY (id_impiegato) REFERENCES Impiegato(id),
    FOREIGN KEY (nome_progetto) REFERENCES Progetto(nome)
);

ALTER TABLE Dipartimento
    ADD CONSTRAINT direttore AS FOREIGN KEY (direttore) REFERENCES Impiegato(id);

