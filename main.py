from pip._vendor.distlib.compat import raw_input

instances = []


def decor(cls):
    def wrap(*args, **kwargs):
        obj = cls(*args, **kwargs)
        instances.append(obj)
        return obj

    return wrap


@decor
class Animals:
    def __init__(self, genus_animal, class_animal, area):
        self.genus_animal = genus_animal
        self.class_animal = class_animal
        self.area = area

    def __repr__(self):
        return f'{self.genus_animal} - {self.class_animal} - {self.area}  '


lion = Animals('lion', 'predator', 12)
monkey = Animals('monkey', 'herbivorous', 2)
panther = Animals('panther', 'predator', 12)
lynx = Animals('lynx', 'predator', 10)
deer = Animals('deer', 'herbivorous', 9)
roe = Animals('roe', 'herbivorous', 5)
hare = Animals('hare', 'herbivorous', 1)
raccoon = Animals('raccoon', 'herbivorous', 1)
bear = Animals('bear', 'predator', 7)
crocodile = Animals('crocodile', 'predator', 8)
horse = Animals('horse', 'herbivorous', 12)
cheetah = Animals('cheetah', 'predator', 10)

# 3.4 кв км
max_area = 3400000
list_aviaries=[]

ans = True
while ans:
    print("""
    1. Check area and settle animals
    2. Add new animal to the aviary
    3. Show all aviary

    """)
    ans = raw_input("What would you like to do? ")
    if ans == "1":
        print("\n Enter list")
        greeting = input()
        list = greeting.replace(',', '').split()
        need_area = 0
        count_av=0

        for s in set(list):

            count_animal = {s: int(greeting.count(s))}
            # print(count_animal)
            for i in count_animal:
                for j in instances:
                    if j.genus_animal == i:
                        if (j.area * count_animal[i]) <= max_area:
                            # count_av=count_av+1

                            aviaries = {'num_aviaries': len(list_aviaries)+1, 'genus_animal': j.genus_animal,
                                    'class_animal': j.class_animal, 'square': (j.area * count_animal[i])}

                            list_aviaries.append(aviaries)

                            print(f'You have {count_animal[i]} {j.genus_animal} you need {(j.area * count_animal[i])} m2. '
                              f'They are {j.class_animal} ')
                            need_area = need_area + (j.area * count_animal[i])
                        else:
                            print(f"You need more area")
                            break

        print(f'You need {need_area} m2 for all aviaries. Its {count_av} aviaries')



    elif ans == "2":
        print("\n Enter the aviary number")
        for s in list_aviaries:
            print(s['num_aviaries'])
            print(s['genus_animal'])
            print('-------------')
        input_aviari=input()
        print("\n Enter the genus animal ")
        input_animal = input()
        is_error_area=1
        is_error_animal=1

        for s in list_aviaries:
            if int(s['num_aviaries']) == int(input_aviari):
                is_error_area = 0

                if s['genus_animal']==input_animal:
                    is_error_animal = 0

                    for i in instances:
                        if s['genus_animal']==i.genus_animal:
                            if s['square']+int(i.area) <= max_area:
                                s['square']=s['square']+int(i.area)
                                print(f' New square')
                                print( s['square'])
                                break
                            else:
                                'You dont have enough space'

        if is_error_area == 1:
            print(f'Number does not exist')

            print("Do you want create new aviari? Write Yes")
            answer = input()
            if answer =='Yes':
                print("\n Enter the genus animal")
                input_animal = input()
                for j in instances:
                    if j.genus_animal == input_animal:
                        aviaries = {'num_aviaries': len(list_aviaries)+1, 'genus_animal': j.genus_animal,
                                        'class_animal': j.class_animal, 'square': (j.area)}

                        list_aviaries.append(aviaries)

                        print(aviaries)

            elif ans != "Yes":
                print(f'Wrong answer')

        elif is_error_area == 0:
            if is_error_animal == 1:
                print(f'Animal can"t live hear')
    elif ans == "3":
        print(list_aviaries)

    elif ans != "":
        print("\n Not Valid Choice Try again")


# lion, monkey, crocodile, lion, lion, monkey
