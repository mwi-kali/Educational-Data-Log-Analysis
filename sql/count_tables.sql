/*
  File: count_tables.sql
  Author: Mwikali Muoki
  Date: 2025-04-09
  Description:
    This script counts the total number of tables in the public schema of the Moodle PostgreSQL database.
    It helps to understand the overall database size and complexity.
*/

-- Count the total number of tables in the 'public' schema
SELECT COUNT(*) AS total_tables
FROM information_schema.tables
WHERE table_schema = 'public';

-- List all table names along with their table type for further inspection.
SELECT table_name, table_type
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;
