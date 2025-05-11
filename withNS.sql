WITH MonthlyPayments AS (
    SELECT
        EXTRACT(MONTH FROM payment_date) AS month,
        COUNT(*) AS total_count,
        SUM(amount) AS total_amount
    FROM payment
    GROUP BY month
),
MikePayments AS (
    SELECT
        EXTRACT(MONTH FROM payment_date) AS month,
        COUNT(*) AS mike_count,
        SUM(amount) AS mike_amount
    FROM payment
    WHERE staff_id = 1
    GROUP BY month
),
JonPayments AS (
    SELECT
        EXTRACT(MONTH FROM payment_date) AS month,
        COUNT(*) AS jon_count,
        SUM(amount) AS jon_amount
    FROM payment
    WHERE staff_id = 2
    GROUP BY month
)
SELECT
    mp.month,
    mp.total_count,
    mp.total_amount,
    COALESCE(mike.mike_count, 0) AS mike_count,
    COALESCE(mike.mike_amount, 0) AS mike_amount,
    COALESCE(jon.jon_count, 0) AS jon_count,
    COALESCE(jon.jon_amount, 0) AS jon_amount
FROM MonthlyPayments mp
LEFT JOIN MikePayments mike ON mp.month = mike.month
LEFT JOIN JonPayments jon ON mp.month = jon.month
ORDER BY mp.month;