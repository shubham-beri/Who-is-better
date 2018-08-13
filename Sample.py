import requests

from bs4 import BeautifulSoup


import matplotlib.pyplot as plt
list_players = {"Virat Kohli" : 253802,"Rohit Sharma" : 34102, "Shikhar Dhawan" : 28235, "Suresh Raina":33335,"M.S. Dhoni":28081, "Yuvraj Singh":36084, "Sachin Tendulkar":35320,"Rahul Dravid":28114,"Virender Sehwag":35263,"Sourav Ganguly": 28779,"Manish Pandey":290630,"David Warner":219889,"Steve Smith":267192}
print("Batsmen you can choose from to compare:")
for i in list_players:
    print(i)
a = input("Enter the player's name: \n").strip()
b = input("Enter the second player name: \n").strip()
response = requests.get("http://stats.espncricinfo.com/ci/engine/player/{}.html?class=2;template=results;type=batting;view=cumulative".format(list_players[a]))
response1 = requests.get("http://stats.espncricinfo.com/ci/engine/player/{}.html?class=2;template=results;type=batting;view=cumulative".format(list_players[b]))
soup = BeautifulSoup(response.text,"html.parser")
#print(soup.title.text)
soup1 = BeautifulSoup(response1.text,"html.parser")

averages=[]
averages1=[]
tTags = soup.find_all('td')
tTags1 = soup1.find_all('td')

for i in range(25,len(tTags1),17):
    averages1.append(tTags1[i].text)

for i in range(25,len(tTags),17):
    averages.append(tTags[i].text)
#ab = "\nStatsguru includes the following current or recent One-Day Internationals:\n"
#if ab in runs:
#    runs.remove(ab)

#for tag in tTags:
#    print(tag.text)'
c = '\xa0'
be = "\n\n\n\n\n"

if c in averages:
    averages.remove(c)
elif be in averages:
    averages.remove(be)

if c in averages1:
    averages1.remove(c)
elif be in averages1:
    averages1.remove(be)


for i in range(len(averages)):

    if  averages[i] == '-' :

        averages[i] = averages[i+1]
    averages[i] = float(averages[i])


match_no = list(range(1,len(averages)+1))

for i in range(len(averages1)):

    if  averages1[i] == '-' :

        averages1[i] = averages1[i+1]
    averages1[i] = float(averages1[i])



match_no1 = list(range(1,len(averages1)+1))



import matplotlib.style as style


plt.plot(match_no,averages,'b',label=a,linewidth = 0.5)
plt.plot(match_no1,averages1,'g',label=b,linewidth = 0.5)

plt.title("{} Vs. {}".format(a,b))
plt.xlabel("Match No")
plt.ylabel("Average")

plt.legend()#REpresents which line specifies which branch
plt.grid(True, color="r")
plt.show()


"""

Records type batting analysis
[change type]

  

View innings by innings list
[change view]

  

Ordered by start date (ascending)

  

Return to query menuCleared query menu 
overall
2008-2018
208
200
35
9588
183
58.10
10405
92.14
35
46
12-16
"""
