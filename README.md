## Crear entorno virtual

python3 -m venv venv 

## Activar entorno

source venv/bin/activate

## instalar dependencias

pip install -r requirements.txt

## correr migraciones (NO EJECUTAR ESTO, solo si es nesesario, continuar con el siguente comando)

python3 manage.py makemigrations 

python3 manage.py migrate 

## levantar servidor

python3 manage.py runserver 


## endpoints

GET,PUT,POST,DELETE

http://localhost:8000/api/medicamentos/

GET,PUT,POST,DELETE

http://localhost:8000/api/tratamientos/

GET,PUT,POST,DELETE

http://localhost:8000/api/enfermedades/

GET

http://localhost:8000/api/q_1/

- No terminado

 http://localhost:8000/api/q_2/ 

- No terminado

 http://localhost:8000/api/q_3/

http://localhost:8000/api/q_4/


## DB

Archivo local con los datos, db.sqlite3