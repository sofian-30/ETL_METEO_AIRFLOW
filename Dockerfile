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

# Commande par défaut pour Airflow
CMD ["airflow", "standalone"]
