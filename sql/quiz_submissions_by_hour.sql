/*
  File: quiz_submissions_by_hour.sql
  Author: Mwikali Muoki
  Date: 2025-04-09
  Description:
    This script determines the number of quiz submissions by the hour of day.
    It assumes that quiz submissions are recorded in the mdl_logstore_standard_log table with an event name
    such as 'quiz_submitted' (adjust the event name if needed).
*/

-- Extract quiz submission counts by hour (0-23)
SELECT 
    EXTRACT(HOUR FROM TO_TIMESTAMP(timecreated))::INTEGER AS hour_of_day,
    COUNT(*) AS submission_count
FROM mdl_logstore_standard_log
WHERE eventname = 'quiz_submitted'
GROUP BY hour_of_day
ORDER BY hour_of_day;

-- Submission counts along with the date
SELECT 
    TO_CHAR(TO_TIMESTAMP(timecreated), 'YYYY-MM-DD') AS submission_date,
    EXTRACT(HOUR FROM TO_TIMESTAMP(timecreated))::INTEGER AS hour_of_day,
    COUNT(*) AS submission_count
FROM mdl_logstore_standard_log
WHERE eventname = 'quiz_submitted'
GROUP BY submission_date, hour_of_day
ORDER BY submission_date, hour_of_day;
