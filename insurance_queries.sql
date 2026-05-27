create database insurance_project;
use insurance_project;
select * from insurance; 

select count(*) as total_customer from insurance

select avg(charges) as average_of_insurances from insurance;

select smoker , avg(charges) as average_smoker_insurance from insurance
group by smoker

select region , avg(charges) as average_region_insurance from insurance
group by region  

select * from insurance
where bmi > 30; 

select count(*) from insurance 
where smoker = "yes" and charges >= 30000; 

