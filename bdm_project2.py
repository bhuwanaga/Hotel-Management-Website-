#!/Python27/python
import MySQLdb
import cgi

print "Content-type: text/html"
print
print "<html><head><title>BDM Term Project</title>"
print ""
print "</head><body>"
print "<h1><font color='black'><marquee> Hotel Management System </marquee></h1>"
print "<h2><font color='black'>Add Other Customers</h2>"
print "<style>"
print ".button {background-color: #4CAF50;border: none;color: white;padding: 15px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;margin: 4px 2px;cursor: pointer;}"
print "body {background: url('')"
print "no-repeat center center fixed;"
print "background-size: 1680px 640px;"
print "}</style>"
print ""
print '<form method="post" action="bdm_project2.py">'

db = MySQLdb.connect(host="localhost",  # Hostname
                     user="******",  # Username
                     passwd="******",  # Password
                     db="******")  # Schema

cur = db.cursor()

query = "select quantity from numbers;"

try:
    cur.execute(query)
except (MySQLdb.Error, MySQLdb.Warning) as e:
    db.rollback()
    print e

rows = cur.fetchall()

quantity = rows[0][0]

for i in range(quantity-1):
        print "<h2><font color='black'>Customer "
        print str(i+1)
        print "</h2>"
        print "	Name:<br>"
        print '	<input type="text" name="Name" required>'
        print "	<br>"
        print "	Address:<br>"
        print '	<input type="text" name="Address" required>'
        print "	<br>"
        print "	E-mail:<br>"
        print '    <input type="email" name="email" required>'
        print "	<br>"
        print "	Date of Birth:<br>"
        print '	<input type="date" name="DOB" required>'
        print "	<br>"
        print "	ID Proof:<br>"
        print '	<input type="text" name="id_proof" required>'
        print "	<br>"
        print "	Gender:<br>"
        print "<select name='gender'>"
        print '  <option name="gender" value="M" checked>Male</option>'
        print '  <option name="gender" value="F">Female</option>'
        print '  <option name="gender" value="O">Other</option>'
        print '</select><br>'

print '	<p><input type="submit" class="button" value="Submit >>"></p>'
print "</form>"

form = cgi.FieldStorage()
name = form.getvalue("Name")

if len(name) == (quantity-1):
    print '<meta http-equiv="refresh" content="0;url=http://localhost/bdm_project3.py" />'

print "</body></html>"  
