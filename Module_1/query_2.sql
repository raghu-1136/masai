-- Step 1: CTE to compute each customer's total spending on completed orders
WITH customer_spending AS (
    -- TODO: implement this CTE
    SELECT 
       c.customer_id,
       c.customer_name,
       SUM( o.quantity * p.price) as total_spend
    FROM orders o
    JOIN products p on o.product_id = p.product_id
    JOIN customers c on o.customer_id = c.customer_id
    WHERE o.status = 'completed'
    GROUP BY c.customer_id,c.customer_name
),
-- Step 2: CTE to compute average spending across all customers
average_spending AS (
    -- TODO: implement this CTE
    SELECT 
       AVG(total_spend) as avg_spend
    FROM customer_spending

)
-- Step 3: Return customers whose total exceeds the average
-- TODO: implement the final SELECT query to retrieve qualifying customers
SELECT
   customer_name,
   total_spend
FROM customer_spending,average_spending
WHERE total_spend > avg_spend
ORDER BY total_spend DESC;
