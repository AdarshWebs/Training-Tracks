# SQL Assignment – Track 1 Basics

## Overview
This assignment focuses on practicing fundamental SQL concepts used in data engineering such as filtering, aggregation, grouping, and ranking queries. The analysis is performed on a dataset containing startup funding in India.

## Dataset Columns

Sno  
Date  
StartupName  
IndustryVertical  
SubVertical  
CityLocation  
InvestorsName  
InvestmentType  
AmountInUSD  

## Questions Solved

1. Number of startups in Pune  
2. Pune startups with Seed / Angel funding  
3. Total funding raised by Pune startups  
4. Top 5 Industry Verticals in India  
5. Top investor by funding for each year  

## Bonus Questions

6. Top startup by funding in each city  
7. SubVertical with highest number of startups  
8. SubVertical with highest funding amount  

## SQL Concepts Used

SELECT  
WHERE  
GROUP BY  
ORDER BY  
SUM()  
COUNT()  
ROW_NUMBER()  

## How to Run

Run the SQL script using:

mysql -u root -p startup_db < sql_assignment.sql

## Author

Adarsh Opalkar