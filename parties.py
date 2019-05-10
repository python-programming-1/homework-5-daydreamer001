import csv
import pprint


def get_bar_party_data():
    """this function reads from a csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific location and the number of complaint calls
     it received in 2016"""

    bar_list = []
    with open('bar_locations.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            bar_dict = {'location_type': row[0],
                        'zip_code': row[1],
                        'city': row[2],
                        'borough': row[3],
                        'latitude': row[4],
                        'longitude': row[5],
                        'num_calls': row[6]}
            bar_list.append(bar_dict)
    return bar_list


def print_data(data):
    for entry in data:
        #print(entry)
        pprint.pprint(entry)


def get_most_noisy_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """
    noisiest_city_and_borough = {'city': None, 'borough': None, 'num_city_calls': None, 'num_borough_calls': None}

    # write code here to find the noisiest city and borough and their respective metrics
    #cities are: ASTORIA, BAYSIDE, BELLEROSE, BRONX, BROOKLYN, CAMBRIA HEIGHTS, COLLEGE POINT, CORONA, EAST ELMHURST, ELMHURST,
    #FAR ROCKAWAY, FLUSHING, FOREST HILLS, GLEN OAKS, HOLLIS, HOWARD BEACH, JACKSON HEIGHTS, JAMAICA, KEW GARDENS, LITTLE NECK,
    #LONG ISLAND CITY, MASPETH, NEW YORK, OZONE PARK, QUEENS VILLAGE, REGO PARK, RICHMOND HILL, RIDGEWOOD, ROCKAWAY PARK, ROSEDALE,
    #SAINT ALBANS, SOUTH OZONE PARK, SOUTH RICHMOND HILL, STATEN ISLAND, SUNNYSIDE, WHITESTONE, WOODHAVEN, WOODSIDE


    #boroughs are: BRONX, BROOKLYN, MANHATTAN, QUEENS, STATEN ISLAND, Unspecified

    astoria=0
    bayside=0
    bellerose=0
    bronxcity=0
    brooklyncity=0
    cambriaheights=0
    collegepoint=0
    corona=0
    eastelmhurst=0
    elmhurst=0
    farrockaway=0
    flushing=0
    foresthills=0
    glenoaks=0
    hollis=0
    howardbeach=0
    jacksonheights=0
    jamaica=0
    kewgardens=0
    littleneck=0
    longislandcity=0
    maspeth=0
    newyork=0
    ozonepark=0
    queensvillage=0
    regopark=0
    richmondhill=0
    ridgewood=0
    rockawaypark=0
    rosedale=0
    saintalbans=0
    southozonepark=0
    southrichmondhill=0
    statenislandcity=0
    sunnyside=0
    whitestone=0
    woodhaven=0
    woodside=0

    bronx=0
    brooklyn=0
    manhattan=0
    queens=0
    statenisland=0
    unspecified=0
    
    maxCityCalls=0
    maxBoroughCalls=0

    

    #set code to find the noisiest city and borough (not mutually exclusive)
    #loop through list of dictionaries, and make two summations of city calls and borough calls based on city and borough
    #once summations are done, find max num city calls and max num borough calls, then set it to the noisest_city_and_borough accordingly.
    
    
    #loop through list of dictionaries, creating summations based on every individual city and borough
    for dicts in data: #looping through every dictionary


        #------cities--------#
        if dicts["city"]=="ASTORIA":
            astoria+=int(dicts["num_calls"])
        
        if dicts["city"]=="BAYSIDE":
            bayside+=int(dicts["num_calls"])
                
        if dicts["city"]=="BELLEROSE":
            bellerose+=int(dicts["num_calls"])

        if dicts["city"]=="BRONX":
            bronxcity+=int(dicts["num_calls"])

        if dicts["city"]=="BROOKLYN":
            brooklyncity+=int(dicts["num_calls"])

        if dicts["city"]=="CAMBRIA HEIGHTS":
            cambriaheights+=int(dicts["num_calls"])

        if dicts["city"]=="COLLEGE POINT":
            collegepoint+=int(dicts["num_calls"])

        if dicts["city"]=="CORONA":
            corona+=int(dicts["num_calls"])

        if dicts["city"]=="EAST ELMHURST":
            eastelmhurst+=int(dicts["num_calls"])

        if dicts["city"]=="ELMHURST":
            elmhurst+=int(dicts["num_calls"])

        if dicts["city"]=="FAR ROCKAWAY":
            farrockaway+=int(dicts["num_calls"])

        if dicts["city"]=="FLUSHING":
            flushing+=int(dicts["num_calls"])

        if dicts["city"]=="FOREST HILLS":
            foresthills+=int(dicts["num_calls"])

        if dicts["city"]=="GLEN OAKS":
            glenoaks+=int(dicts["num_calls"])

        if dicts["city"]=="HOLLIS":
            hollis+=int(dicts["num_calls"])

        if dicts["city"]=="HOWARD BEACH":
            howardbeach+=int(dicts["num_calls"])

        if dicts["city"]=="JACKSON HEIGHTS":
            jacksonheights+=int(dicts["num_calls"])

        if dicts["city"]=="JAMAICA":
            jamaica+=int(dicts["num_calls"])

        if dicts["city"]=="KEW GARDENS":
            kewgardens+=int(dicts["num_calls"])

        if dicts["city"]=="LITTLE NECK":
            littleneck+=int(dicts["num_calls"])

        if dicts["city"]=="LONG ISLAND CITY":
            longislandcity+=int(dicts["num_calls"])

        if dicts["city"]=="MASPETH":
            maspeth+=int(dicts["num_calls"])

        if dicts["city"]=="NEW YORK":
            newyork+=int(dicts["num_calls"])

        if dicts["city"]=="OZONE PARK":
            ozonepark+=int(dicts["num_calls"])

        if dicts["city"]=="QUEENS VILLAGE":
            queensvillage+=int(dicts["num_calls"])

        if dicts["city"]=="REGO PARK":
            regopark+=int(dicts["num_calls"])

        if dicts["city"]=="RICHMOND HILL":
            richmondhill+=int(dicts["num_calls"])

        if dicts["city"]=="RIDGEWOOD":
            ridgewood+=int(dicts["num_calls"])

        if dicts["city"]=="ROCKAWAY PARK":
            rockawaypark+=int(dicts["num_calls"])

        if dicts["city"]=="ROSEDALE":
            rosedale+=int(dicts["num_calls"])

        if dicts["city"]=="SAINT ALBANS":
            saintalbans+=int(dicts["num_calls"])

        if dicts["city"]=="SOUTH OZONE PARK":
            southozonepark+=int(dicts["num_calls"])

        if dicts["city"]=="SOUTH RICHMOND HILL":
            southrichmondhill+=int(dicts["num_calls"])

        if dicts["city"]=="STATEN ISLAND":
            statenislandcity+=int(dicts["num_calls"])

        if dicts["city"]=="SUNNYSIDE":
            sunnyside+=int(dicts["num_calls"])

        if dicts["city"]=="WHITESTONE":
            whitestone+=int(dicts["num_calls"])

        if dicts["city"]=="WOODHAVEN":
            woodhaven+=int(dicts["num_calls"])

        if dicts["city"]=="WOODSIDE":
            woodside+=int(dicts["num_calls"])




#-------boroughs-----------#
        if dicts["borough"]=="BRONX":
            bronx+=int(dicts["num_calls"])

        if dicts["borough"]=="BROOKLYN":
            brooklyn+=int(dicts["num_calls"])

        if dicts["borough"]=="MANHATTAN":
            manhattan+=int(dicts["num_calls"])

        if dicts["borough"]=="QUEENS":
            queens+=int(dicts["num_calls"])

        if dicts["borough"]=="STATEN ISLAND":
            statenisland+=int(dicts["num_calls"])

        if dicts["borough"]=="Unspecified":
            unspecified+=int(dicts["num_calls"])



            
#individual city and borough call values have been populated
#set max city and borough calls
    maxCityCalls=max(astoria, bayside, bellerose, bronxcity, brooklyncity, cambriaheights, collegepoint, corona, eastelmhurst, elmhurst, farrockaway, flushing, foresthills, glenoaks, hollis, howardbeach, jacksonheights, jamaica, kewgardens, littleneck, longislandcity, maspeth, newyork, ozonepark, queensvillage, regopark, richmondhill, ridgewood, rockawaypark, rosedale, saintalbans, southozonepark, southrichmondhill, statenislandcity, sunnyside, whitestone, woodhaven, woodside) 
    maxBoroughCalls=max(bronx, brooklyn, manhattan, queens, statenisland, unspecified)

#return value (city name) based on key
    city=''
    borough=''
    
    if maxCityCalls==astoria:
        city="ASTORIA"

    if maxCityCalls==bayside:
        city="BAYSIDE"

    if maxCityCalls==bellerose:
        city="BELLEROSE"

    if maxCityCalls==bronxcity:
        city="BRONX"

    if maxCityCalls==brooklyncity:
        city="BROOKLYN"

    if maxCityCalls==cambriaheights:
        city="CAMBRIA HEIGHTS"

    if maxCityCalls==collegepoint:
        city="COLLEGE POINT"

    if maxCityCalls==corona:
        city="CORONA"
        
    if maxCityCalls==eastelmhurst:
        city="EAST ELMHURST"

    if maxCityCalls==elmhurst:
        city="ELMHURST"

    if maxCityCalls==farrockaway:
        city="FAR ROCKAWAY"

    if maxCityCalls==flushing:
        city="FLUSHING"

    if maxCityCalls==foresthills:
        city="FOREST HILLS"

    if maxCityCalls==glenoaks:
        city="GLEN OAKS"

    if maxCityCalls==hollis:
        city="HOLLIS"

    if maxCityCalls==howardbeach:
        city="HOWARD BEACH"

    if maxCityCalls==jacksonheights:
        city="JACKSON HEIGHTS"

    if maxCityCalls==jamaica:
        city="JAMAICA"

    if maxCityCalls==kewgardens:
        city="KEW GARDENS"

    if maxCityCalls==littleneck:
        city="LITTLE NECK"

    if maxCityCalls==longislandcity:
        city="LONG ISLAND CITY"

    if maxCityCalls==maspeth:
        city="MASPETH"

    if maxCityCalls==newyork:
        city="NEW YORK"

    if maxCityCalls==ozonepark:
        city="OZONE PARK"

    if maxCityCalls==queensvillage:
        city="QUEENS VILLAGE"

    if maxCityCalls==regopark:
        city="REGO PARK"

    if maxCityCalls==richmondhill:
        city="RICHMOND HILL"

    if maxCityCalls==ridgewood:
        city="RIDGEWOOD"

    if maxCityCalls==rockawaypark:
        city="ROCKAWAY PARK"

    if maxCityCalls==rosedale:
        city="ROSEDALE"

    if maxCityCalls==saintalbans:
        city="SAINT ALBANS"

    if maxCityCalls==southozonepark:
        city="SOUTH OZONE PARK"

    if maxCityCalls==southrichmondhill:
        city="SOUTH RICHMOND HILL"

    if maxCityCalls==statenislandcity:
        city="STATEN ISLAND"

    if maxCityCalls==sunnyside:
        city="SUNNYSIDE"

    if maxCityCalls==whitestone:
        city="WHITESTONE"

    if maxCityCalls==woodhaven:
        city="WOODHAVEN"

    if maxCityCalls==woodside:
        city="WOODSIDE"

    



#-----------------------------------------------------------#
    if maxBoroughCalls==bronx:
        borough="BRONX"

    if maxBoroughCalls==brooklyn:
        borough="BROOOKLYN"

    if maxBoroughCalls==manhattan:
        borough="MANHATTAN"

    if maxBoroughCalls==queens:
        borough="QUEENS"

    if maxBoroughCalls==statenisland:
        borough="STATEN ISLAND"

    if maxBoroughCalls==unspecified:
        borough="Unspecified"


    noisiest_city_and_borough = {'city': city, 'borough': borough, 'num_city_calls': maxCityCalls, 'num_borough_calls': maxBoroughCalls}
    return noisiest_city_and_borough


def get_quietest_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """

    quietest_city_and_borough = {'city': None, 'borough': None, 'num_city_calls': None, 'num_borough_calls': None}

    # write code here to find the quietest city and borough and their respective metrics
    
    #set code to find the quietest city and borough
    #loop through list of dictionaries, and make two summations of city calls and borough calls based on city and borough
    #once summations are done, find min num city calls and min num borough calls, then set it to the quietest_city_and_borough accordingly.





    #once quietest city and burough have been found, set the other dictionary elements with regards to the burough and city

    #cities are: ASTORIA, BAYSIDE, BELLEROSE, BRONX, BROOKLYN, CAMBRIA HEIGHTS, COLLEGE POINT, CORONA, EAST ELMHURST, ELMHURST,
    #FAR ROCKAWAY, FLUSHING, FOREST HILLS, GLEN OAKS, HOLLIS, HOWARD BEACH, JACKSON HEIGHTS, JAMAICA, KEW GARDENS, LITTLE NECK,
    #LONG ISLAND CITY, MASPETH, NEW YORK, OZONE PARK, QUEENS VILLAGE, REGO PARK, RICHMOND HILL, RIDGEWOOD, ROCKAWAY PARK, ROSEDALE,
    #SAINT ALBANS, SOUTH OZONE PARK, SOUTH RICHMOND HILL, STATEN ISLAND, SUNNYSIDE, WHITESTONE, WOODHAVEN, WOODSIDE


    #boroughs are: BRONX, BROOKLYN, MANHATTAN, QUEENS, STATEN ISLAND, Unspecified

    astoria=0
    bayside=0
    bellerose=0
    bronxcity=0
    brooklyncity=0
    cambriaheights=0
    collegepoint=0
    corona=0
    eastelmhurst=0
    elmhurst=0
    farrockaway=0
    flushing=0
    foresthills=0
    glenoaks=0
    hollis=0
    howardbeach=0
    jacksonheights=0
    jamaica=0
    kewgardens=0
    littleneck=0
    longislandcity=0
    maspeth=0
    newyork=0
    ozonepark=0
    queensvillage=0
    regopark=0
    richmondhill=0
    ridgewood=0
    rockawaypark=0
    rosedale=0
    saintalbans=0
    southozonepark=0
    southrichmondhill=0
    statenislandcity=0
    sunnyside=0
    whitestone=0
    woodhaven=0
    woodside=0

    bronx=0
    brooklyn=0
    manhattan=0
    queens=0
    statenisland=0
    unspecified=0
    
    minCityCalls=0
    minBoroughCalls=0

    

    #set code to find the noisiest city and borough (not mutually exclusive)
    #loop through list of dictionaries, and make two summations of city calls and borough calls based on city and borough
    #once summations are done, find max num city calls and max num borough calls, then set it to the noisest_city_and_borough accordingly.
    
    
    #loop through list of dictionaries, creating summations based on every individual city and borough
    for dicts in data: #looping through every dictionary


        #------cities--------#
        if dicts["city"]=="ASTORIA":
            astoria+=int(dicts["num_calls"])
        
        if dicts["city"]=="BAYSIDE":
            bayside+=int(dicts["num_calls"])
                
        if dicts["city"]=="BELLEROSE":
            bellerose+=int(dicts["num_calls"])

        if dicts["city"]=="BRONX":
            bronxcity+=int(dicts["num_calls"])

        if dicts["city"]=="BROOKLYN":
            brooklyncity+=int(dicts["num_calls"])

        if dicts["city"]=="CAMBRIA HEIGHTS":
            cambriaheights+=int(dicts["num_calls"])

        if dicts["city"]=="COLLEGE POINT":
            collegepoint+=int(dicts["num_calls"])

        if dicts["city"]=="CORONA":
            corona+=int(dicts["num_calls"])

        if dicts["city"]=="EAST ELMHURST":
            eastelmhurst+=int(dicts["num_calls"])

        if dicts["city"]=="ELMHURST":
            elmhurst+=int(dicts["num_calls"])

        if dicts["city"]=="FAR ROCKAWAY":
            farrockaway+=int(dicts["num_calls"])

        if dicts["city"]=="FLUSHING":
            flushing+=int(dicts["num_calls"])

        if dicts["city"]=="FOREST HILLS":
            foresthills+=int(dicts["num_calls"])

        if dicts["city"]=="GLEN OAKS":
            glenoaks+=int(dicts["num_calls"])

        if dicts["city"]=="HOLLIS":
            hollis+=int(dicts["num_calls"])

        if dicts["city"]=="HOWARD BEACH":
            howardbeach+=int(dicts["num_calls"])

        if dicts["city"]=="JACKSON HEIGHTS":
            jacksonheights+=int(dicts["num_calls"])

        if dicts["city"]=="JAMAICA":
            jamaica+=int(dicts["num_calls"])

        if dicts["city"]=="KEW GARDENS":
            kewgardens+=int(dicts["num_calls"])

        if dicts["city"]=="LITTLE NECK":
            littleneck+=int(dicts["num_calls"])

        if dicts["city"]=="LONG ISLAND CITY":
            longislandcity+=int(dicts["num_calls"])

        if dicts["city"]=="MASPETH":
            maspeth+=int(dicts["num_calls"])

        if dicts["city"]=="NEW YORK":
            newyork+=int(dicts["num_calls"])

        if dicts["city"]=="OZONE PARK":
            ozonepark+=int(dicts["num_calls"])

        if dicts["city"]=="QUEENS VILLAGE":
            queensvillage+=int(dicts["num_calls"])

        if dicts["city"]=="REGO PARK":
            regopark+=int(dicts["num_calls"])

        if dicts["city"]=="RICHMOND HILL":
            richmondhill+=int(dicts["num_calls"])

        if dicts["city"]=="RIDGEWOOD":
            ridgewood+=int(dicts["num_calls"])

        if dicts["city"]=="ROCKAWAY PARK":
            rockawaypark+=int(dicts["num_calls"])

        if dicts["city"]=="ROSEDALE":
            rosedale+=int(dicts["num_calls"])

        if dicts["city"]=="SAINT ALBANS":
            saintalbans+=int(dicts["num_calls"])

        if dicts["city"]=="SOUTH OZONE PARK":
            southozonepark+=int(dicts["num_calls"])

        if dicts["city"]=="SOUTH RICHMOND HILL":
            southrichmondhill+=int(dicts["num_calls"])

        if dicts["city"]=="STATEN ISLAND":
            statenislandcity+=int(dicts["num_calls"])

        if dicts["city"]=="SUNNYSIDE":
            sunnyside+=int(dicts["num_calls"])

        if dicts["city"]=="WHITESTONE":
            whitestone+=int(dicts["num_calls"])

        if dicts["city"]=="WOODHAVEN":
            woodhaven+=int(dicts["num_calls"])

        if dicts["city"]=="WOODSIDE":
            woodside+=int(dicts["num_calls"])




