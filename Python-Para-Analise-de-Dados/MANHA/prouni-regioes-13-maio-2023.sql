CREATE DATABASE aulas;

use aulas;

SELECT count(*) FROM prouni;

SELECT * FROM prouni;

SELECT DISTINCT uf_busca from prouni;

SET SQL_SAFE_UPDATES = 0;

ALTER TABLE prouni
add column regiao char(30) after turno;

select uf_busca, regiao from prouni;

update prouni
set regiao =
CASE
    WHEN uf_busca  in ('MS', 'MT', 'GO', 'DF' ) THEN "Centro-Oeste"
    WHEN uf_busca  in ('RS', 'SC', 'PR' ) THEN "Sul"
    WHEN uf_busca  in ('SP', 'MG', 'RJ', 'ES' ) THEN "Sudeste"
    WHEN uf_busca  in ('AM', 'AP', 'AC', 'PA', 'RO', 'RR', 'TO' ) THEN "Norte"
    WHEN uf_busca  in ('BA', 'SE', 'AL', 'PE', 'PB',
					   'RN', 'CE', 'PI', 'MA') THEN "Nordeste"
END;

SELECT * FROM prouni;

SELECT regiao, uf_busca, nome, nota_integral_ampla,
	   mensalidade, bolsa_integral_cotas from prouni;

describe prouni;

SELECT regiao, uf_busca, nome, nota_integral_ampla,
	   mensalidade, bolsa_integral_cotas from prouni
where campus_external_id = 706710 and nome = 'Medicina';

SELECT * from prouni
where campus_external_id = 706710 and nome = 'Medicina';



# Média do Brasil
SELECT nome, FORMAT(min(nota_integral_ampla), 0) AS min_nota,
	   FORMAT(avg(nota_integral_ampla), 0) AS nota,
	   FORMAT(max(nota_integral_ampla), 0) AS max_nota,
	   FORMAT(min(mensalidade),0) as min_mensalidade, 
	   FORMAT(avg(mensalidade),0) as mensalidade, 
       FORMAT(max(mensalidade),0) as max_mensalidade, 
       FORMAT(max(bolsa_integral_cotas),0) as bolsa from prouni
GROUP BY nome  
HAVING nome = 'Medicina';


# Média por regiao - curso medicina
SELECT regiao, nome, FORMAT(min(nota_integral_ampla), 0) AS min_nota,
	   FORMAT(avg(nota_integral_ampla), 0) AS nota,
	   FORMAT(max(nota_integral_ampla), 0) AS max_nota,
	   FORMAT(min(mensalidade),0) as min_mensalidade, 
	   FORMAT(avg(mensalidade),0) as mensalidade, 
       FORMAT(max(mensalidade),0) as max_mensalidade, 
       FORMAT(max(bolsa_integral_cotas),0) as bolsa from prouni
GROUP BY regiao, nome  
HAVING nome = 'Medicina';

SELECT regiao, nome, FORMAT(min(nota_integral_ampla), 0) AS min_nota,
	   FORMAT(avg(nota_integral_ampla), 0) AS nota,
	   FORMAT(max(nota_integral_ampla), 0) AS max_nota,
	   FORMAT(min(mensalidade),0) as min_mensalidade, 
	   FORMAT(avg(mensalidade),0) as mensalidade, 
       FORMAT(max(mensalidade),0) as max_mensalidade, 
       FORMAT(max(bolsa_integral_cotas),0) as bolsa from prouni
GROUP BY regiao, nome
order by nome desc;

select * from prouni;





