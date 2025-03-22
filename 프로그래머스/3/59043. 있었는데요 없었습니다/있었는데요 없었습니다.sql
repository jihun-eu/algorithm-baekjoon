-- 코드를 입력하세요
SELECT INS.ANIMAL_ID, INS.NAME
FROM ANIMAL_INS INS
JOIN (SELECT ANIMAL_ID, DATETIME FROM ANIMAL_OUTS) OUTS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE OUTS.DATETIME < INS.DATETIME
ORDER BY INS.DATETIME;