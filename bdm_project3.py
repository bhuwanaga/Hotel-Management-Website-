#!/Python27/python
import MySQLdb
import cgi
import random

print "Content-type: text/html"
print
print "<html><head><title>BDM Term Project</title>"
print ""
print "</head><body>"
print "<h1><font color='black'><marquee> Hotel Management System </marquee></h1>"
print "<h2><font color='black'>Add Rooms</h2>"
print "<style>"
print ".button {background-color: #4CAF50;border: none;color: white;padding: 15px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;margin: 4px 2px;cursor: pointer;}"
print "body {background: url('')"
print "no-repeat center center fixed;"
print "background-size: 1680px 640px;"
print "tr:nth-child(even) {background-color: #dddddd;}"
print "tr:nth-child(odd) {background-color: #ADD8E6;}"
print "}</style>"
print ""

db = MySQLdb.connect(host="localhost",  # Hostname
                     user="******",  # Username
                     passwd="******",  # Password
                     db="******")  # Schema

print '<form method="post" action="bdm_project3.py">'
print "	Number of Single Occupancy + Queen Size: "
print "<select name='SOQ'>"
print '  <option name="SOQ" value="1">1</option>'
print '  <option name="SOQ" value="2">2</option>'
print '  <option name="SOQ" value="3">3</option>'
print '  <option name="SOQ" value="4">4</option>'
print '  <option name="SOQ" value="5">5</option>'
print '  <option name="SOQ" value="6">6</option>'
print '  <option name="SOQ" value="7">7</option>'
print '  <option name="SOQ" value="8">8</option>'
print '  <option name="SOQ" value="9">9</option>'
print '  <option name="SOQ" value="0">0</option>'
print '</select><br>'
print "	Number of Double Occupancy + Queen Size: "
print "<select name='DOQ'>"
print '  <option name="DOQ" value="0">0</option>'
print '  <option name="DOQ" value="1">1</option>'
print '  <option name="DOQ" value="2">2</option>'
print '  <option name="DOQ" value="3">3</option>'
print '  <option name="DOQ" value="4">4</option>'
print '  <option name="DOQ" value="5">5</option>'
print '  <option name="DOQ" value="6">6</option>'
print '  <option name="DOQ" value="7">7</option>'
print '  <option name="DOQ" value="8">8</option>'
print '  <option name="DOQ" value="9">9</option>'
print '</select><br>'
print "	Number of Single Occupancy + King Size: "
print "<select name='SOK'>"
print '  <option name="SOK" value="0">0</option>'
print '  <option name="SOK" value="1">1</option>'
print '  <option name="SOK" value="2">2</option>'
print '  <option name="SOK" value="3">3</option>'
print '  <option name="SOK" value="4">4</option>'
print '  <option name="SOK" value="5">5</option>'
print '  <option name="SOK" value="6">6</option>'
print '  <option name="SOK" value="7">7</option>'
print '  <option name="SOK" value="8">8</option>'
print '  <option name="SOK" value="9">9</option>'
print '</select><br>'
print "	Number of Double Occupancy + King Size: "
print "<select name='DOK'>"
print '  <option name="DOK" value="0">0</option>'
print '  <option name="DOK" value="1">1</option>'
print '  <option name="DOK" value="2">2</option>'
print '  <option name="DOK" value="3">3</option>'
print '  <option name="DOK" value="4">4</option>'
print '  <option name="DOK" value="5">5</option>'
print '  <option name="DOK" value="6">6</option>'
print '  <option name="DOK" value="7">7</option>'
print '  <option name="DOK" value="8">8</option>'
print '  <option name="DOK" value="9">9</option>'
print '</select><br>'
print '	<p><input type="submit" class="button" value="Submit >>"></p>'
print "</form>"
print "<h3><font color='black'>Room Prices</h3>"
print '''
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 30%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

th {background-color: #4682B4;}

tr:nth-child(even) {
    background-color: #dddddd;
}

tr:nth-child(odd) {
    background-color: #ADD8E6;
}

</style>
</head>
<body>

<table>
  <tr>
    <th>Room Type + Bed Size</th>
    <th>Price</th>
    <th>Floor</th>
  </tr>
  <tr>
    <td><b>Single Occupancy + Queen</b></td>
    <td>50$</td>
    <td>1</td>
  </tr>
  <tr>
    <td><b>Double Occupancy + Queen</b></td>
    <td>100$</td>
    <td>2</td>
  </tr>
  <tr>
    <td><b>Single Occupancy + King</b></td>
    <td>150$</td>
    <td>3</td>
  </tr>
  <tr>
    <td><b>Double Occupancy + King</b></td>
    <td>200$</td>
    <td>4</td>
  </tr>
</table>'''

