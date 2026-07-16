SELECT
    customer_id,
    SUM(transaction_amount) AS total_amount
FROM transactions
GROUP BY customer_id;