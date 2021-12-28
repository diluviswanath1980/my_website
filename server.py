from flask import Flask,render_template,request,redirect,url_for
import csv

app = Flask(__name__)
print(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, DILU!</p>"

# @app.route('/blog')
# def blog():
# 	return "<p>Hey, I am Dilu</p>"

# @app.route('/blog/2020/dogs')
# def blog2():
# 	return "<p>This is blog2</p>"
#--------------------------------------------

# @app.route('/')
# def index():
# 	return render_template('index.html')

# @app.route('/index.html')
# def index1():
# 	return render_template('index.html')

# @app.route('/home.html')
# def about():
# 	return render_template('about.html')

# @app.route('/components.html')
# def components():
# 	return render_template('components.html')

# @app.route('/contact.html')
# def contact():
# 	return render_template('contact.html')
#--------------------------------------------

@app.route('/')
def home():
	return render_template('about.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt',mode='a') as database:
		name = data['name']
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{name},{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv',newline='',mode='a') as database2:
		name = data['name']
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name,email,subject,message])


@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
	if request.method == 'POST':
		try:
			name = request.form['name']
			# email = request.form['email']
			# subject = request.form['subject']
			# message = request.form['message']
			#print(email,subject,message)
			data = request.form.to_dict()
			# print(data)
			write_to_file(data)
			write_to_csv(data)
			return render_template('thankyou.html',name=name)
		except:
			return 'Did not save to Database'
	else:
		return '<p>Something went wrong.Please try again.</>'