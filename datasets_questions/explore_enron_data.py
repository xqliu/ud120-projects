#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# print int(enron_data['Prentice James'.upper()]['exercised_stock_options']) + int(enron_data['Prentice James'.upper()]['restricted_stock'])

# print enron_data['Colwell Wesley'.upper()]['from_this_person_to_poi']

print enron_data['FASTOW ANDREW S']['deferral_payments']

print enron_data['Fastow Andrew S'.upper()]['total_payments']
print enron_data['LAY KENNETH L'.upper()]['total_payments']
print enron_data['SKILLING JEFFREY K'.upper()]['total_payments']

# print enron_data['Kenneth Lay'.upper()]


print enron_data['SKILLING JEFFREY K']



count = 0
for d in enron_data:
    # print d
    # print enron_data[d]
    # print len(enron_data[d])
    #if 'Fastow'.upper() in d:
    #    print str(d), str(enron_data[d])

    #if 'Jeffrey'.upper() in d:
    #    print str(d), str(enron_data[d])

    if enron_data[d]['poi'] == 1:
        count = count + 1

print "Number of total data:", len(enron_data)
print "Number of POI: ", count

# print len(enron_data[0])

email_count = 0
salary_count = 0

# Calculate percentage of user without total payment 
with_tp, without_tp = 0, 0
for d in enron_data:
    if enron_data[d]['salary'] != 'NaN':
        salary_count = salary_count + 1
    if enron_data[d]['email_address'] != 'NaN':
        email_count = email_count + 1
    if enron_data[d]['total_payments'] != 'NaN':
        with_tp = with_tp + 1
    else:
        without_tp = without_tp + 1

print "People with total payment: ", with_tp
print "People without total payment: ", without_tp
print "Percentage of people without total payment: ",
print  str(100*(float(without_tp)/(with_tp+without_tp)))

# Calculate percentage of POI without total payment
with_tp, without_tp = 0, 0
for d in enron_data:
    if enron_data[d]['salary'] != 'NaN':
        salary_count = salary_count + 1
    if enron_data[d]['email_address'] != 'NaN':
        email_count = email_count + 1
    if enron_data[d]['total_payments'] != 'NaN' and enron_data[d]['poi'] is True:
        with_tp = with_tp + 1
    elif enron_data[d]['total_payments'] == 'NaN' and enron_data[d]['poi'] is True:
        without_tp = without_tp + 1

print "POI with total payment: ", with_tp
print "POI without total payment: ", without_tp
print "Percentage of POI without total payment: ",
print  str(100*(float(without_tp)/(with_tp+without_tp)))

print "People without email: ", email_count
print "People without salary: ", salary_count

