def load_data(df, file_path):
    """Chargement des données dans un fichier CSV."""
    df.to_csv(file_path, index=False)
    print(f"Données sauvegardées dans {file_path}")
