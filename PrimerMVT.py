#Desafío Entregable
#Mi Primer MVT
#Sabaidini Inés

#Detalle del paso a paso

#CONECTANDO A GIT Y CREANDO MI REPOSITORIO
#Abro una terminal de GitBash en la carpeta donde está ubicado mi proyecto
#git init
#git add PrimerMVT.py
#git commit -m 'Cree el repositorio y guardé mi documento'

#Subo mi repositorio a GitHub
#git remote add origin https://github.com/inesabaidini/PrimerMVT.git
#git branch -M main
#git push -u origin main

#ARRANCANDO CON DJANGO
#django-admin startproject primermvt
#cd primermvt
#python manage.py makemigrations
#python manage.py migrate
#python manage.py runserver

#VIEWS
#Agregi views.py dentro de la carpeta primermvt
#Para que me cargue todas las carpetas en github puse git add . y desp el commit y el push
#Voy a urls.py y agrego from primermvt.views import * para que me quede importadas todas mis views
#agrego la ruta de templates al DIRS

#MODELO
#Creo mi modelo o mi app: python manage.py startapp 'familiares'
#Voy a models.py dentro de familiares y creo mi class Familia
#from familiares.models import Familia agrego esto a mi views.py
#agrego en settings.py mi modulo familiares
#python manage.py check familiares
#python manage.py makemigrations
#python manage.py migrate


#SUBIR MIS FAMILIARES A SQLITE
#Puedo hacerlo a mano desde SQLite o hacerlo con código desde la terminal

