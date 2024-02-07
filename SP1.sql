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
