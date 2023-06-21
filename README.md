Autochek Data Engineering Challenge
This repository contains solutions to the Autochek Data Engineering Challenge, which involves generating a summarized table from multiple datasets and loading the data into a PostgreSQL database.

## Problem Statement One
The problem statement revolves around creating a summarized table from the following datasets:

Borrower_table: Contains information about borrowers (customer_id, state, city, zip code).
Loan_table: Contains information about loans (borrower_id, loan_id, date_of_release, term, interest rate, loan amount, downpayment, payment frequency, maturity date).
Payment_Schedule: Contains information about payment schedules (loan_id, schedule_id, expected payment date, expected payment amount).
Loan_payment: Contains information about loan payments (loan_id, payment_id, amount paid, date paid).
The goal is to generate a SQL query that retrieves desired columns from these tables, calculates PAR Days (the number of days the loan was not paid in full), and calculates the amount_at_risk for each missed payment.

Solution
The solution to the problem consists of the following components:

Extracting the data from Google Sheets: The data is provided in Google Sheets format. To extract the data, it needs to be downloaded and saved as CSV files.

Transforming the data: Once the data is extracted, it needs to be transformed to generate the desired summarized table. This transformation involves joining the relevant tables, calculating PAR Days, and aggregating the data.

Loading the data into a PostgreSQL database: After the transformation, the data is loaded into a PostgreSQL database using the psycopg2 library.

Querying the data: Once the data is loaded into the database, SQL queries can be executed to retrieve the desired summarized table.

The solution to the problem is implemented in a Jupyter Notebook (.ipynb file). The notebook includes step-by-step instructions, code snippets, and explanations for each part of the solution.

Usage
To use the solution, follow these steps:

Clone the repository: git clone https://github.com/your-username/autochek-data-engineering-challenge.git

Install the required dependencies: pip install -r requirements.txt

Extract the data: Follow the instructions provided in the Jupyter Notebook to extract the data from Google Sheets and save it as CSV files.

Transform and load the data: Execute the code snippets provided in the Jupyter Notebook to transform the data, create the PostgreSQL database, and load the data into the database.

Query the data: Use the SQL queries provided in the Jupyter Notebook to retrieve the desired summarized table from the database.

Please make sure you have a PostgreSQL database installed and running before executing the code snippets for loading the data. Also, ensure that you have the necessary permissions to create databases and tables.


Conclusion
This repository provides a solution to the Autochek Data Engineering Challenge, which involves extracting, transforming, and loading data from multiple datasets and generating a summarized table. By following the instructions in the Jupyter Notebook, users can replicate the solution and retrieve the desired results.

Please refer to the Jupyter Notebook for detailed instructions and code explanations.

## Problem Statement Two

This repository contains a script written in Python that retrieves exchange rate data from a specified source and saves it in a specific format. The script is designed to run on a scheduler to pull the data multiple times a day.

### Problem Statement
The goal of this project is to fetch exchange rate data for 7 countries from a specific website and save the data in a standardized format. The data should include the timestamp of when the record was pulled, the currency being converted from (always USD), the rate of 1 USD to the target currency, and the rate of 1 unit of the target currency to USD. The script should also be scheduled to run twice a day, at 1 AM and 11 PM, to ensure the data is up to date.

Solution
The solution to the problem involves the following steps:

Create a free account on XE: To access the exchange rate data, you need to create a free account on XE (https://www.xe.com).

Go through the documentation: Familiarize yourself with the documentation provided by XE to understand how to retrieve the exchange rate data using their API (https://xecdapi.xe.com/docs/v1/).

Write a script to pull the data: Use Python to write a script that fetches the exchange rate data from the specified website and saves it in the desired format. The script should include functionality to specify the target currencies and handle the authentication with the XE API.

Set up a scheduler: Use a scheduler (e.g., cron on Linux or Task Scheduler on Windows) to schedule the execution of the script. Configure the scheduler to run the script twice a day, at 1 AM and 11 PM, to ensure the data is pulled at the desired intervals.

Usage
To use this script and set up the scheduler, follow these steps:

Create a free account on XE: Visit https://www.xe.com and create a free account to obtain the necessary API credentials.

Install the required dependencies: Make sure you have Python installed on your system. Install the required Python packages by running the following command:

Copy code
pip install requests
Clone the repository: Clone this repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/your-username/exchange-rate-data-puller.git
Configure the script: Open the script file (e.g., exchange_rate_puller.py) and update the necessary variables, such as your XE API credentials and the target currencies.

Test the script: Run the script manually to ensure it successfully pulls the exchange rate data and saves it in the desired format.

Set up the scheduler: Use your preferred scheduler (e.g., cron on Linux, Task Scheduler on Windows) to schedule the execution of the script. Configure the scheduler to run the script twice a day, at 1 AM and 11 PM, by specifying the appropriate command to execute the Python script.

By following these steps, the exchange rate data will be pulled automatically according to the scheduled intervals and saved in the specified format.

Please note that the script and scheduler setup mentioned in this README assume the usage of only Python without using a specific framework like Airflow. The script is designed to handle the data retrieval and saving aspects efficiently, without the need for additional dependencies.

Conclusion
This repository provides a solution for pulling exchange rate data from a specified source and setting up a scheduler to automate the data retrieval process. By following the provided steps, anyone can set up the script, configure it with their XE API credentials, and schedule it to run at desired intervals.

