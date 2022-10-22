l1=['banglore','hydrabad','chenai','delhi','mumbai','mysore','sycndrabad']
l2 =['ore','bad','nai']

new_list= []
for city in l1:
    # print(city)
    for key in l2:
        # print(key)
        if key in city:
            print(city)
            # pass
        