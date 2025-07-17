SELECT
  P.name AS party_name,
  S.name AS state_name,
  COUNT(V.id) AS voter_count
FROM Voters AS V
JOIN Parties AS P
  ON V.party_id = P.id
JOIN States AS S
  ON V.state_id = S.id
WHERE
  UPPER(S.name) LIKE 'N%'
GROUP BY
  P.name,
  S.name
ORDER BY
  P.name DESC,
  S.name ASC;