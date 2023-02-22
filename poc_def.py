import requests
import csv


def download_table(table):
    response = requests.get(f"http://api.nbp.pl/api/exchangerates/tables/{table}")
    response_json = response.json()
    return response_json[0]


def create_rates_list(data):
    final_table = []
    for tbl in data:
        eff_date = tbl['effectiveDate']
        rts = tbl['rates']
        for val in rts:
            list_of_values = list(val.values())
            temp_list = []
            temp_list.append(eff_date)
            temp_list.extend(list_of_values)
            final_table.append(temp_list)
    return final_table


def get_headers():
    headers = []
    data = download_table('a')
    rates = data['rates']
    date_header = list(data.keys())[2]
    rate_headers = list(rates[0].keys())
    headers.append(date_header)
    headers.extend(rate_headers)
    return headers


def data_to_csv(table):
    file_written = 'poc01.csv'
    with open(file_written, 'w', newline='', encoding='UTF-8') as csvfile:
        csv.writer(csvfile).writerows(table)
    return csvfile


if __name__ == '__main__':
    responses = []
    for table_type in ('a', 'b'):
        responses.append(download_table(table_type))
    rates = create_rates_list(responses)
    headers = get_headers()
    rates.insert(0, headers)
    data_to_csv(rates)

