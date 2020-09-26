# This Python script connects to a PostgreSQL database and utilizes Pandas to obtain data and create a data frame
import psycopg2
import pandas as pd

# Establish a connection to the database by creating a cursor object
# Connect to the PostgreSQL database
host = "localhost" # either "localhost", a domain name, or an IP address.
port = "5432" # default postgres port
dbname = "moodle"
user = "postgres"
pw = "secrets"
conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=pw)
# Create a new cursor
cur = conn.cursor()

# A function that takes in a PostgreSQL query and outputs a pandas database 
def pull(sql_query, database = conn):
    table = pd.read_sql_query(sql_query, database)
    return table

# Utilize the create_pandas_table function to create a Pandas data frame
# Store the data as a variable

overall_grade = pull("select AVG(finalgrade) as overall_grade_of_learners from mdl_grade_grades")
print('Overall grade of learners ') 
print(overall_grade)
print('\n')

forum_posts = pull("select count(*) as number_of_forum_posts from mdl_forum_posts")
print('Number of forum posts')
print(forum_posts)

# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
cur.close()
conn.close()