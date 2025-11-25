-- Set role and warehouse
USE ROLE ACCOUNTADMIN;
USE WAREHOUSE COMPUTE_WH;

-- Create and select database + schema
CREATE DATABASE IF NOT EXISTS food_delivery;
CREATE SCHEMA IF NOT EXISTS food_delivery.surge_demo;
USE DATABASE food_delivery;
USE SCHEMA surge_demo;
SHOW TABLES LIKE 'orders_snowpark';

SELECT *
FROM orders_snowpark
ORDER BY event_time DESC
LIMIT 20;
CREATE OR REPLACE VIEW surge_pricing AS
SELECT 
    location_id AS zone,
    COUNT(*) AS orders_last_window,
    AVG(order_value) AS avg_base_price,
    CASE 
        WHEN COUNT(*) >= 50 THEN 1.6
        WHEN COUNT(*) >= 30 THEN 1.3
        WHEN COUNT(*) >= 15 THEN 1.15
        ELSE 1.0
    END AS surge_multiplier,
    AVG(order_value) *
    CASE 
        WHEN COUNT(*) >= 50 THEN 1.6
        WHEN COUNT(*) >= 30 THEN 1.3
        WHEN COUNT(*) >= 15 THEN 1.15
        ELSE 1.0
    END AS surge_price
FROM orders_snowpark
WHERE event_time >= DATEADD(MINUTE, -30, CURRENT_TIMESTAMP())
GROUP BY location_id;

SELECT *
FROM surge_pricing
ORDER BY surge_multiplier DESC;

