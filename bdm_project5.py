#!/Python27/python
import MySQLdb
import cgi

print "Content-type: text/html"
print
print "<html><head><title>BDM Term Project</title>"
print ""
print "</head><body>"
print "<h1><font color='black'><marquee> Hotel Management System </marquee></h1>"
print '''
<!DOCTYPE html>
<html>
<body>'''

db = MySQLdb.connect(host="localhost",  # Hostname
                     user="******",  # Username
                     passwd="******",  # Password
                     db="******")  # Schema

print '''<form action="/Lab_02.py">
  <fieldset>
    <legend><h2>Invoice Details</h2></legend>'''

cur = db.cursor()

query1 = "select ID_Proof from visitors order by entry_added desc limit 1;"
cur.execute(query1)
id_proof_list = cur.fetchall()
id_proof = id_proof_list[0][0]

query0 = "select distinct name from visitors where id_proof = '" + id_proof + "';"
cur.execute(query0)
name_list = cur.fetchall()
name = name_list[0][0]
print "	Name: "
print name
print "	<br>"

query2 = "select sum(num_of_rooms) from room r where ID_Proof ='" + id_proof + "';"
cur.execute(query2)
tot_room_list = cur.fetchall()
tot_room = tot_room_list[0][0]
print "	Total Rooms Booked: "
print tot_room
print "	<br>"

query3 = "select sum(price*num_of_rooms)*(re.End_Date-re.Start_Date) from room r,reservation re where r.Room_ID = re.Room_ID and ID_Proof = '" + id_proof + "';"
cur.execute(query3)
price_room_list = cur.fetchall()
if not price_room_list:
    price_room = 0
elif price_room_list[0][0] is None:
    price_room = 0
else:
    price_room = price_room_list[0][0]
print "	Price for Rooms Booked: "
print price_room
print "	<br>"

query4 = "select distinct e.event_room_price*(re.End_Date-re.Start_Date) from events e,reservation re where e.event_id = re.Event_ID and e.ID_Proof = '" + id_proof + "';"
cur.execute(query4)
price_event_list = cur.fetchall()
if not price_event_list:
    price_event = 0
elif price_event_list[0][0] is None:
    price_event = 0
else:
    price_event = price_event_list[0][0]
print "	Price for Event Booked: "
print price_event
print "	<br>"

if tot_room >= 4 :
    discount = 20
else:
    discount = 0

print "	Discount: " + str(discount) + "%"
print "	<br>"

x = int(price_room)
y = int(price_event)
final_price = x + y
discount1 = (discount/100.0)
final_price = final_price * (1-discount1)
print "	Final Amount: "
print final_price
print "	<br>"

query5 = "select distinct re.start_date,re.end_date from reservation re,events e where e.event_id = re.event_id and e.ID_Proof = '"+ id_proof + "';"
cur.execute(query5)
event_date_list = cur.fetchall()
if not event_date_list:
    print "No Event Booked"
    print "<br>"
else:
    query9 = "select distinct re.r_id from reservation re,events e where e.event_id = re.event_id and e.ID_Proof = '"+ id_proof + "';"
    cur.execute(query9)
    rid_list = cur.fetchall()
    rid = rid_list[0][0]
    for start_date in event_date_list:
        print "Start_date for Event: " + str(start_date[0])
        print "<br>"
        print "End_date for Event: " + str(start_date[-1])
        print "<br>"

query6 = "select distinct re.start_date,re.end_date from reservation re,room r where r.Room_ID = re.Room_ID and ID_Proof = '" + id_proof + "';"
cur.execute(query6)
room_date_list = cur.fetchall()
if not room_date_list:
    print "No Rooms Booked"
    print "<br>"
else:
    query8 = "select distinct re.r_id from reservation re,room r where r.Room_ID = re.Room_ID and ID_Proof = '" + id_proof + "';"
    cur.execute(query8)
    rid_list = cur.fetchall()
    rid = rid_list[0][0]
    for start_date in room_date_list:
        print "Start_date for Rooms Booked: " + str(start_date[0])
        print "<br>"
        print "End_date for Rooms Booked: " + str(start_date[-1])
        print "<br>"
print "	Payment Method: Cash"
print "	<br>"    
print '''</fieldset>
</form>

</body>
</html>
'''

query7 = "insert into billing (discount,final_amount,room_amount,event_amount,billing_method,r_id) values (" + str(discount) + "," + str(final_price) + "," + str(price_room) + "," + str(price_event) + ",'Cash'," + str(rid) + ");"
try:
    cur.execute(query7)
    db.commit()
except (MySQLdb.Error, MySQLdb.Warning) as e:
    db.rollback()
    print e
