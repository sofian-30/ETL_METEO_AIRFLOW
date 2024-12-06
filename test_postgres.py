import psycopg2

# Informations de connexion
HOST = "localhost"  # ou utilisez l'adresse IP si nécessaire
PORT = 5432
DATABASE = "airflow"  # Remplacez par votre POSTGRES_DB
USER = "airflow"           # Remplacez par votre POSTGRES_USER
PASSWORD = "airflow"   # Remplacez par votre POSTGRES_PASSWORD

try:
    # Connexion à la base PostgreSQL
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        database=DATABASE,
        user=USER,
        password=PASSWORD
    )
    print("Connexion réussie !")

    # Créez un curseur pour exécuter des commandes SQL
    cursor = conn.cursor()

    # Exemple : Vérifiez les tables existantes
    cursor.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public';")
    tables = cursor.fetchall()
    print("Tables dans la base de données :", tables)

    # Fermez la connexion
    cursor.close()
    conn.close()
    print("Connexion fermée.")
except Exception as e:
    print("Erreur lors de la connexion :", e)
