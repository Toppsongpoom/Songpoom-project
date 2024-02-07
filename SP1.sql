-- dataset https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries
select
    work_year,
    job_title,
    salary_in_usd,
    company_location
from `raw_data.ds_salaries`
where  salary_in_usd >= 200000 
order by 
    company_location = "US"    
limit 30


select
 agent_name, 
 agent_code,
 working_area
from `raw_data.agents`
where working_area = (select cust_city from `raw_data.customers` where cust_name = 'Holmes' )


- - aggregate function
SELECT
COUNT(*) AS n_tracks,
ROUND (AVG(bytes), 2) AS avg_bytes,
SUM(bytes) AS sum_bytes,
MIN(bytes) AS min_bytes,
MAX(bytes) AS max_bytes
From tracks;
- - aggregate function
SELECT
count(*) As total_n,
count(company) as B2B,
Count(*) - count(company) as B2C
from customers;
- 
- - aggregate function
SELECT
country,
count(*) AS customers
from customers
GROUP by country
-- having filter group
HAVING (country like "B%" or country LIKE "C%") and customers >= 5;
- 
- - aggregate function
SELECT
country,
count(*) AS customers
from customers
GROUP by country
-- having filter group
HAVING customers >= 5
ORDER by customers desc;
- - aggregate function
SELECT
COUNT(*) AS n_tracks,
ROUND (AVG(bytes), 2) AS avg_bytes,
SUM(bytes) AS sum_bytes,
MIN(bytes) AS min_bytes,
MAX(bytes) AS max_bytes
From tracks;
- - aggregate function
SELECT
count(*) As total_n,
count(company) as B2B,
Count(*) - count(company) as B2C
from customers;
- 
- - aggregate function
SELECT
country,
count(*) AS customers
from customers
GROUP by country
-- having filter group
HAVING (country like "B%" or country LIKE "C%") and customers >= 5;
- 
- - aggregate function
SELECT
country,
count(*) AS customers
from customers
GROUP by country
-- having filter group
HAVING customers >= 5
ORDER by customers desc;
