> ### Using Multiple DBs in Different apps
Additional Requirements:
* Router (for each database implement a router to route the queries respectively.)
[application]()


> ### Using Multiple DBs in same Django app
Additional Requirements:
* Declaring App label 
* Router (for each database implement a router to route the queries respectively.)
### Commands

<b><u>In the project</u> :</b>

* ``` python manage.py migrate ```
* ```python manage.py startapp Blue```
* comment the other model and respective model registration in admin.py
* ```python manage.py makemigrations```
* commit the first model into respective database here
* ```python manage.py migrate Blue 0001 --database=users_db```
* uncomment and make migrations to whole( here first,second )
* ```python manage.py makemigrations```
* fake the first model migration to second database by
* ```python manage.py migrate Blue 0001 --database=customer_db --fake```
* fake second migration (so to consider only first)
*  ```python manage.py migrate Blue 0002 --database=users_db --fake```
* now to make considering only second model by second database(here customer_db)
* ```python manage.py migrate Blue 0002 --database=customer_db```

* Yo done! check the databases..
[application]()