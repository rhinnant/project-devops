#!/bin/bash

# --- Variables ---
DB_NAME="my_it_dashboard"
DB_USER="tele"
DB_PASSWORD="2wsx3edc@WSX#EDC"
PROJECT_DIR="$HOME/Backup/my_it_dashboard-main"  # Change this to your Django project path

# --- Update system and install PostgreSQL ---
echo "Updating system and installing PostgreSQL..."
sudo apt update
sudo apt install -y postgresql postgresql-contrib python3-psycopg2

# --- Start PostgreSQL service ---
echo "Starting PostgreSQL service..."
sudo systemctl start postgresql
sudo systemctl enable postgresql

# --- Create database and user ---
echo "Creating PostgreSQL database and user..."
sudo -i -u postgres psql <<EOF
CREATE DATABASE $DB_NAME;
CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
EOF

# --- Test PostgreSQL connection ---
echo "Testing PostgreSQL connection..."
PGPASSWORD=$DB_PASSWORD psql -h localhost -U $DB_USER -d $DB_NAME -c "\dt"

# --- Run Django migrations ---
echo "Applying Django migrations..."
cd $PROJECT_DIR || exit
python3 manage.py makemigrations
python3 manage.py migrate

echo "✅ PostgreSQL setup complete and Django migrations applied!"
echo "You can now run your server: python3 manage.py runserver"
