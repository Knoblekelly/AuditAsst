# Audit Assistant
#### Video Demo:  <https://youtu.be/D32OG6HFsVY>
#### Description:
For my final project I created Audit Assistant. This program features an HTML webpage that allows the user to upload a .CSV file, processes the .CSV file into a SQL database, sorts and filters the SQL database, then produces a table through the webpage that highlights areas of concern.

I work at a skilled nursing facility and a large part of my job is running audits to ensure that all departments are completing various tasks on time. Therefore I decided to attempt to automate one of the audits I regularly run using Python scripts to read and sort the raw information produced by the Electronic Health Record program we use. The final product starts with a .CSV file and ends with an HTML page that visualizes the completion dates of the assessments. The .CSV file contains a list of completed assessments for residents at a skilled nursing facility. These assessments need to be completed every 90 days for each resident at the facility. The EHR program used at the facility I work at can produce a list of all assessments completed for residents in a given time-frame, but is not able to produce a list of overdue assessments in a reliable way. Audit Assistant can take take the list of assessments, sort them by completion date, and then return a new database of the most recent date of completion for each assessment for each resident. The webpage then returns this new database as a table wherein any completion date outside of the 90 day limit is highlighted.

Audit Assistant uses Python, SQL, Flask, HTML, CSS, and Javascript:

app.py – Contains python coding for accepting the .CSV file, executing the GET and POST requests from the webpage to navigate to the different pages, and managing the SQL queries to produce the final database.
script.py – Defines a function for inserting information from a .CSV file into a SQL database. Ideally more of the functions from app.py would have been in here, but I had issues calling the functions consistently so now this file only has the one function.
data.db – Contains two tables: udas_raw (where all of the data from the .CSV file is initially loaded) and udas_fin (where the final list of only the most recently completed assessments for each resident is stored).
requirements.txt – Only contains the call for flask.
Static Folder – Contains the CSS files. I had issues with calling the CSS file in my HTML pages (despite moving it up and down in my folders) so I wound up following a guide step-by-step that used this file structure.
Uploads Folder – Contains the uploaded .CSV file. In order to access the information with SQL, I had to allow the file to be uploaded to my project fully. I was hoping to be able to read the file into a SQL database without this requirement, but could not get it to work
Templates Folder – Contains all of my HTML files including a reusable layout.

At one point I hoped to have the program start with a PDF file and then convert it to .CSV before filling the tables. However, the programming requirements for that were beyond my skill. While I did temporarily try using a pre-built module for converting PDF to .CSV, the results were not reliable.
