# JOVENES-STEM-WEBSITE
Este repositorio aloja:
1. Una API y un Panel de Administración para la gestión de contenido (/content)
2. El sitio web del proyecto jóvenes en stem, cliente de la API (/frontend)

El panel de administración permite gestionar el contenido de la API para el sitio web (frontend) del proyecto jóvenes en STEM.

## REALIZAR CAMBIOS
1. git clone [enlace]
2. Preparar su propia rama como entorno de trabajo local:
3. cd [repositorio]
4. git branch [rama-tarea-que-esten-trabajando]
5. git checkout [rama-tarea-que-esten-trabajando]

## EJECUTAR EL FRONTEND
1. colocarse en la carpeta /frontend
2. npm install --force
3. npm run dev
4. el sitio se ejecuta en: http://localhost:5173/

## EJECUTAR EL BACKEND 
1. entrar en la carpeta /jovenes-stem-website
2. si no se tienen las librerías: pip install -r requirements.txt
3. python manage.py createsuperuser
4. python manage.py runserver
5. para entrar a la API http://127.0.0.1:8000/content/api/
6. para entra al panel de gestión de contenido http://127.0.0.1:8000/admin

## REALIZAR UN PUSH
1. colocarse en la carpeta y rama adecuada
2. git add .
3. git commit -m "mensaje-corto-tarea-que-trabajé"
4. git push origin [rama-tarea-que-esten-trabajando]

## REALIZAR UN PULL REQUEST
1. realizar el pull request desde el repositorio de GitHub
2. una vez aprobado se mezclará su rama con la main
3. es importante mantener su rama propia actualizada
