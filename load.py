import psycopg2

def load_data_to_csv(df, file_path):
    """Chargement des données dans un fichier CSV."""
    df.to_csv(file_path, index=False)
    print(f"Données sauvegardées dans {file_path}")

def load_data_to_postgres(df, db_config):
    """Chargement des données dans une base PostgreSQL."""
    try:
        # Connexion à PostgreSQL
        conn = psycopg2.connect(
            dbname=db_config["dbname"],
            user=db_config["user"],
            password=db_config["password"],
            host=db_config["host"],
            port=db_config["port"],
        )
        cursor = conn.cursor()
        
        # Création de la table si elle n'existe pas
        create_table_query = """
        CREATE TABLE IF NOT EXISTS weather_data (
            date TIMESTAMP PRIMARY KEY,
            temperature FLOAT
        );
        """
        cursor.execute(create_table_query)
        conn.commit()
        
        # Insertion des données
        for _, row in df.iterrows():
            cursor.execute(
                """
                INSERT INTO weather_data (date, temperature)
                VALUES (%s, %s)
                ON CONFLICT (date) DO NOTHING;
                """,
                (row['date'], row['temperature'])
            )
        conn.commit()
        print("Données insérées dans PostgreSQL avec succès.")
    except Exception as e:
        print(f"Erreur lors du chargement dans PostgreSQL : {e}")
    finally:
        cursor.close()
        conn.close()
