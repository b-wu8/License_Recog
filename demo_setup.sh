cd src/database
mysql -u root < setup.sql
cd ..
python3 LoadData.py
