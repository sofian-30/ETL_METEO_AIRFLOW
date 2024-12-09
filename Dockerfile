FROM python:3.10-slim

# Installer les dépendances nécessaires pour Airflow
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet
COPY . .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Initialiser la base de données Airflow
RUN airflow db init

# Commande pour créer un utilisateur administrateur dans Airflow
RUN airflow users create \
    --username admin \
    --password admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com

# Commande par défaut pour démarrer Airflow
CMD ["airflow", "standalone"]
