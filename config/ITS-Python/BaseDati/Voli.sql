CREATE DOMAIN Posint as INTEGER
        check (value > 0);

CREATE DOMAIN PosintGr1900 as INTEGER
        check (value > 1900);


CREATE TABLE Nazione(
    nome VARCHAR PRIMARY KEY
);

CREATE TABLE Città(
    id INTEGER PRIMARY KEY,
    nome VARCHAR,
    abitanti Posint,
    nazione VARCHAR,
    FOREIGN KEY (nazione) REFERENCES Nazione(nome)
);

CREATE TABLE CompagniaAerea(
    nome VARCHAR PRIMARY KEY,
    fondazione PosintGr1900,
    città INTEGER,
    FOREIGN KEY (città) REFERENCES Città(id)
);

CREATE TABLE Aereoporto(
    codice VARCHAR PRIMARY KEY,
    nome VARCHAR,
    città INTEGER,
    FOREIGN KEY (città) REFERENCES Città(id)
);

CREATE TABLE Volo(
    codice VARCHAR PRIMARY KEY,
    durata_minuti Posint,
    partenza VARCHAR,
    arrivo VARCHAR,
    compagnia VARCHAR,
    FOREIGN KEY (partenza) REFERENCES Aereoporto(codice),
    FOREIGN KEY (arrivo) REFERENCES Aereoporto(codice),
    FOREIGN KEY (compagnia) REFERENCES CompagniaAerea(nome),
    CHECK (partenza <> arrivo)
);