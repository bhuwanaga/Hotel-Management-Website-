#!/Python27/python
import MySQLdb
import cgi

print "Content-type: text/html"
print
print "<html><head><title>BDM Term Project</title>"
print ""
print "</head><body>"
print "<h1><font color='black'><marquee> Hotel Management System </marquee></h1>"
print "<h2><font color='black'>Search Reservation</h2>"
print "<style>"
print ".button {background-color: #4CAF50;border: none;color: white;padding: 15px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;margin: 4px 2px;cursor: pointer;}"
print "body {background: url('')"
print "no-repeat center center fixed;"
print "background-size: 1680px 640px;"
print "}</style>"
print ""

db = MySQLdb.connect(host="localhost",  # Hostname
                     user="******",  # Username
                     passwd="******",  # Password
                     db="******")  # Schema

print '<form method="post" action="bdm_project7.py">'
print "	<br>"
print "	Please enter ID Proof for re-confirmation:<br>"
print '	<input type="text" name="id_proof" required>'
print "	<br>"
print '	<p><input type="submit" class="button" value="Search >>"></p>'
print "</form>"

form = cgi.FieldStorage()
id_proof = form.getvalue("id_proof")

print '''<form action="/Lab_02.py">
  <fieldset>
    <legend><h2>Invoice Details</h2></legend>'''

cur = db.cursor()

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
