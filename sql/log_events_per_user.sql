/*
  File: log_events_per_user.sql
  Author: Mwikali Muoki
  Date: 2025-04-09
  Description:
    This script counts the number of log events per user for a specific set of actions (verbs).
    Actions include: loggedin, viewed, started, submitted, uploaded, updated, searched, resumed, answered, attempted, and abandoned.
    The query aggregates these events per user from the mdl_logstore_standard_log table.
*/

-- Count log events per user for specified actions
SELECT 
    userid,
    SUM(CASE 
            WHEN action IN (
                'loggedin', 
                'viewed', 
                'started', 
                'submitted', 
                'uploaded', 
                'updated', 
                'searched', 
                'resumed', 
                'answered', 
                'attempted', 
                'abandoned'
            ) THEN 1 
            ELSE 0 
        END) AS event_count
FROM mdl_logstore_standard_log
GROUP BY userid
ORDER BY event_count DESC;

-- List also the breakdown of each action type per user.
SELECT 
    userid,
    SUM(CASE WHEN action = 'loggedin' THEN 1 ELSE 0 END) AS loggedin_count,
    SUM(CASE WHEN action = 'viewed' THEN 1 ELSE 0 END) AS viewed_count,
    SUM(CASE WHEN action = 'started' THEN 1 ELSE 0 END) AS started_count,
    SUM(CASE WHEN action = 'submitted' THEN 1 ELSE 0 END) AS submitted_count,
    SUM(CASE WHEN action = 'uploaded' THEN 1 ELSE 0 END) AS uploaded_count,
    SUM(CASE WHEN action = 'updated' THEN 1 ELSE 0 END) AS updated_count,
    SUM(CASE WHEN action = 'searched' THEN 1 ELSE 0 END) AS searched_count,
    SUM(CASE WHEN action = 'resumed' THEN 1 ELSE 0 END) AS resumed_count,
    SUM(CASE WHEN action = 'answered' THEN 1 ELSE 0 END) AS answered_count,
    SUM(CASE WHEN action = 'attempted' THEN 1 ELSE 0 END) AS attempted_count,
    SUM(CASE WHEN action = 'abandoned' THEN 1 ELSE 0 END) AS abandoned_count
FROM mdl_logstore_standard_log
GROUP BY userid
ORDER BY userid;
