-- Mendapatkan jumlah nilai pinalty
SELECT 
    customer_id, 
    sum(pinalty)
FROM 
    invoice 
GROUP BY 
    customer_id
HAVING 
    sum(pinalty) > 0;
