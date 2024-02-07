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
