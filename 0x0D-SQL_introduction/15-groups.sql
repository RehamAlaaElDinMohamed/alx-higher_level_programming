-- counts number of occurences of a particular score grouped by the score
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESCi;
