def create_table_html(data):
    table_html = ""
    
    for key, value in data.items():
        table_html += "<tr>"
        table_html += f"<td>{key}</td>"
        table_html += f"<td>{value}</td>"
        table_html += "</tr>"
    
    return table_html