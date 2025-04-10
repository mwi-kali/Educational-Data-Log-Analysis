/*
  File: count_records.sql
  Author: Mwikali Muoki
  Date: 2025-04-09
  Description:
    This script counts the number of records in key tables of the Moodle database.
    These tables include logs, user information, course details, modules, grades, and forum interactions.
*/

/* 1. Count records in mdl_logstore_standard_log */
SELECT 'mdl_logstore_standard_log' AS table_name,
       COUNT(*) AS total_records
FROM mdl_logstore_standard_log;

/* 2. Count records in mdl_user */
SELECT 'mdl_user' AS table_name,
       COUNT(*) AS total_records
FROM mdl_user;

/* 3. Count records in mdl_course */
SELECT 'mdl_course' AS table_name,
       COUNT(*) AS total_records
FROM mdl_course;

/* 4. Count records in mdl_modules */
SELECT 'mdl_modules' AS table_name,
       COUNT(*) AS total_records
FROM mdl_modules;

/* 5. Count records in mdl_course_modules */
SELECT 'mdl_course_modules' AS table_name,
       COUNT(*) AS total_records
FROM mdl_course_modules;

/* 6. Count records in mdl_course_modules_completion */
SELECT 'mdl_course_modules_completion' AS table_name,
       COUNT(*) AS total_records
FROM mdl_course_modules_completion;

/* 7. Count records in mdl_grade_items */
SELECT 'mdl_grade_items' AS table_name,
       COUNT(*) AS total_records
FROM mdl_grade_items;

/* 8. Count records in mdl_grade_grades */
SELECT 'mdl_grade_grades' AS table_name,
       COUNT(*) AS total_records
FROM mdl_grade_grades;

/* 9. Count records in mdl_grade_categories */
SELECT 'mdl_grade_categories' AS table_name,
       COUNT(*) AS total_records
FROM mdl_grade_categories;

/* 10. Count records in mdl_grade_items_history */
SELECT 'mdl_grade_items_history' AS table_name,
       COUNT(*) AS total_records
FROM mdl_grade_items_history;

/* 11. Count records in mdl_grade_grades_history */
SELECT 'mdl_grade_grades_history' AS table_name,
       COUNT(*) AS total_records
FROM mdl_grade_grades_history;

/* 12. Count records in mdl_grade_categories_history */
SELECT 'mdl_grade_categories_history' AS table_name,
       COUNT(*) AS total_records
FROM mdl_grade_categories_history;

/* 13. Count records in mdl_forum */
SELECT 'mdl_forum' AS table_name,
       COUNT(*) AS total_records
FROM mdl_forum;

/* 14. Count records in mdl_forum_discussions */
SELECT 'mdl_forum_discussions' AS table_name,
       COUNT(*) AS total_records
FROM mdl_forum_discussions;

/* 15. Count records in mdl_forum_posts */
SELECT 'mdl_forum_posts' AS table_name,
       COUNT(*) AS total_records
FROM mdl_forum_posts;
