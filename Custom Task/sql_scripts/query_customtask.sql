SELECT utca FROM ASSZISZTENS;
SELECT kkod FROM KORHAZ WHERE VAROS="MISKOLC";
SELECT asszisztens.nev FROM asszisztens INNER JOIN verado ON asszisztens.aszemigz=verado.aszemigz WHERE verado.nev= "BERENYI MIKLOS";
SELECT verado.nev FROM verado INNER JOIN ver ON verado.vtajszam= ver.vtajszam ORDER BY veradasideje;