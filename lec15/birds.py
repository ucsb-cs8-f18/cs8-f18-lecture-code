def new_sighting(kinds, counts, sighting):
    if sighting not in kinds:
        kinds.append(sighting)
        # missing code
        counts.append(0) # A
 #       counts.append(1) #B

    ind = kinds.index(sighting)
    counts[ind]+=1

'''

'''
def new_sighting_2(bird_dict, sighting):
    if sighting not in bird_dict:
        bird_dict[sighting] = 0
    bird_dict[sighting]+=1
        
    
