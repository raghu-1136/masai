-- Step 1: Define a CTE that computes each day's revenue from completed orders only
WITH daily_sales AS (
    SELECT
        o.order_date,
        -- TODO: compute total revenue for this date (quantity * matching product price),
        SUM(o.quantity * p.price ) AS daily_revenue
    FROM orders o JOIN products p 
    ON o.product_id = p.product_id
    -- counting completed orders only
    WHERE o.status = 'completed'
    -- TODO: filter to completed orders and group by order_date
    GROUP BY o.order_date
)
-- Step 2: Select order_date, daily_revenue, and the running total using a window function
SELECT
    order_date,
    daily_revenue,
    -- TODO: compute running_total using a window function ordered by order_date
    SUM(daily_revenue) OVER(ORDER BY order_date) AS running_total
FROM daily_sales
ORDER BY order_date;
