<h1>Project: capstone-api-kezia</h1>
<body> This file is a documentation done by Kezia Surani Liung for the Capstone Project - Kappa class. This project was deployed as of Monday, May 17th, 2020. The read_sql_query is used to create a dataframe and extract the needed columns from chinook.db which will be used throughout this exercise.</body><br>
<h1> Documentation </h1>
<h2> Welcoming page </h2>
<body> I have prepared a few url in the home page to direct users to some endpoints </body>
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
<p> This endpoint returns the sales data by Customer and by Genre that happened in a specific month. Each month input will return different string. The <i>month</i> value here is inputted to replace the <i>month_name</i> at the end of the link.</p>
<p>User should use the full month name to use this, for example: January, February and so on.</p>
</li></ol>