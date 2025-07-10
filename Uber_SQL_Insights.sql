-- Total Requests by Pickup Point and Status
SELECT pickup_point, status, COUNT(*) AS total_requests
FROM uber_requests
GROUP BY pickup_point, status
ORDER BY pickup_point, total_requests DESC;

-- Hourly Demand Trend
SELECT 
    HOUR(request_timestamp) AS hour_of_day,
    COUNT(*) AS total_requests
FROM uber_requests
GROUP BY hour_of_day
ORDER BY hour_of_day;

--  Requests with No Cars Available
SELECT COUNT(*) AS no_car_requests
FROM uber_requests 
WHERE status = 'No Cars Available';

-- Supply vs Demand Per Hour
SELECT 
    HOUR(request_timestamp) AS hour,
    COUNT(*) AS total_requests,
    SUM(CASE WHEN status = 'Trip Completed' THEN 1 ELSE 0 END) AS completed_trips,
    SUM(CASE WHEN status != 'Trip Completed' THEN 1 ELSE 0 END) AS unfulfilled_requests
FROM uber_requests 
GROUP BY hour
ORDER BY hour;

-- Driver-wise Trip Completion Count
SELECT driver_id, COUNT(*) AS completed_trips
FROM uber_requests 
WHERE status = 'Trip Completed'
GROUP BY driver_id
ORDER BY completed_trips DESC;

-- Cancellation Rates by Pickup Point
SELECT 
    pickup_point,
    COUNT(*) AS total_requests,
    SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled,
    ROUND(SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS cancel_rate_percent
FROM uber_requests
GROUP BY pickup_point;

-- Peak Hours for No Cars Available
SELECT 
    HOUR(request_timestamp) AS hour,
    COUNT(*) AS no_car_count
FROM uber_requests
WHERE status = 'No Cars Available'
GROUP BY hour
ORDER BY no_car_count DESC
LIMIT 5;
