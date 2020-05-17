from flask import Flask, request 
import pandas as pd 
import sqlite3
app = Flask(__name__) 

def get_data():
    conn = sqlite3.connect('data/chinook.db')
    data = pd.read_sql_query("SELECT (c.firstname || ' ' || c.lastname) as FullName, \
i.BillingCountry as Country, i.InvoiceDate, g.Name as Genre, it.Quantity, round(i.Total,2) as Total \
FROM customers as c \
LEFT JOIN invoices as i ON i.customerid = c.customerid \
LEFT JOIN invoice_items as it ON it.invoiceid = i.invoiceid \
LEFT JOIN tracks as t ON t.trackid = it.trackid \
LEFT JOIN genres as g ON g.genreid = t.genreid", conn, parse_dates= 'InvoiceDate')
    data['Month'] = data['InvoiceDate'].dt.month_name()
    monthorder = ['January','February','March','April','May','June','July','August','September','October','November','December']
    data['Month'] = pd.Categorical(data['Month'],
                                         categories=monthorder,
                                         ordered=True)
    return data
# testing home page
@app.route('/', methods=['GET']) 
def get_text():
    return '''
<h1> Nothing to see here. Move along. Here are some url to follow:</h1>
<li> For all <a href="https://capstone-api-algoritma-kezia.herokuapp.com/cust">customers</a> sales data.</li>
<li> For country sales by <a href="https://capstone-api-algoritma-kezia.herokuapp.com/genre">genre</a>.</li>
<li> For monthly sales, here is an example for <a href="https://capstone-api-algoritma-kezia.herokuapp.com/get/sales/month/January">January</a>.</li>
<p> You can change the month name to get the appropriate monthly sales.</p>
    '''

# mendapatkan keseluruhan sales data dari customers
@app.route('/cust', methods=['GET']) 
def get_data_cust():
    data = get_data()
    return (data.to_json())

# mendapatkan keseluruhan sales data dari setiap country by genre
@app.route('/genre', methods=['GET']) 
def get_data_genre():
    data = get_data()
    genre_country = pd.pivot_table(data=data,index='Month',columns=['Country','Genre'],values='Total', aggfunc=sum)
    genre_country = genre_country.unstack(level=0).dropna()
    return (genre_country.to_json())

# mendapatkan data dengan filter kolom Genre
@app.route('/get/sales/month/<month_name>', methods=['GET']) 
def get_data_equal(month_name): 
    data = get_data()
    sales = pd.pivot_table(data=data,
                                   index='FullName',
                                   columns='Genre',
                                  values='Total',
                                  aggfunc=sum)
    sales = sales.reset_index().melt(id_vars = 'FullName')
    sales = sales[sales['value'].notna()]
    month = data['Month'] == month_name
    sales = sales[month]
    return (sales.to_json())

@app.route('/docs', methods=['GET'])
def documentation():
    return '''
<h1> Documentation </h1>
<h2> Welcoming page </h2>
<body> I have prepared a few url in the home page to direct users to some endpoints. </body>
<h2> Static Endpoints </h2>
<ol><li>
<p><b> /cust </b>, method = <b>GET</b> </p>
<p> This first static endpoint returns the detailed sales data of all customers, all countries, and all genres by month. Here you may find below information: </p>
<ul style="list-style-type:disc;">
<li> Customer Full Name </li>
<li> Country of Sales </li>
<li> Date of Invoice </li>
<li> Genre </li>
<li> Sales Quantity </li>
<li> Sales Amount </li>
<li> Month of Sales</li>
</ul></li></ol>
<ol start = "2"><li>
<p><b> /genre </b>, method = <b>GET</b> </p>
<p> This second static endpoint returns the sales data of each Genre by Country by Month, where you can find below information: </p>
<ul style="list-style-type:disc;">
<li> Country Name </li>
<li> Genre </li>
<li> Month of Sales </li>
<li> Sales amount </li>
</ul>
<p> Here I used: </p>
<ul>
<li> <i>pd.pivot_table</i> to do the aggregation</li>
<li> <i>unstack</i> to get the structure I want </li>
<li> <i>dropna</i> to exclude data with null values</li>
</ul></ol>
<h2> Dynamic Endpoints </h2>
<ol><li>
<p><b> /data/get/equal/data/&lt;month_name&gt;</b>, method = <b>GET</b></p>
<p> This endpoint returns the sales data by Customer and by Genre that happened in a specific month. Each month input will return different string. 
<br> The <i>month</i> value here is inputted to replace the <i>month_name</i> at the end of the link.</p>
<p>User should use the full month name to use this, for example: January, February and so on.</p>
</li></ol>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=5000) 