from flask import render_template, Flask, json, request
import os
import psycopg2

app = Flask(__name__)


def connect_to_db():
    '''conn = psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USERNAME"],
        password=os.environ["DB_PASSWORD"],
    )'''
    conn = psycopg2.connect(os.environ["DB_URL"])
    return conn


@app.route("/", methods=["GET", "POST"])
@app.route("/medlist", methods=["GET", "POST"])
def fetch_medicine():
    conn = connect_to_db()
    cur = conn.cursor()

    if request.method == "POST":
        new_data = request.form.to_dict()
        print(new_data)
        query = """
                INSERT INTO medicine (medicine_name, bag_name, description, expiry)
                VALUES (%(medicine_name)s, %(bag_name)s, %(description)s, to_date(%(expiry)s,'MM-YYYY'));
                """
        cur.execute(query, new_data)

    cur.execute(
        "select medicine_name,bag_name,description,to_char(expiry,'Mon YYYY') from medicine;"
    )
    med_data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", med_data=med_data)
