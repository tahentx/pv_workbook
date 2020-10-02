SELECT 
test_groups.name,
COUNT(test_cases.group_name) OVER() AS all_test_cases,
COUNT(SELECT test_cases.status 
      FROM test_cases 
      WHERE status = 'OK') AS passed_test_cases,
FROM test_groups
INNER JOIN test_cases
ON test_groups.name = test_cases.group_name