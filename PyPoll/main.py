import os
import csv

os.chdir(os.path.dirname(__file__))
election_data_csv = os.path.join('Resources', 'election_data.csv')

with open(election_data_csv) as csv_file:

    csv_reader=csv.reader(csv_file, delimiter=',') 
    header=next(csv_reader) 

    voterids=[] 
    countys=[] 
    candidates=[]
    candidatenames=[]
    totalpercandidates=[]
    electionresultcandidates=[]
    totalcandidatepercentage=[]
    
    t_count=0
    winnervotes=0
    loop1=0
    loop2=0
    loop3=0
    loop4=0

    for row in csv_reader:
        voterid=row[0]
        county=row[1] 
        candidate=row[2]
        voterids.append(voterid)
        countys.append(county)
        candidates.append(candidate)
    
    t_count = len(voterids)

candidatenames.append(candidates[0]) 

for loop1 in range (t_count-1):
    if candidates[loop1+1] != candidates[loop1] and candidates[loop1+1] not in candidatenames:
        candidatenames.append(candidates[loop1+1])

n=len(candidatenames)

for loop2 in range (n): 
    totalpercandidates.append(candidates.count(candidatenames[loop2]))  

loservotes=t_count

for loop3 in range(n): 
    totalcandidatepercentage.append(f'{round((totalpercandidates[loop3]/t_count*100), 3)}%') 
    if totalpercandidates[loop3]>winnervotes: 
        winner=candidatenames[loop3]
        winnervotes=totalpercandidates[loop3]

for loop4 in range(n):
    electionresultcandidates.append(f'{candidatenames[loop4]}: {totalcandidatepercentage[loop4]} ({totalpercandidates[loop4]})') 

resultlines='\n'.join(electionresultcandidates) 

analysis=f'\
Election Results\n\
----------------------------\n\
Total Votes: {t_count}\n\
----------------------------\n\
{resultlines}\n\
----------------------------\n\
Winner: {winner} \n\
----------------------------\n'

print(analysis) 

file1=open("analysis\Analysis.txt","w") 
file1.writelines(analysis) 
file1.close() 
