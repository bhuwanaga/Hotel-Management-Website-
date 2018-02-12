#!/Python27/python
import MySQLdb
import cgi

print "Content-type: text/html"
print
print "<html><head><title>BDM Term Project</title>"
print ""
print "</head><body>"
print "<h1><font color='black'><marquee> Hotel Management System </marquee></h1>"
print "<h2><font color='black'>Reservation</h2>"
print "<style>"
print ".button {background-color: #4CAF50;border: none;color: white;padding: 15px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;margin: 4px 2px;cursor: pointer;}"
print "body {background: url('')"
print "no-repeat center center fixed;"
print "background-size: 1680px 640px;"
print "}</style>"
print ""

db = MySQLdb.connect(host="localhost",  # Hostname
                     user="fancy",  # Username
                     passwd="mysql",  # Password
                     db="hotel")  # Schema

print '<form method="post" action="bdm_project4.py">'
print "	Check - In:<br>"
print '	<input type="date" name="check_in" required>'
print "	<br>"
print "	Check - Out:<br>"
print '	<input type="date" name="check_out" required>'
print "	<br>"
print '	<p><input type="submit" class="button" value="Submit >>"></p>'
print "</form>"

form = cgi.FieldStorage()
check_in = form.getvalue("check_in")
check_out = form.getvalue("check_out")

cur = db.cursor()

query1 = "select ID_Proof from visitors order by entry_added desc limit 1;"
cur.execute(query1)
id_proof_list = cur.fetchall()
id_proof = id_proof_list[0][0]
#print id_proof

query2 = "select distinct e.event_id from visitors v, events e where v.ID_Proof = e.ID_Proof and e.ID_Proof = '" + str(id_proof) + "';"
cur.execute(query2)
event_id_list = cur.fetchall()
#print event_id_list

query3 = "select distinct r.room_id from visitors v, room r where v.ID_Proof = r.ID_Proof and r.ID_Proof = '" + str(id_proof) + "';"
cur.execute(query3)
room_id_list = cur.fetchall()
#print room_id_list

if not event_id_list:
    if not room_id_list:
        query = "insert into Reservation(Start_Date,End_Date)values('" + str(check_in) + "','" + str(check_out) + "');"
        #print query
        try:
            cur.execute(query)
            db.commit()
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            db.rollback()
            #print e
    else:
        for row in room_id_list:
            query = "insert into Reservation(Start_Date,End_Date,Room_ID)values('" + str(check_in) + "','" + str(check_out) + "','" + str(row[0]) + "');"
            #print query
            try:
                cur.execute(query)
                db.commit()
            except (MySQLdb.Error, MySQLdb.Warning) as e:
                db.rollback()
                #print e
else:
    event_id = event_id_list[0][0]
    if not room_id_list:
        query = "insert into Reservation(Start_Date,End_Date,Event_ID)values('" + str(check_in) + "','" + str(check_out) + "','" + str(event_id) + "');"
        #print query
        try:
            cur.execute(query)
            db.commit()
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            db.rollback()
            #print e
    else:
        for row in room_id_list:
            query = "insert into Reservation(Start_Date,End_Date,Room_ID,Event_ID)values('" + str(check_in) + "','" + str(check_out) + "','" + str(row[0]) + "','" + str(event_id) + "');"
            #print query
            try:
                cur.execute(query)
                db.commit()
            except (MySQLdb.Error, MySQLdb.Warning) as e:
                db.rollback()
                #print e
                
query3 = "select distinct r.room_id from visitors v, room r where v.ID_Proof = r.ID_Proof"
cur.execute(query3)
room_id_list = cur.fetchall()
#print room_id_list



if check_in <> None and check_out <> None:
    print '<meta http-equiv="refresh" content="0;url=http://localhost/bdm_project5.py" />'

print "</body></html>"
