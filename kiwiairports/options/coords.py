def lat(locations):
    return [loc['location']['lat'] for loc in locations]


def lon(locations):
    return [loc['location']['lon'] for loc in locations]
