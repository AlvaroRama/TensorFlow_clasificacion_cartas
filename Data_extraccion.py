import requests
import os
from dotenv import load_dotenv
import warnings
import zipfile
warnings.filterwarnings('ignore')

# Cargar variables de entorno desde .env

load_dotenv()

# Gestión de rutas y directorios.

carpeta_dataset = os.path.join(os.getcwd(), "dataset")

os.makedirs(carpeta_dataset, exist_ok=True)

ruta_salida = os.path.join(carpeta_dataset, "dataset.zip")


# Módulo de descarga de archivos del repositorio de Kaggle.

url = 'https://www.kaggle.com/api/v1/datasets/download/gpiosenka/cards-image-datasetclassification'

api_key = os.getenv('KAGGLE_API_KEY')

headers = {'Authorization': f'Bearer {api_key}'}

response = requests.get(url, headers=headers, verify=False)

with open(ruta_salida, 'wb') as file:
    file.write(response.content)

print(f"Archivo guardado en: {ruta_salida}")


# Búsqueda y descompresión de archivos.

def extract_and_remove_zip(directory):
    """
    Busca archivos ZIP en el directorio especificado, extrae su contenido y luego elimina el archivo ZIP.

    Parámetros:
        directory (str): Ruta del directorio donde se buscarán los archivos ZIP.

    Retorna:
        None
    """
    for filename in os.listdir(directory):
        if filename.endswith('.zip'):
            zip_path = os.path.join(directory, filename)
            extract_path = directory

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)

            os.remove(zip_path)

            print(f"El archivo {zip_path} ha sido descomprimido y eliminado.")
            return

    print("No se encontró ningún archivo zip en el directorio.")


directory = 'dataset/'

extract_and_remove_zip(directory)