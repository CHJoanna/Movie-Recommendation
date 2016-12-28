## parse Keyword_Themes
def load_data():
    """
    This method reads the dataset, and returns a list of rows.
    Each row is a list containing the values in each column.
    """
    import csv
    
    with open('Allmovie_Keyword_Genres.csv', 'rb') as f:
        f.seek(0)
        reader = csv.reader(f)
        return [l for l in reader]

data = load_data()

for row in data:
    row[2] = row[2].replace("[","")
    row[2] = row[2].replace("]","")
    themes = row[2].split(",")
    for theme in themes:
        row.append(theme)

with open('Allmovie_Keyword_Genres_Theme_mod.csv', 'w') as f:
    thedatawriter = csv.writer(f)
    for row in data:
        thedatawriter.writerow(row)