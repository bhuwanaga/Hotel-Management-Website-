#!/Python27/python
import MySQLdb

db = MySQLdb.connect(host="localhost",  # Hostname
                     user="******",  # Username
                     passwd="******",  # Password
                     db="******")  # Schema

cur = db.cursor();


cur.execute("insert into visitors values('daskjhdj537','daskjhdj','daskjhdj@gmail.com','daskjhdj382','2013-08-01','ind','D','M',now());")
cur.execute("insert into visitors values('aafksf123','aafksf','aafksf@gmail.com','aafksf995','2013-12-03','ind','D','M',now());")
cur.execute("insert into visitors values('hsfjahd123','hsfjahd','hsfjahd@gmail.com','hsfjahd308','2005-12-16','ind','D','M',now());")
cur.execute("insert into visitors values('asvhda123','asvhda','asvhda@gmail.com','asvhda291','2014-10-13','ind','D','M',now());")
cur.execute("insert into visitors values('hbsd123','hbsd','hbsd@gmail.com','hbsd449','1995-07-02','ind','D','M',now());")
cur.execute("insert into visitors values('jasbdmas123','jasbdmas','jasbdmas@gmail.com','jasbdmas766','2003-10-09','ind','D','M',now());")
cur.execute("insert into visitors values('hasbdnasnmd123','hasbdnasnmd','hasbdnasnmd@gmail.com','hasbdnasnmd528','2011-12-14','ind','D','M',now());")
cur.execute("insert into visitors values('bdsah123','bdsah','bdsah@gmail.com','bdsah855','2006-08-16','ind','D','M',now());")
cur.execute("insert into visitors values('husak123','husak','husak@gmail.com','husak460','2004-02-03','ind','D','M',now());")

cur.execute("insert into room values(100,'Single',1,'Queen',1,50,'daskjhdj963',1,108);")
cur.execute("insert into room values(101,'Single',1,'Queen',1,50,'aafksf123',1,104);")
cur.execute("insert into room values(102,'Single',1,'Queen',1,50,'hsfjahd123',1,101);")
cur.execute("insert into room values(103,'Single',1,'Queen',1,50,'asvhda123',1,105);")
cur.execute("insert into room values(104,'Single',1,'Queen',1,50,'hbsd123',1,104);")
cur.execute("insert into room values(105,'Single',1,'Queen',1,50,'jasbdmas123',1,102);")
cur.execute("insert into room values(106,'Single',1,'Queen',1,50,'hasbdnasnmd123',1,102);")
cur.execute("insert into room values(107,'Single',1,'Queen',1,50,'bdsah123',1,107);")
cur.execute("insert into room values(108,'Single',1,'Queen',1,50,'husak123',1,103);")

cur.execute("insert into events values(200,'Meeting','Holds maximum of 20 people. Food Services Included','Corporate',2,'Board Room','500','No','daskjhdj963');")
cur.execute("insert into events values(201,'Meeting','Holds maximum of 20 people. Food Services Included','Corporate',3,'Board Room','500','No','aafksf123');")
cur.execute("insert into events values(202,'Meeting','Holds maximum of 20 people. Food Services Included','Corporate',4,'Board Room','500','No','hsfjahd123');")
cur.execute("insert into events values(203,'Meeting','Holds maximum of 20 people. Food Services Included','Corporate',5,'Board Room','500','No','asvhda123');")
cur.execute("insert into events values(204,'Meeting','Holds maximum of 20 people. Food Services Included','Corporate',6,'Board Room','500','No','hbsd123');")
cur.execute("insert into events values(205,'Meeting','Holds maximum of 20 people. Food Services Included','Corporate',7,'Board Room','500','No','jasbdmas123');")
cur.execute("insert into events values(206,'Meeting','Holds maximum of 20 people. Food Services Included','Corporate',8,'Board Room','500','No','hasbdnasnmd123');")
cur.execute("insert into events values(207,'Meeting','Holds maximum of 20 people. Food Services Included','Corporate',9,'Board Room','500','No','bdsah123');")
cur.execute("insert into events values(208,'Meeting','Holds maximum of 20 people. Food Services Included','Corporate',10,'Board Room','500','No','husak123');")

cur.execute("insert into reservation values(2017-04-07,'2017-04-14',306,'104',);")
cur.execute("insert into reservation values(2017-10-10,'2017-10-17',302,'103',);")
cur.execute("insert into reservation values(2017-06-03,'2017-06-10',306,'103',);")
cur.execute("insert into reservation values(2017-01-11,'2017-01-18',303,'106',);")
cur.execute("insert into reservation values(2017-05-04,'2017-05-11',309,'101',);")
cur.execute("insert into reservation values(2017-10-05,'2017-10-12',306,'105',);")
cur.execute("insert into reservation values(2017-07-23,'2017-07-30',306,'103',);")
cur.execute("insert into reservation values(2017-04-19,'2017-04-26',307,'107',);")
cur.execute("insert into reservation values(2017-01-07,'2017-01-14',304,'103',);")

cur.execute("insert into billing values(0,4875,864,4011,403,'Cash',308);")
cur.execute("insert into billing values(0,4844,523,4321,403,'Cash',305);")
cur.execute("insert into billing values(0,5111,686,4425,404,'Cash',309);")
cur.execute("insert into billing values(0,4690,783,3907,401,'Cash',309);")
cur.execute("insert into billing values(0,2165,927,1238,409,'Cash',307);")
cur.execute("insert into billing values(0,2365,825,1540,407,'Cash',301);")
cur.execute("insert into billing values(0,4359,527,3832,402,'Cash',309);")
cur.execute("insert into billing values(0,4175,773,3402,401,'Cash',303);")
cur.execute("insert into billing values(0,5552,679,4873,403,'Cash',305);")

db.commit()
