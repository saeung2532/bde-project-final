-- [{'txn_date': '2021-11-27'
-- , 'new_case': 6073
-- , 'total_case': 2100959
-- , 'new_case_excludeabroad': 6016
-- , 'total_case_excludeabroad': 2094122
-- , 'new_death': 32
-- , 'total_death': 20677
-- , 'new_recovered': 6538
-- , 'total_recovered': 2000721
-- , 'update_date': '2021-11-27 07:32:10'}]

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
