# License_Recog
Automatic License Plate Recognition in Python. The system features graphical approach to detect the location of the plate and machine learning to recognize each individual letter and number. There is also a SQL database come as standard built-in functionality. We have a basic UI implemented in python tkinter. We may change the UI to java later for better maintainability and functionality. The recognition uses a simple CNN that was trained to recognize all letters and digits. The accuracy is an impressive 98 percentage correct rate. However, given that the graphical approach is less reliable, the system combined does not give impressive consistency and accuracy as one of the part does. We will keep improving the detection algorithm. 

# Algorithms
The approach to detect the plate is rather graphical. We search within the photo for a rectangle that fits the aspect ratio of that of a license plate. This is a brute force process and gives relatively less reliable outcome. The algorithm we use to predict each one of the letters and numbers uses machine learning. We have a pre-trained model that recognizes all letters and numbers used in license plates. We dissect the license plate to several areas and recognize each letter and number one at a time. The model is trained from a simple CNN, which provides decent results given the size of the network. 

# Module/Package Required
MySQL 5.7 or above \
\
Python 3.6 \
tkinter \
PIL \
time \
sys \
subprocess \
concurrent \
mysql.connector \
skimage \
matplotlib \
numpy \
pickle

# To run the program

Clone the repository. Navigate to the root directory of the repository folder. Run demo_setup.sh in terminal. This will set up the MySQL database and run scripts to load in data. If it fails during running demo_setup.sh, please check your MySQL installation. 

Then run the run.sh to start the program.  
```
sh demo_setup.sh
sh run.sh
```

# Database Credentials
The credentials for database login. For demo purposes, there are these following users:
```
root      <your root user password>              Has full access to databases and users
Mark      MarkMark123!                           Has read-only access to database
admin     Admin123!                              Has full access to databases
```

# Database Access Issue
If the database connection fails, run mysql in terminal in root user and type in password.
```
sudo mysql -u root -p
```
```
USE mysql;
UPDATE user SET plugin='mysql_native_password' WHERE User='root';
```
This gives MySQL permission to run as base user. 

# Machine Learning Tutorial and References
https://github.com/L1aoXingyu/pytorch-beginner \
https://zhuanlan.zhihu.com/p/26854386
