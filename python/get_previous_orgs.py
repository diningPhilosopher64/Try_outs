import requests
from bs4 import BeautifulSoup



def get_previous_years_orgs(previous_years):
    previous_years_sets = []
    for year in previous_years:
        content = requests.get(year)

        if content.status_code == 200:
            
            soup = BeautifulSoup(content.text, 'html.parser')
            targets = soup.findAll("h4", {"class":"organization-card__name"})

            orgs = []
            for target in targets:
                orgs.append(target.text)

            this_set = set(orgs)
            previous_years_sets.append(this_set)
            
            first_set = previous_years_sets[0]
            
            iterator= 1
            
            while iterator < len(previous_years_sets):
                first_set = first_set.intersection(previous_years_sets[iterator])
                iterator += 1
                
    return list(first_set)
            




def test():
    list1 = get_previous_years_orgs(["https://summerofcode.withgoogle.com/archive/2019/organizations"])
    list2 = get_previous_years_orgs(["https://summerofcode.withgoogle.com/archive/2018/organizations"])
    test1 = list(set(list1).intersection(set(list2)))
    test2 = get_previous_years_orgs(last_two_years)
    test1.sort()
    test2.sort()
    if test1 == test2:
        return True
    else:
        return False


if __name__ == '__main__':

    last_two_years = ["https://summerofcode.withgoogle.com/archive/2019/organizations",
                      "https://summerofcode.withgoogle.com/archive/2018/organizations"]

    last_three_years = ["https://summerofcode.withgoogle.com/archive/2019/organizations",
                      "https://summerofcode.withgoogle.com/archive/2018/organizations",
                       "https://summerofcode.withgoogle.com/archive/2017/organizations"]


    last_two_years_orgs = get_previous_years_orgs(last_two_years)

    for org in last_two_years_orgs:
        print(org)

    






