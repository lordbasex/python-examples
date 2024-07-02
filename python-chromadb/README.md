# ChromaDB Matrix Collection

Este proyecto utiliza ChromaDB para crear y gestionar una colección de documentos relacionados con la película "Matrix". También incluye un script para realizar búsquedas en esta colección.

## Requisitos

- Python 3.6 o superior
- pip

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    cd tu-repositorio
    ```

2. Crea un entorno virtual (opcional, pero recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Crear la Colección

Para crear la colección "matrix" y añadir documentos relacionados con la película, ejecuta el siguiente script:

    ```bash
    python3 intro.py
    ```

Este script hará lo siguiente:
- Iniciará el cliente de ChromaDB.
- Verificará si la colección "matrix" ya existe.
- Creará la colección si no existe.
- Añadirá documentos relacionados con la película "Matrix" a la colección.

## Realizar Búsquedas

Para realizar búsquedas en la colección "matrix", usa el siguiente script:

    ```bash
    python3 search.py "tu consulta de búsqueda"
    ```

Por ejemplo:

    ```bash
    python3 search.py "ciencia ficción distópica"
    ```

También puedes especificar el número de resultados a devolver:

    ```bash
    python3 search.py "ciencia ficción distópica" --n_results 3
    ```

## Dependencias

Las dependencias del proyecto están listadas en el archivo `requirements.txt` e incluyen:

- `chromadb`
- `sentence-transformers`

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para cualquier mejora o corrección.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.