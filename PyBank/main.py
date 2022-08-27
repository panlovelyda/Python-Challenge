import os
import csv

os.chdir(os.path.dirname(__file__))
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

with open(budget_data_csv) as csv_file:

    csv_reader=csv.reader(csv_file, delimiter=',') 
    header=next(csv_reader) 

    months=[] 
    prolosses=[] 

    total=0
    a_change=0
    m_change=0
    m_count=0
    delta1=0
    delta2=0         
    delta_line1=0
    delta_line2=0
    loop1=0
    loop2=0

    for row in csv_reader:
        month=row[0]
        proloss=row[1] 
        months.append(month)
        prolosses.append(proloss)
    
    m_count = len(months)

for loop1 in range (m_count):
    total=total+int(prolosses[loop1]) 

for loop2 in range (m_count-1): 
    a_change=a_change+(float(prolosses[loop2+1])-float(prolosses[loop2])) 
    m_change=(float(prolosses[loop2+1])-float(prolosses[loop2])) 
    if m_change>delta1:
        delta1=m_change
        delta_line1=loop2
    else:
        delta1=delta1

    if m_change<delta2: 
        delta2=m_change
        delta_line2=loop2
    else:
        delta2=delta2

analysis=f'\
Financial Analysis\n\
----------------------------\n\
Total Months: {m_count}\n\
Total Amount: ${total}\n\
Average Change: ${round(a_change/(m_count-1),2)}\n\
Greatest Increase in Profits: {months[delta_line1+1]} (${int(delta1)})\n\
Greatest Decrease in Profits: {months[delta_line2+1]} (${int(delta2)})\n'

print(analysis) 

file1=open("analysis\Analysis.txt","w") 
file1.writelines(analysis) 
file1.close() 