#-------boroughs-----------#
        if dicts["borough"]=="BRONX":
            bronx+=int(dicts["num_calls"])

        if dicts["borough"]=="BROOKLYN":
            brooklyn+=int(dicts["num_calls"])

        if dicts["borough"]=="MANHATTAN":
            manhattan+=int(dicts["num_calls"])

        if dicts["borough"]=="QUEENS":
            queens+=int(dicts["num_calls"])

        if dicts["borough"]=="STATEN ISLAND":
            statenisland+=int(dicts["num_calls"])

        if dicts["borough"]=="Unspecified":
            unspecified+=int(dicts["num_calls"])



            
#individual city and borough call values have been populated
#set max city and borough calls
    minCityCalls=min(astoria, bayside, bellerose, bronxcity, brooklyncity, cambriaheights, collegepoint, corona, eastelmhurst, elmhurst, farrockaway, flushing, foresthills, glenoaks, hollis, howardbeach, jacksonheights, jamaica, kewgardens, littleneck, longislandcity, maspeth, newyork, ozonepark, queensvillage, regopark, richmondhill, ridgewood, rockawaypark, rosedale, saintalbans, southozonepark, southrichmondhill, statenislandcity, sunnyside, whitestone, woodhaven, woodside) 
    minBoroughCalls=min(bronx, brooklyn, manhattan, queens, statenisland, unspecified)

