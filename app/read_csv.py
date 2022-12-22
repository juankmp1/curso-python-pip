import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        #print(header)
        
        data = []
        country= {}
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key:value for key, value in iterable}
            data.append(country_dict)
            
        return data
        


if __name__ == '__main__':
    country = read_csv('./world_population.csv')
    #print(data[0])
    countries = country[0]
    print(countries)
    #print(len(countries))
    #print(countries['Capital'])
    # valores = countries.values()
    # print(valores)
    """this is the title..."""
    i = 0
    final_values=[]
    for value in countries:        
        i += 1
        if i > 5 and i < 14:
            #print('esta es la i: ', i)
            final_values.append(value)

    print('this is final values',final_values)

    population = {year: population for year, population in countries.items if year is final_values}
    print(population)    

    # for value in countries:
    #     #if countries.values()    | == 'Afghanistan':
    #     print(value)

   
    