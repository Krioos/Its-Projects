BEGIN TRANSACTION;

CREATE DOMAIN PosInteger AS INTEGER CHECK (VALUE >= 0);
CREATE DOMAIN StringaM AS VARCHAR(100);
CREATE DOMAIN CodIATA AS CHAR(3);

CREATE TABLE Compagnia (
    nome StringaM PRIMARY KEY,
    annoFondaz PosInteger
);

CREATE TABLE Aeroporto (
    codice CodIATA PRIMARY KEY,
    nome StringaM NOT NULL
);

CREATE TABLE LuogoAeroporto (
    aeroporto CodIATA PRIMARY KEY,
    citta StringaM NOT NULL,
    nazione StringaM NOT NULL
);

CREATE TABLE Volo (
    codice PosInteger NOT NULL,
    comp StringaM NOT NULL,
    durataMinuti PosInteger NOT NULL,
    PRIMARY KEY (codice, comp),
    FOREIGN KEY (comp) REFERENCES Compagnia(nome)
);

CREATE TABLE ArrPart (
    codice PosInteger NOT NULL,
    comp StringaM NOT NULL,
    arrivo CodIATA NOT NULL,
    partenza CodIATA NOT NULL,
    PRIMARY KEY (codice, comp),
    FOREIGN KEY (arrivo) REFERENCES Aeroporto(codice),
    FOREIGN KEY (partenza) REFERENCES Aeroporto(codice)
);

ALTER TABLE Volo
ADD CONSTRAINT fk_vo_arrpart
FOREIGN KEY (codice, comp) REFERENCES ArrPart(codice, comp)
DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE ArrPart
ADD CONSTRAINT fk_arr_vo
FOREIGN KEY (codice, comp) REFERENCES Volo(codice, comp)
DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE Aeroporto
ADD CONSTRAINT fk_aer_luogo
FOREIGN KEY (codice) REFERENCES LuogoAeroporto(aeroporto)
DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE LuogoAeroporto
ADD CONSTRAINT fk_luogo_aer
FOREIGN KEY (aeroporto) REFERENCES Aeroporto(codice)
DEFERRABLE INITIALLY DEFERRED;

COMMIT;