#return value (city name) based on key
    city=''
    borough=''
    
    if minCityCalls==astoria:
        city="ASTORIA"

    if minCityCalls==bayside:
        city="BAYSIDE"

    if minCityCalls==bellerose:
        city="BELLEROSE"

    if minCityCalls==bronxcity:
        city="BRONX"

    if minCityCalls==brooklyncity:
        city="BROOKLYN"

    if minCityCalls==cambriaheights:
        city="CAMBRIA HEIGHTS"

    if minCityCalls==collegepoint:
        city="COLLEGE POINT"

    if minCityCalls==corona:
        city="CORONA"
        
    if minCityCalls==eastelmhurst:
        city="EAST ELMHURST"

    if minCityCalls==elmhurst:
        city="ELMHURST"

    if minCityCalls==farrockaway:
        city="FAR ROCKAWAY"

    if minCityCalls==flushing:
        city="FLUSHING"

    if minCityCalls==foresthills:
        city="FOREST HILLS"

    if minCityCalls==glenoaks:
        city="GLEN OAKS"

    if minCityCalls==hollis:
        city="HOLLIS"

    if minCityCalls==howardbeach:
        city="HOWARD BEACH"

    if minCityCalls==jacksonheights:
        city="JACKSON HEIGHTS"

    if minCityCalls==jamaica:
        city="JAMAICA"

    if minCityCalls==kewgardens:
        city="KEW GARDENS"

    if minCityCalls==littleneck:
        city="LITTLE NECK"

    if minCityCalls==longislandcity:
        city="LONG ISLAND CITY"

    if minCityCalls==maspeth:
        city="MASPETH"

    if minCityCalls==newyork:
        city="NEW YORK"

    if minCityCalls==ozonepark:
        city="OZONE PARK"

    if minCityCalls==queensvillage:
        city="QUEENS VILLAGE"

    if minCityCalls==regopark:
        city="REGO PARK"

    if minCityCalls==richmondhill:
        city="RICHMOND HILL"

    if minCityCalls==ridgewood:
        city="RIDGEWOOD"

    if minCityCalls==rockawaypark:
        city="ROCKAWAY PARK"

    if minCityCalls==rosedale:
        city="ROSEDALE"

    if minCityCalls==saintalbans:
        city="SAINT ALBANS"

    if minCityCalls==southozonepark:
        city="SOUTH OZONE PARK"

    if minCityCalls==southrichmondhill:
        city="SOUTH RICHMOND HILL"

    if minCityCalls==statenislandcity:
        city="STATEN ISLAND"

    if minCityCalls==sunnyside:
        city="SUNNYSIDE"

    if minCityCalls==whitestone:
        city="WHITESTONE"

    if minCityCalls==woodhaven:
        city="WOODHAVEN"

    if minCityCalls==woodside:
        city="WOODSIDE"

    



#-----------------------------------------------------------#
    if minBoroughCalls==bronx:
        borough="BRONX"

    if minBoroughCalls==brooklyn:
        borough="BROOOKLYN"

    if minBoroughCalls==manhattan:
        borough="MANHATTAN"

    if minBoroughCalls==queens:
        borough="QUEENS"

    if minBoroughCalls==statenisland:
        borough="STATEN ISLAND"

    if minBoroughCalls==unspecified:
        borough="Unspecified"


    quietest_city_and_borough = {'city': city, 'borough': borough, 'num_city_calls': minCityCalls, 'num_borough_calls': minBoroughCalls}



    return quietest_city_and_borough


if __name__ == '__main__':
    bar_data = get_bar_party_data()

    # uncomment the line below to see what the data looks like
    #print_data(bar_data)

    noisy_metrics = get_most_noisy_city_and_borough(bar_data)

    quiet_metrics = get_quietest_city_and_borough(bar_data)

    print('Noisy Metrics: {}'.format(noisy_metrics))
    print('Quiet Metrics: {}'.format(quiet_metrics))
