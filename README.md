# capstone-api-kezia
### This file is a documentation done by Kezia Surani Liung for the Capstone Project - Kappa class. This project was deployed as of Monday, May 17th, 2020.
<h1> Documentation </h1>
<h2> Static Endpoints </h2>
<ol><li>
<p> /cust , method = GET </p>
<p> This endpoint returns the sales data of all customers by month. Within this, you can find: </p>
<ul style="list-style-type:disc;">
<li> Customer Full Name </li>
<li> Country of Sales </li>
<li> Date & Month of Sales </li>
<li> Genre Name </li>
<li> Quantity and Total amount of Sales </li>
</ul>
<ol start = "2"><li>
<p> /data/get/equal/data/&lt;data_name&&gt; , method = GET </p>
<p> Return full data &lt;data_name&gt; in JSON format. Currently available data are:</p>
<ul style="list-style-type:disc;">
</ul></li></ol>
<h2> Dynamic Endpoints </h2>
<ol><li>
<p> /data/get/equal/&lt;data_name&gt;/&lt;column&gt;/&lt;value&gt; , method = GET</p>
<p> Return all &lt;data_name&gt; where the value of column &lt;column&gt; is equal to &lt;value&gt;</p>
</li></ol>