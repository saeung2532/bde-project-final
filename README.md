# Wattana Saeung DTI1 63606011

#Airflow
username: admin
password: password 

#MySQL
username: admin
password: password 


#Query create table 
CREATE TABLE covidtoday (
	id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR (25) NOT NULL,
    txn_date DATE NOT NULL,
    new_case INT NOT NULL,
    total_case INT NOT NULL,
    new_case_exclude INT NOT NULL,
    total_case_exclude INT NOT NULL,
    new_death INT NOT NULL,
    total_death INT NOT NULL,
    new_recovered INT NOT NULL,
    total_recovered INT NOT NULL,
    update_date DATETIME NOT NULL
);