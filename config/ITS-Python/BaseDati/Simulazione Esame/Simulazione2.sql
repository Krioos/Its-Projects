--1) Quali sono le persone con stipendio di al massimo 40000 euro
select nome, stipendio
from Persona
where stipendio <= 40000;

--2) Quali sono i ricercatori che lavorano ad almeno un
--   progetto e hanno uno stipendio di al massimo 40000
select distinct p.id, p.nome, p.cognome 
from Persona as p
inner join AttivitaProgetto as ap on ap.persona = p.id
where p.posizione = 'Ricercatore' and p.stipendio <= 40000;

--3) Qual è il budget totale dei progetti nel db
select sum(budget) as budget_totale
from Progetto;

--4) Qual è il budget totale dei progetti a cui lavora ogni
--   persona. Per ogni persona restituire nome, cognome e
--   budget totale dei progetti nei quali è coinvolto.
select p.id, p.nome, p.cognome, sum(pr.budget) as budget_totale
from AttivitaProgetto as ap
inner join Persona as p on p.id = ap.persona
inner join Progetto as pr on pr.id = ap.progetto
group by p.id;

--5) Qual è il numero di progetti a cui partecipa ogni
--   professore ordinario. Per ogni professore ordinario,
--   restituire nome, cognome, numero di progetti nei quali è
--   coinvolto
select p.nome, p.cognome, count(ap.progetto) as totale_progetti
from Persona as p
inner join AttivitaProgetto as ap on ap.persona = p.id
where p.posizione = 'Professore Ordinario'
group by p.id;

--6) Qual è il numero di assenze per malattia di ogni
--   professore associato. Per ogni professore associato,
--   restituire nome, cognome e numero di assenze per
--   malattia
select p.nome, p.cognome, count(a.id) as numero_assenze
from Assenza as a
inner join Persona as p on p.id = a.persona
where a.tipo = 'Malattia'
group by p.id;

--7) Qual è il numero totale di ore, per ogni persona, dedicate
--   al progetto con id '5'. Per ogni persona che lavora al
--   progetto, restituire nome, cognome e numero di ore totali
--   dedicate ad attività progettuali relative al progetto
select p.nome, p.cognome, sum(ap.oreDurata) as ore_totali
from AttivitaProgetto as ap
inner join Persona as p on p.id = ap.persona
where ap.progetto = 5
group by p.id;

--8) Qual è il numero medio di ore delle attività progettuali
--   svolte da ogni persona. Per ogni persona, restituire nome,
--   cognome e numero medio di ore delle sue attività
--   progettuali (in qualsivoglia progetto)
select p.nome, p.cognome, avg(ap.oreDurata) as durata_media
from Persona as p
inner join AttivitaProgetto as ap on ap.persona = p.id
group by p.id;

--9) Qual è il numero totale di ore, per ogni persona, dedicate
--   alla didattica. Per ogni persona che ha svolto attività
--   didattica, restituire nome, cognome e numero di ore totali
--   dedicate alla didattica 
select 
from 