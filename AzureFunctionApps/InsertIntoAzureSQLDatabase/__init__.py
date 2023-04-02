import logging
import pyodbc
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    valueToLog = 'Azure function log 1'

    server = '<server_name>'
    database = '<database_name>'
    username = '<username>'
    password = '<password>'   
    driver= '{ODBC Driver 17 for SQL Server}'
    
    conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    cursor.execute(f"EXECUTE dbo.PopulateLogVariable @Variable = '{valueToLog}'")
    conn.commit()
    
    return func.HttpResponse(f"Variable {valueToLog} is logged.")