# pythonpractice.py
import random



counties = ['arapahoe','denver','jefferson']

counties_tuple = ('arapahoe','denver','jefferson')

counties_dic = {'arapahoe': 422829,}

# voting_data = []

# voting_data.append({"county":'arapahoe', 'registered_voters':422829})
# voting_data.append({"county":'denver', 'registered_voters':463353})
# voting_data.append({"county":'jefferson', 'registered_voters':432438})


# voting_data.insert(2,{"county":'el paso', 'registered_voters':461149})
# voting_data.remove({"county":'arapahoe', 'registered_voters':422829})
# voting_data.append(voting_data.pop(0))
# voting_data.append({"county":'arapahoe', 'registered_voters':422829})




# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

# for k,v in counties_dict.items():
#     print(f'{k} county has {v} registered voters')

# for i in range(len(voting_data)):
#     print(f'{voting_data[i]["county"]} county has {voting_data[i]["registered_voters"]} registered voters')

def neighboring(txt):
    ordy = [ord(i) for i in txt.lower()]
    bias = 0
    for i in ordy[1:]:
        print(str(i) +" " + str(ordy[bias]))
        if abs(i - ordy[bias]) != 1:
            print(str(i) + " "+str(ordy[bias]))
            return False
        bias += 1
    return True

print(neighboring("abcdedcba"))