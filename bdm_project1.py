#!/Python27/python
import MySQLdb
import cgi

print "Content-type: text/html"
print
print "<html><head><title>BDM Term Project</title>"
print ""
print "</head><body>"
print "<h1><font color='black'><marquee> Hotel Management System </marquee></h1>"
print "<h2><font color='black'>Details of the Visit</h2>"
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

print '<form method="post" action="bdm_project1.py">'
print "	Purpose of Visit (Select only one):<br>"
print '	<input type="checkbox" name="visit_purpose" value="Private" checked>Private<br>'
print '	<input type="checkbox" name="visit_purpose" value="Corporate">Corporate<br>'
print '	<input type="checkbox" name="visit_purpose" value="Social">Social<br>'
print '	Number of People(between 2 and 100):<br>'
print ' <input type="number" name="number" min="2" max="150" required><br>'
print '	Name of the event/group:<br>'
print ' <input type="text" name="event_name" required><br>'
print "	Event Room:<br>"
print "<select name='event_room'>"
print '  <option name="event_room" value="None">None</option>'
print '  <option name="event_room" value="Banquet Hall">Banquet Hall</option>'
print '  <option name="event_room" value="Roof Top">Roof Top</option>'
print '  <option name="event_room" value="Board Room">Board Room</option>'
print '  <option name="event_room" value="Conference Room">Conference Room</option>'
print '  <option name="event_room" value="Auditorium">Auditorium</option>'
print '</select><br>'
print "	Do you need Room to Stay?<br>"
print '	<input type="radio" name="need_room" value="Yes"> Yes<br>'
print '    <input type="radio" name="need_room" value="No" checked> No<br>'
print '	<p><input type="submit" class="button" value="Submit >>"></p>'
print "</form>"
print "<h3><font color='black'>Event Room Prices</h3>"
print '''
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 50%;
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
<table>
  <tr>
    <th>Event Room</th>
    <th>Price</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><b>Board Room</b></td>
    <td>500$</td>
    <td>Holds maximum of 20 people. Food Services Included</td>
  </tr>
  <tr>
    <td><b>Conference Room</b></td>
    <td>1000$</td>
    <td>Holds maximum of 25 people. Food Services Included</td>
  </tr>
  <tr>
    <td><b>Auditorium</b></td>
    <td>1500$</td>
    <td>Holds maximum of 50 people. Food Services Included</td>
  </tr>
  <tr>
    <td><b>Roof Top</b></td>
    <td>2000$</td>
    <td>Holds maximum of 100 people. Food Services Included</td>
  </tr>
  <tr>
    <td><b>Banquet Hall</b></td>
    <td>2500$</td>
    <td>Holds maximum of 150 people. Food Services Included</td>
  </tr>
</table>'''

form = cgi.FieldStorage()
visit_pr = form.getvalue("visit_purpose")
quantity = form.getvalue("number")
need_room = form.getvalue("need_room")
event_name = form.getvalue("event_name")
event_room = form.getvalue("event_room")

#print visit_pr
#print quantity
#print event_room

cur = db.cursor()

query1 = "select ID_Proof from visitors order by entry_added desc limit 1;"
cur.execute(query1)
id_proof_list = cur.fetchall()
id_proof = id_proof_list[0][0]

#print id_proof

if event_room == "Board Room":
    event_desc = "Holds maximum of 20 people. Food Services Included"
    event_room_price = 500
elif event_room == "Conference Room":
    event_desc = "Holds maximum of 25 people. Food Services Included"
    event_room_price = 1000
elif event_room == "Auditorium":
    event_desc = "Holds maximum of 50 people. Food Services Included"
    event_room_price = 1500
elif event_room == "Roof Top":
    event_desc = "Holds maximum of 100 people. Food Services Included"
    event_room_price = 2000
elif event_room == "Banquet Hall":
    event_desc = "Holds maximum of 150 people. Food Services Included"
    event_room_price = 2500
elif event_room == "None":
    event_desc = "None"
    event_room_price = 0

#print event_desc
#print event_room_price

query = "insert into events(Event_grp_Name,Event_Description,Event_Type,Participants_Number,Event_Room,Event_Room_Price,Need_Room,ID_Proof)values('" + event_name + "','" + event_desc + "','" + visit_pr + "'," + str(quantity) + ",'" + event_room + "'," + str(event_room_price) + ",'" + need_room + "','" + id_proof + "');"
#print query

try:
    cur.execute(query)
    db.commit()
except (MySQLdb.Error, MySQLdb.Warning) as e:
    db.rollback()
    print e
    
query = "<p>" + query + "</p>"

#if visit_pr == "Private":
#    print '<meta http-equiv="refresh" content="0;url=http://localhost/bdm_project2.py" />'

if need_room == "Yes":
    print '<meta http-equiv="refresh" content="0;url=http://localhost/bdm_project3.py" />'

if need_room == "No":
    print '<meta http-equiv="refresh" content="0;url=http://localhost/bdm_project4.py" />'

visit_pr = "<p>" + visit_pr + "</p>"
quantity = "<p>" + quantity + "</p>"

#print query
#print visit_pr
#print quantity

print "</body></html>"  
