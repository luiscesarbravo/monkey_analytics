##### \# Monkey Analytics

##### 

##### Pipeline personal para migrar datos operativos desde Excel hacia un stack analítico reproducible.

##### 

##### \## Objetivo

##### Construir un pipeline \*\*Excel → Python (pandas) → PostgreSQL\*\* y, en una fase posterior, llevarlo a \*\*AWS\*\* (S3 + Glue/Athena).

##### 

##### \## Stack

##### \- Python (pandas)

##### \- SQLAlchemy + psycopg2

##### \- PostgreSQL

##### \- Git/GitHub

##### 

##### \## Estructura del repo

##### \- `data/`: datasets locales (raw/staging/processed). `data/raw` se ignora en Git.

##### \- `src/`: código del pipeline (etl/db/utils)

##### \- `notebooks/`: exploración y prototipos

##### \- `docs/`: notas técnicas y documentación

##### 

##### \## Estado actual

##### \- Repo inicial creado y sincronizado con GitHub

##### \- Entorno virtual fuera del repo (`venv\_monkey`)

##### \- Dependencias registradas en `requirements.txt`

##### \- Datos Excel disponibles localmente en `data/raw` (no versionados)

##### 

##### \## Próximos pasos

##### 1\. Leer `data/raw/BD\_MonkeyPapas.xlsx` con pandas y validar schema

##### 2\. Definir modelo relacional en PostgreSQL

##### 3\. Cargar a staging/processed y automatizar ETL

##### 4\. Extender a AWS (S3 + Glue/Athena)

