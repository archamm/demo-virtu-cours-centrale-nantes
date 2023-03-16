# Image de base à utiliser (Python 3.9 Slim)
FROM python:3.9-slim

# Copie du fichier Python (container_info.py) du répertoire courant (hôte) vers le répertoire /app (conteneur)
COPY container_info.py /app/

ENV CONTAINER_ID CONTAINER_1

# Commande à exécuter lorsque le conteneur démarre
CMD ["python", "/app/container_info.py"]