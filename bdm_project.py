#!/Python27/python
import MySQLdb
import cgi

print "Content-type: text/html"
print
print "<html><head><title>BDM Term Project</title>"
print ""
print "</head><body>"
print "<h1><font color='black'><marquee> Hotel Management System </marquee></h1>"
print "<h2><font color='black'>Add/Search Customer</h2>"
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

print '<form method="post" action="bdm_project.py">'
print "	Name:<br>"
print '	<input type="text" name="name" required>'
print "	<br>"
print "	Address:<br>"
print '	<input type="text" name="address" required>'
print "	<br>"
print "	E-mail:<br>"
print ' <input type="email" name="email" required>'
print "	<br>"
print "	Date of Birth:<br>"
print '	<input type="date" name="dob" required>'
print "	<br>"
print "	ID Proof:<br>"
print '	<input type="text" name="id_proof" required>'
print "	<br>"
print "	Gender:<br>"
print '	<input type="radio" name="gender" value="male" checked> Male<br>'
print ' <input type="radio" name="gender" value="female"> Female<br>'
print ' <input type="radio" name="gender" value="other"> Other<br>'
print "	Type of Visitor:<br>"
print "<select name='visitor_type'>"
print '  <option name="visitor_type" value="ind">Individual</option>'
print '  <option name="visitor_type" value="grp">Group</option>'
print '</select><br>'
print "	Search for Reservation:<br>"
print '	<input type="radio" name="search" value="Yes"> Yes<br>'
print ' <input type="radio" name="search" value="No" checked> No<br>'
print '	<p><input type="submit" class="button" value="Submit >>"></p>'
print "</form>"

form = cgi.FieldStorage()
name = form.getvalue("name")
addr = form.getvalue("address")
email = form.getvalue("email")
dob = form.getvalue("dob")
id_proof = form.getvalue("id_proof")
gender = form.getvalue("gender")
visit_type = form.getvalue("visitor_type")
Visitor_SubType = "P"
search = form.getvalue("search")

cur = db.cursor()

query = "insert into visitors values('" + id_proof + "','" + name + "','" + email + "','" + addr + "','" + dob + "','" + visit_type + "','" + Visitor_SubType + "','" + gender + "',now());"

try:
    cur.execute(query)
    db.commit()
except (MySQLdb.Error, MySQLdb.Warning) as e:
    db.rollback()
    print e

if visit_type == "grp":
    print '<meta http-equiv="refresh" content="0;url=http://localhost/bdm_project1.py" />'
if visit_type == "ind":
    print '<meta http-equiv="refresh" content="0;url=http://localhost/bdm_project3.py" />'
if search == "Yes":
    print '<meta http-equiv="refresh" content="0;url=http://localhost/bdm_project7.py" />'

print "</body></html>"
