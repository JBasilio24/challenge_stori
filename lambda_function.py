from datetime import datetime
from utils.aws_utils import read_csv_from_s3, send_email
from utils.render_utils import create_table_html
from utils.data_processing import process_csv_data


def lambda_handler(event, context):
    # Obtener el año actual
    current_year = datetime.now().year

    # Nombre del archivo CSV a leer
    csv_file_name = "transactions.csv"
    
    # Lee el archivo CSV desde S3
    bucket_name = "techchallengejba"
    csv_content = read_csv_from_s3(bucket_name, csv_file_name)
    
    # Procesa los datos del CSV
    transactions, total_balance, average_credit_per_month, average_debit_per_month, transaction_count, months = process_csv_data(csv_content)
    
    # Lee el contenido de la plantilla HTML
    with open('template.html', 'r') as f:
        template = f.read()
    
    # Reemplaza las variables en la plantilla HTML con los valores correspondientes
    template = template.replace('{{total_balance}}', str(total_balance))
    template = template.replace('{{average_credit_per_month}}', create_table_html(average_credit_per_month))
    template = template.replace('{{average_debit_per_month}}', create_table_html(average_debit_per_month))
    template = template.replace('{{transaction_count}}', str(transaction_count))
    template = template.replace('{{current_year}}', str(current_year)) 

    # Envía el correo electrónico con la información resumida
    sender = "jonathanbasilio212@gmail.com"
    recipients = ["jonathanbasilio212@gmail.com"]  # Lista de destinatarios
    subject = 'Resumen de transacciones'
    
    send_email(sender, recipients, subject, template)
    
    # Devuelve una respuesta indicando que el correo electrónico se ha enviado correctamente
    return {
        'statusCode': 200,
        'body': months
    }
