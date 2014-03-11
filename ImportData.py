# all the imports
import csv
import sqlite3


class ImportData:
    def __init__(self, f, schema, db):
        self.FILENAME = f
        self.SCHEMA = schema
        self.DATABASE = db

    def connect_db(self):
        self.conn = sqlite3.connect(self.DATABASE)
        return self.conn.cursor()

    def close_db(self):
        self.conn.close()

    def init_db(self):
        self.connect_db().executescript(self.SCHEMA);
        print 'Database Schema Created Successfully'

    def commit_db(self):
        self.conn.commit()


    def FetchRow(self):
        with open(self.FILENAME, 'rb') as f:
            reader = csv.reader(f)
            rowcount = 0
            for row in reader:
                if rowcount != 0:
                    self.WriteToDb(row)
                rowcount += 1
            self.close_db()
            print 'database updated successfully'


    def WriteToDb(self, row):
        id = row[0]
        email = row[1]
        name = row[2]
        address = row[3]
        contact_no = row[4]
        mobile_no = row[5]
        dob = row[6]
        experience_years = row[7]
        experience_months = row[8]
        title = row[9]
        current_location = row[10]
        preferred_location = row[11]
        current_employer = row[12]
        current_designation = row[13]
        salary = row[14]
        ug_course = row[15]
        pg_course = row[16]
        ppg_course = row[17]
        db = self.connect_db()
        db.execute('insert into resume (id,'
                   'email,'
                   'name,'
                   'address,'
                   'contact_number,'
                   'mobile_number,'
                   'dob,'
                   'experience_years,'
                   'experience_months,'
                   'title,'
                   'current_location,'
                   'preferred_location,'
                   'current_employer,'
                   'current_designation,'
                   'salary,'
                   'ug_course,'
                   'pg_course,'
                   'ppg_course) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                   [id,
                    email,
                    name,
                    address,
                    contact_no,
                    mobile_no,
                    dob,
                    experience_years,
                    experience_months,
                    title,
                    current_location,
                    preferred_location,
                    current_employer,
                    current_designation,
                    salary,
                    ug_course,
                    pg_course,
                    ppg_course])
        self.commit_db()
        print id, email, name, address, contact_no, mobile_no, dob, experience_years, experience_months, \
            current_location, preferred_location, current_employer, current_designation, salary, ug_course, pg_course, ppg_course


obj = ImportData('resumes .csv', 'schema.sql', 'flaskr.db')
#obj.init_db()
obj.FetchRow()
