"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []

f = open('sales-report.txt') # read sales-report file
for line in f:
    line = line.rstrip() # clear the right space for each line
    entries = line.split('|') # split line into list at |

    # the 1st element of the list is assigned to salesperson
    salesperson = entries[0] 
    
    # the 3rd element of the list is assigned to melons
    # change string to integer
    melons = int(entries[2]) 

    # check if salesperson has been added
    if salesperson in salespeople: 
        # get the index of the salesperson if they have been added
        position = salespeople.index(salesperson) 

        # at the same index location, add the number of the melons sold
        melons_sold[position] += melons

    # initially, add the salesperson and the melons they sold the 1st time
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)): # print the report
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')


# Improvements: construct a dictionary

# key is salesperson's name

# value is a tuple of total amount of order and melons number

# report_dict[key] = report_dict.get(key, 0) + value

# print items of the salesreport dictionary
