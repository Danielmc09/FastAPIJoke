# FastAPIJOKE

<p align="center">
  <img src ="https://res.cloudinary.com/practicaldev/image/fetch/s--PrsSS-li--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3bp4cdg6ocw9pyu3h522.jpg" />
</p>


This API was created to make different requests

- /jokes &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;                 : Returns a random joke
- /jokes?joke_type=chuck &#160; : Returns a joke from the API https://api.chucknorris.io
- /jokes?joke_type=dad &#160;&#160;&#160;&#160;   : Returns a joke from the API https://icanhazdadjoke.com/api
- /save_joke      &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;        : Save the text of the joke in the database
- /update_joke/{joke_id}    &#160;&#160;&#160;&#160;   : Update the joke text in the database based on the id
- /delete_joke/{joke_id}    &#160;&#160;&#160;&#160;&#160;   : Delete the joke text in the database based on id
- /lcm    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;   : Calculates the least common multiple of a list of numbers greater than 0
- /increment    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;   : Increases the entered number by 1

## Clone the repository

```bash
https://github.com/Danielmc09/FastAPIJoke.git
```
## Create virtual env and activate 

```bash
create:
  virtualenv name_env 
  
activate:
  On Unix or MacOS, using the bash shell: source venv/bin/activate
  On Windows using the Command Prompt: path\venv\Scripts\activate.bat
```
## Install libraries

```bash
pip install -r requirements.txt
```
## Based on the .env.example file create an .env file 
- Keep in mind that the database used in this project is PostgreSQL, so the reference in the .env file is to the connection to PostgreSQL
```bash
DATABASE_URL=postgresql://user:password@localhost/NombreDeTuDB
```

## Run proyect

```bash
uvicorn main:app --reload
```

## Create table
- Remember to create the database before running the created_db.py file keep in mind to create an .env file based on the .env.example file and modify it with your information
```bash
- python config/created_db.py
```


## Run Test

```bash
- pytest test/test_joke.py
```


## General notes 

- The technologies used in this project can be viewed in the requirements.txt file.
- The database used in this project is PostgreSQL
- version python 3.11.3
- version FastAPI 0.95.0



- Ports to use that should not be busy or with local services turned off:
  - FastAPI: 8000
  - PostgreSQL: 5432

| Path                                        | Verb   | Body params        |
|---------------------------------------------|--------|--------------------|
| Local                                       ||
| http://localhost:8000/jokes                 | GET    | joke_type=Optional |
| http://localhost:8000/save_joke             | POST   | joke=string        |
| http://localhost:8000/update_joke/{joke_id} | PUT    | joke_id=int        |
| http://localhost:8000/delete_joke/{joke_id} | DELETE | joke_id=int        |
| http://localhost:8000/lcm                   | POST   | numbers=ListNumber |
| http://localhost:8000/increment             | GET    | number=int         |
| http://localhost:8000/docs                  | GET    |                    |
| http://localhost:8000/redoc                 | GET    |                    |



Autor: <a href="https://www.linkedin.com/in/angeldanielmendieta/">Angel Daniel Menideta Castillo</a> © 2023