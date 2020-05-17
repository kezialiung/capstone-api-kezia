# capstone-api-kezia
## This file is a documentation done by Kezia Surani Liung for the Capstone Project

@app.route('/docs', methods=['GET'])
def documentation():
    return '''
    <h1> Documentation </h1>
    <h2> Static Endpoints </h2>
    <ol>
        <li>
            <p> / , method = GET </p>
            <p> Base Endpoint, returning welcoming string value. </p>
        </li>           
    </ol>
    <h2> Dynamic Endpoints </h2>
    <ol start = "2">
        <li>
            <p> /data/get/equal/data/&lt;data_name&&gt; , method = GET 
            </p>
            <p> Return full data &lt;data_name&gt; in JSON format. Currently available data are: 
            </p>
            <ul style="list-style-type:disc;">
                <li> chinook.db </li>
                <li> pulsar_stars.csv </li>
            </ul>
        </li>
        <li>
            <p> /data/get/equal/&lt;data_name&gt;/&lt;column&gt;/&lt;value&gt; , method = GET
            </p>
            <p> Return all &lt;data_name&gt; where the value of column &lt;column&gt; is equal to &lt;value&gt;
            </p>
        </li>
    </ol>
    '''