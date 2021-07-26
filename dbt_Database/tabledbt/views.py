from django.shortcuts import render
from django.http import HttpResponse
import snowflake.connector
import pandas as pd
#import json


# Create your views here.

def home(request):
    return render(request,'table_form.html')

def table_view(request):
    ctx = snowflake.connector.connect(
        user = 'DINESH2000',
        password = 'Dinesh@2000',
        account = 'di63379.us-east-2.aws',
        database = request.POST["db_name"],
        schema = request.POST["schema_name"]
    )
    cs = ctx.cursor()
    try:
        table_name = request.POST["table_name"]
        db_name = request.POST["db_name"]
        schema_name = request.POST["schema_name"]
        column_name = request.POST["column_name"]
        query_name = request.POST["query_name"]
        if column_name == "ALL":
            column_name = "*"
        QUERY = ""
        if query_name == "":
            QUERY ="SELECT "+ column_name +" FROM "+db_name+"."+schema_name+"."+table_name 
        else:
            QUERY = query_name
        cs.execute(QUERY)
        #cs.execute("SHOW SCHEMAS;")
        df = pd.DataFrame.from_records(iter(cs), columns = [x[0] for x in cs.description])
        #json_records = df.reset_index().to_json(orient = 'records')
        #data = []
        #data = json.loads(json_records)
        #context = {'d' : data}
        context = df.to_html()
        return render(request, 'table_form.html', {'context' : context})
        #return HttpResponse(context)
    finally:
        cs.close()
        ctx.close()
    return HTTPResponse("Failed")
    
