--1--
select codice, comp
from volo
where durataminuti > 180;

--2--
select comp
from volo
where durataminuti > 180;

--3--
select codice, comp
from arrpart
where partenza = 'CIA';

--4--
select comp
from arrpart
where arrivo = 'FCO';

--5--
select codice, comp
from arrpart
where partenza ='FCO' and arrivo = 'JFK';

--6--
select comp
from arrpart
where partenza = 'FCO' and arrivo = 'JFK';

--7--
select distinct c.nome
from Compagnia as c, Volo as v, ArrPart as ap, LuogoAeroporto as lp, LuogoAeroporto as la
where v.comp = c.nome
  and ap.codice = v.codice
  and ap.comp = v.comp
  and ap.partenza = lp.aeroporto
  and ap.arrivo = la.aeroporto
  and lp.citta = 'Roma'
  and la.citta = 'New York';

--8--
select distinct a.codice, a.nome, l.citta
from aeroporto as a, luogoaeroporto as l, arrpart as ap
where a.codice = l.aeroporto
	and a.codice = ap.partenza
	and ap.comp = 'MagicFly';

--9--
select distinct v.codice, v.comp, ap.partenza, ap.arrivo
from volo as v, arrpart as ap, aeroporto as a1, aeroporto as  a2, luogoaeroporto as l1, luogoaeroporto as l2
where ap.codice = v.codice
  and ap.partenza = a1.codice
  and ap.arrivo = a2.codice
  and a1.codice = l1.aeroporto
  and a2.codice = l2.aeroporto
  and l1.citta = 'Roma'
  and l2.citta = 'New York';

--10--
select distinct
  v1.comp as compagnia,
  v1.codice as codice_volo_1,
  ap1.partenza,
  ap1.arrivo as scalo,
  v2.codice as codice_volo_2,
  ap2.arrivo
from volo as v1, volo as v2,
     arrpart as ap1, arrpart as ap2,
     aeroporto as  a_partenza, aeroporto as a_arrivo,
     luogoaeroporto as l_part, luogoaeroporto as l_arr
where v1.codice = ap1.codice
  and v2.codice = ap2.codice
  and v1.comp = v2.comp
  and ap1.arrivo = ap2.partenza
  and ap1.partenza = a_partenza.codice
  and ap2.arrivo = a_arrivo.codice
  and a_partenza.codice = l_part.aeroporto
  and a_arrivo.codice = l_arr.aeroporto
  and l_part.citta = 'Roma'
  and l_arr.citta = 'New York';

--11--
select c.nome
from arrpart as ap, compagnia as c
where  c.nome = ap.comp
	and ap.partenza = 'FCO'
	and ap.arrivo = 'JFK'
	and c.annofondaz is not null;