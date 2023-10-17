# Pollution Under Control Renewal Remainder

The rapid urbanization and escalating vehicular population have significantly contributed to the deterioration of air quality, posing serious health and environmental concerns worldwide. To address this pressing issue, the project proposes an innovative solution, the "Pollution Under Control Renewal Reminder" (PUCRR), which aims to initiate the process of reminding renewal of pollution under control (PUC) certificates for vehicles besides allowing vehicle owners to download their PUC certificates, PUC centers to upload issued/renewed PUC certificates, RTO centers to have access for sending renewal remainders in one click and handle all administrative operations.

# Requirements
1 --> Python==3.11.3 <br>
2 --> mysql installer ( don't forget to create root user and password ) <br>
3 --> mysql workbench <br>

# follow these steps for viewing this project

step 1: clone this project  <br>
step 2: open terminal and set path to current project path where this project is stored locally on your machine.  <br>
step 3: run this command--> pip install -r requirements.txt  <br>
step 4: create database with name 'pucdb'  <br>
step 5: goto settings.py file in pollution_under_control/settings.py <br>
step 6: goto DATABASES variable and change values of key's 'USER' and 'PASSWORD' to your local mysql root name and password.  <br>
step 7: run command 'python manage.py migrate' <br>
step 8: run command 'python manage.py createsuperuser' <br>
step 9: you will be asked to enter username, email and password ( remember those, in future u will use them for login to admin dashboard and testing purposes wherever login form is rendered) <br>
step 10: run command 'python manage.py runserver' <br>


NOTE : even it is old tested project as you created new database there wont be any existing data so frst upload some sample files using superuser login credentials and explore other features. if you have any queries feel free to contact me. <br>

# Project has been fired up on local host and you are ready to use!!!!




