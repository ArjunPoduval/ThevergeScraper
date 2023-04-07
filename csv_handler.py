import csv
import datetime


def write_data_to_csv(data):
    header = ["id", "URL", "headline", "author", "date"]
    date_str = datetime.datetime.now().strftime("%d%m%Y")
    file_name = f"{date_str}_verge.csv"
    new_data = []
    for i, d in enumerate(data):
        d_new = list(d)
        d_new.insert(0, i)   
        new_data.append(d_new)

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(new_data)

if __name__ == '__main__':
    data = []

    # Create a CSV file and write the header and data

    write_data_to_csv(data)
    print("CSV file created successfully!")