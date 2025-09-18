WITH first_login AS (
    SELECT a.player_id, MIN(a.event_date) AS first_login
    FROM Activity a
    GROUP BY a.player_id
),
consec_login AS (
    SELECT
        COUNT(A.player_id) AS num_logins
    FROM
        first_login F
    JOIN
        Activity A ON F.player_id = A.player_id
        AND F.first_login = DATE_SUB(A.event_Date, INTERVAL 1 DAY)
)

SELECT
    ROUND(
        (SELECT c.num_logins FROM consec_login c)
        / (SELECT COUNT(f.player_id) FROM first_login f)
        , 2) AS fraction;
