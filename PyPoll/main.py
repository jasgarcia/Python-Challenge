#add dependencies
import os
import csv

#load files and creat output
csv_load = os.path.join("Resources", "election_data.csv")
outputText = os.path.join("ResultsPoll", "election.txt")

# Create empty lists
polls=[]
dict_polls={}
dict_summary={}

# Open file
with open(csv_load, newline='') as csvfile:
    
    poll = csv.reader(csvfile,delimiter=',')
  
    next(poll)
    textresults = open(outputText,"w")

    # print to text file
    textresults.write("Election Results")
    print("Election Results")
    # print text file
    textresults.write("\n-------------------------")
    print("-------------------------") 

    # Convert to list 
    for line in poll:
        polls.append(line)
    # print to text file
    textresults.write("\nTotal Votes: "+str(len(polls)))
    print("Total Votes: "+str(len(polls)))
    # print to text file
    textresults.write("\n-------------------------")
    print("-------------------------")

    # convert for candidate names
    for line in polls:
        name_key = line[2]
        if name_key not in dict_polls:
           # insert name_key for dic results
            dict_polls[name_key]=0
        # count the names for name results
        dict_polls[name_key]+=1
    
    # calculate 
    total_polls = len(polls)
    for name in dict_polls:
        dict_summary[name]=round((dict_polls[name]/total_polls)*100)
        # print to text file
        textresults.write("\n"+str(name)+": "+str(dict_summary[name])+"% "+"("+str(dict_polls[name])+")")
        # print to console
        print(str(name)+": "+str(dict_summary[name])+"% "+"("+str(dict_polls[name])+")")
        
    # create for the highest results
    highest= 0

    # determine the winner using for
    for name in dict_summary:
        if highest < dict_summary[name]:
            highest=dict_summary[name]
            winner = name
            
    # print to text file
    textresults.write("\n-------------------------")
    print("-------------------------")
    # print to text file
    textresults.write("\nWinner: "+winner)
    print("Winner: "+winner)
    #printto text file
    textresults.write("\n-------------------------")
    print("-------------------------")
    
# Close file
textresults.close()