
importibm_db


dictionary={}
def printTableData(conn):sql="SELECT*FROM
userdetails"
out = ibm_db.exec_immediate(conn, sql)document=
ibm_db.fetch_assoc(out)whiledocument!=False:

dictionary.update({document['USERNAME']:document['PASSWORD']})document=
ibm_db.fetch_assoc(out)



definsertTableData(conn,rollno,username,email,password):


sql="INSERTINTO
userdetails(rollno,username,email,password) VALUES({},'{}','{}','{}')".format(rollno,username,email,password)
out =ibm_db.exec_immediate(conn,sql)
print('Numberofaffectedrows:',ibm_db.num_rows(out),"\n")



defupdateTableData(conn,rollno,username,email,password):
sql = "UPDATE userdetails SET(username,email,password)=('{}','{}','{}'
)WHERE
rollno={}".format(username,email,password
,rollno)
out = ibm_db.exec_immediate(conn,sql)
print('Numberofaffectedrows:',ibm_db.num_rows(out),"\n")


def

deleteTableData(conn,rollno):
sql = "DELETE FROM userdetails WHERErollno={}".format(rollno)
out = ibm_db.exec_immediate(conn, sql)print('Number
ofaffectedrows:',ibm_db.num_rows(out),"\n")


try:


conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31198;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=bjn03696;PWD=ef96tLJX2VjzaCPX;","","")


print("Dbconnected")


except:


print("Error")





from flask importFlask,render_template,request,url_for,sessionapp=Flask(name)
@app.route("/")


@app.route("/login",methods=['POST','GET'])deflogin():
if
request.method=="POST":
printTableData(conn)


username=request.form['username']password=request.form['password']try:

ifdictionary[username]==passwordandusernameindictionary:
return "Logged in successfully"except:
return"Invalid
username or password"return
render_template('loginpage.html')

@app.route("/register",methods=['POST','GET'])


defregister():
if request.method=="POST":rollno=
request.form['rollno']
username = request.form['username']email=
request.form['email']
password=request.form['password']


insertTableData(conn,rollno,username,email,password)return
render_template('loginpage.html')
returnrender_template('registerpage.html')






if
name=="main":


app.run(debug=True)qlate,request,url_for,sessionapp=Flask(name)@app.route("/&quo
t;)@app.route("/login",methods=['POST','GET'])deflogin():
ifrequest.method=="POST":
printTableData(conn)


username=request.form['username']password=request.form['password']try:

ifdictionary[username]==passwordandusernameindictionary:


return "Logged in successfully"except:
return"Invalid
usernameorpassword"
returnrender_template('log’)
