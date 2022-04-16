def plant_recommendation(care):

    # bug :if care = 'low':
    #     ^
    #     SyntaxError: invalid

   if care =='low':
        print('aloe')
   elif care == 'medium':
        print('pothos')

 # elif care == 'medium':
 # logic error

   elif care =='high':
        print('orchid')

#  plant_rec('low')
# NameError: name 'plant_rec' is not defined -->runtime error

plant_recommendation('low')
plant_recommendation('medium')
plant_recommendation('high')