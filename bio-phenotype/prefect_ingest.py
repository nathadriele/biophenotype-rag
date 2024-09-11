from prefect import task, Flow
import pandas as pd
import psycopg2

def get_bio_db_connection():
    conn = psycopg2.connect(
        dbname='your_dbname',
        user='your_user',
        password='your_password',
        host='localhost',
        port='5432'
    )
    return conn

@task
def extract_data():
    conn = get_bio_db_connection()
    query = "SELECT question, response FROM conversation_history;"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

@task
def transform_data(df):
    df['question'] = df['question'].str.strip()
    df['response'] = df['response'].str.strip()
    return df

@task
def load_data(df):
    conn = psycopg2.connect(
        dbname='your_destination_dbname',
        user='your_destination_user',
        password='your_destination_password',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO your_destination_table (question, response) VALUES (%s, %s)",
            (row['question'], row['response'])
        )
    conn.commit()
    cursor.close()
    conn.close()

with Flow("Bio-Phenotype Data Ingestion Flow") as flow:
    df = extract_data()
    transformed_df = transform_data(df)
    load_data(transformed_df)

if __name__ == "__main__":
    flow.run()
