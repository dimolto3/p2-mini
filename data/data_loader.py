import pandas as pd


host_country_map = {
    # 하계 올림픽
    'Athina': 'GRE',
    'Paris': 'FRA',
    'St. Louis': 'USA',
    'London': 'GBR',
    'Stockholm': 'SWE',
    'Antwerpen': 'BEL',
    'Amsterdam': 'NED',
    'Los Angeles': 'USA',
    'Berlin': 'GER',
    'Helsinki': 'FIN',
    'Melbourne': 'AUS',
    'Roma': 'ITA',
    'Tokyo': 'JPN',
    'Mexico City': 'MEX',
    'Munich': 'GER', 
    'Montreal': 'CAN',
    'Moskva': 'RUS', 
    'Seoul': 'KOR',
    'Barcelona': 'ESP',
    'Atlanta': 'USA',
    'Sydney': 'AUS',
    'Beijing': 'CHN',
    'Rio de Janeiro': 'BRA',

    # 동계 올림픽
    'Chamonix': 'FRA',
    'Sankt Moritz': 'SUI',
    'Lake Placid': 'USA',
    'Garmisch-Partenkirchen': 'GER',
    'Oslo': 'NOR',
    'Cortina d\'Ampezzo': 'ITA',
    'Squaw Valley': 'USA',
    'Innsbruck': 'AUT',
    'Grenoble': 'FRA',
    'Sapporo': 'JPN',
    'Sarajevo': 'YUG',
    'Calgary': 'CAN',
    'Albertville': 'FRA',
    'Lillehammer': 'NOR',
    'Nagano': 'JPN',
    'Salt Lake City': 'USA',
    'Torino': 'ITA',
    'Vancouver': 'CAN',
    'Sochi': 'RUS'
}

def load_olympic():
    olympic_df = pd.read_csv('data/athlete_events.csv')
    olympic_df['host_NOC'] = olympic_df['City'].map(host_country_map)
    olympic_df['is_host'] = olympic_df['NOC'] == olympic_df['host_NOC']
    return olympic_df

def get_noc_region_map():
    noc_df = pd.read_csv('data/noc_regions.csv')
    return noc_df.set_index('NOC')['region'].to_dict()

if __name__ == '__main__':
    olympic = load_olympic()
    print(olympic.head())
    noc_region = get_noc_region_map()
    print(noc_region['AUS'])