from cs50 import SQL
import csv


def db_create(filename):
	db = SQL("sqlite:///data.db")

	with open(filename, "r") as file:
		reader = csv.DictReader(file)
		for row in reader:
			db.execute ("INSERT INTO udas_raw (resident, date, uda, status, type) VALUES(?, ?, ?, ?, ?)", row["Resident"], row["Date"], row["UDA"], row["Status"], row["Type"])

