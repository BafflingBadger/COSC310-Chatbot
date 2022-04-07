import googlemaps

def get_place(query):

    # Define the API key
    API_KEY = "AIzaSyAzzRV3vyaSdqYVtPeoiJbie5-BB-OD3aM"

    # Define our client
    gmaps = googlemaps.Client(key = API_KEY)

    # Search a place
    my_fields = ['name', 'formatted_address', 'place_id']
    results = gmaps.find_place(input=query, input_type='textquery', fields=my_fields)

    # Get a place_id and get details of that place
    my_place_id = results['candidates'][0]['place_id']
    my_fields = ['name', 'formatted_address', 'rating', 'formatted_phone_number', 'type']
    results_detail = gmaps.place(place_id=my_place_id, fields=my_fields)

    # Extract specific data from results and return them as an array
    name = results_detail['result']['name']
    address = results_detail['result']['formatted_address']
    phone = results_detail['result']['formatted_phone_number']
    rating = results_detail['result']['rating']
    details = [name, address, phone, rating]

    return details, my_place_id



def get_directions(my_place_id):

    # Define the API key
    API_KEY = "AIzaSyAzzRV3vyaSdqYVtPeoiJbie5-BB-OD3aM"

    # Define our client
    gmaps = googlemaps.Client(key = API_KEY)

    # Get directions from U-Six to a certain place
    my_directions = gmaps.directions(origin='695 Academy Way, Kelowna, BC, Canada', destination='place_id:'+my_place_id, mode='driving')

    # Make a single string composed of all directions and return that string
    old_instructions = ''
    for step in my_directions[0]['legs'][0]['steps']:
        instructions = step['html_instructions'].replace('<b>','').replace('</b>','').replace('<div style="font-size:0.9em">', '. ').replace('</div>', '').replace('<wbr/>', '') + '. '
        instructions = old_instructions + instructions
        old_instructions = instructions
    
    return instructions

