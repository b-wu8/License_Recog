cd src/database
mysql -u root -p < setup.sql
cd ..
python3 LoadData.py