form = cgi.FieldStorage()
SOQ = form.getvalue("SOQ")
DOQ = form.getvalue("DOQ")
SOK = form.getvalue("SOK")
DOK = form.getvalue("DOK")

cur = db.cursor()

query1 = "select ID_Proof from visitors order by entry_added desc limit 1;"
cur.execute(query1)
id_proof_list = cur.fetchall()
id_proof = id_proof_list[0][0]

if SOQ not in [None,'0']:
    for i in range(int(SOQ)):
        print "Its working"
        room_Type = "Single"
        floor = 1
        bed_size = "Queen"
        num_bed = 1
        price = 50
        room_num = random.randint(101,109)
        query = "insert into room (Room_Type,Floor,Bed_Size,Number_Of_Beds,Price,ID_Proof,num_of_rooms,room_num)values('" + room_Type + "'," + str(floor) + ",'" + bed_size + "'," + str(num_bed) + "," + str(price) + ",'" + str(id_proof)+ "'," + '1' + "," + str(room_num) + ");"
        print query
        try:
            cur.execute(query)
            db.commit()
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            db.rollback()
            print e
            
if DOQ not in [None,'0']:
    for i in range(int(DOQ)):
        room_Type = "Double"
        floor = 2
        bed_size = "Queen"
        num_bed = 2
        price = 100
        room_num = random.randint(201,209)
        query = "insert into room (Room_Type,Floor,Bed_Size,Number_Of_Beds,Price,ID_Proof,num_of_rooms,room_num)values('" + room_Type + "'," + str(floor) + ",'" + bed_size + "'," + str(num_bed) + "," + str(price) + ",'" + str(id_proof)+ "'," + '1' + "," + str(room_num) + ");"
        print query
        try:
            cur.execute(query)
            db.commit()
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            db.rollback()
            print e
if SOK not in [None,'0']:
    for i in range(int(SOK)):
        room_Type = "Single"
        floor = 3
        bed_size = "King"
        num_bed = 1
        price = 150
        room_num = random.randint(301,309)
        query = "insert into room (Room_Type,Floor,Bed_Size,Number_Of_Beds,Price,ID_Proof,num_of_rooms,room_num)values('" + room_Type + "'," + str(floor) + ",'" + bed_size + "'," + str(num_bed) + "," + str(price) + ",'" + str(id_proof)+ "'," + '1' + "," + str(room_num) + ");"
        print query
        try:
            cur.execute(query)
            db.commit()
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            db.rollback()
            print e
if DOK not in [None,'0']:
    for i in range(int(DOK)):
        room_Type = "Double"
        floor = 4
        bed_size = "King"
        num_bed = 2
        price = 200
        room_num = random.randint(401,409)
        query = "insert into room (Room_Type,Floor,Bed_Size,Number_Of_Beds,Price,ID_Proof,num_of_rooms,room_num)values('" + room_Type + "'," + str(floor) + ",'" + bed_size + "'," + str(num_bed) + "," + str(price) + ",'" + str(id_proof)+ "'," + '1' + "," + str(room_num) + ");"
        print query
        try:
            cur.execute(query)
            db.commit()
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            db.rollback()
            print e

if SOQ or DOQ or SOK or DOK not in [None,'0']:
    print '<meta http-equiv="refresh" content="0;url=http://localhost/bdm_project4.py" />'

print "</body></html>"  
