import csv

def copy_csv(input_file, output_file, city):
    with open(input_file, 'r') as infile:
        reader = csv.reader(infile)
        with open(output_file, 'w', newline="") as outfile:
          writer = csv.writer(outfile)
          for row in reader:
            if row[1] == city:
              writer.writerow(row)             

city = input("Enter city name: ")
copy_csv("./data/join.csv", "./data/filtered/" + city + ".csv", city)

