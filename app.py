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

#mendapatkan data dengan filter kolom Genre
@app.route('/data/get/equal/data/<month_name>', methods=['GET']) 
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
    <h2> Static Endpoints </h2>
    <ol><li>
    <p> / , method = GET </p>
    <p> Base Endpoint, returning welcoming string value. </p>
    </li></ol>
    <h2> Dynamic Endpoints </h2>
    <ol start = "2"><li>
    <p> /data/get/equal/data/&lt;data_name&&gt; , method = GET </p>
    <p> Return full data &lt;data_name&gt; in JSON format. Currently available data are: 
    </p>
    <ul style="list-style-type:disc;">
    <li> chinook.db </li>
    <li> pulsar_stars.csv </li>
    </ul></li>
    <li>
    <p> /data/get/equal/&lt;data_name&gt;/&lt;column&gt;/&lt;value&gt; , method = GET
    </p>
    <p> Return all &lt;data_name&gt; where the value of column &lt;column&gt; is equal to &lt;value&gt;
    </p></li></ol>
    '''


if __name__ == '__main__':
    app.run(debug=True, port=5000) 