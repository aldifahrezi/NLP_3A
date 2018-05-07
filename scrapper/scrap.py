import json
import os
import requests
import pickle

ZOMATO_API_KEY = (os.environ['ZOMATO_API_KEY'])

def get_cities():
    cities = [
        "jakarta",
        "depok",
        "bogor",
        "banten",
        "bandung",
        "semarang",
        "surabaya",
        "denpasar",
        "makassar",
        "medan",
        "aceh",
        "Yogyakarta",
        "solo",
        "malang",
        "manado",
        "padang"
        "lombok",
        "pasar minggu",
        "senayan",
        "cirebon",
        "menteng",
        "kelapa gading",
        "thamrin",
        "tanjung duren",
        "beji",
        "sudirman",
        "bekasi",
        "pondok aren",
        "setiabudi",
        "dharmawangsa",
        "tebet",
        "kemang",
        "kuningan",
        "pondok indah",
        "pluit",
        "puri indah",
        "bogor utara",
        "bekasi utara",
        "thamrin",
        "serpong utara",
        "pantai indah kapuk",
        "gandaria",
        "serpong",
        "fatmawati",
        "cikini",
        "blok m",
        "palu",
        "palembang",
        "benda",
        "cibodas",
        "ciledug",
        "cipondoh",
        "ciputat",
        "ciputat timur",
        "jatiuwung",
        "pamulang",
        "pinang",
        "cengkareng",
        "kebon jeruk",
        "roxy",
        "slipi",
        "hayam wuruk",
        "klender",
        "jatinegara",
        "cisarua",
    ]

    return cities

def get_restaurant_ids(cities):
    headers = {'user-key': ZOMATO_API_KEY}

    restaurant_ids = set()

    for city in cities:
        url = 'https://developers.zomato.com/api/v2.1/search?count=20&q={}'.format(city)
        r = requests.get(url, headers=headers)
        json_data = json.loads(r.text)
        for restaurant in json_data['restaurants']:
            restaurant_ids.add(restaurant['restaurant']['R']['res_id'])

    return list(restaurant_ids)

def get_restaurant_reviews(restaurant_ids):
    headers = {'user-key': ZOMATO_API_KEY}

    reviews = []
    
    for restaurant_id in restaurant_ids:
        url = 'https://developers.zomato.com/api/v2.1/reviews?res_id={}'.format(restaurant_id)
        r = requests.get(url, headers=headers)
        json_data = json.loads(r.text)

        if 'user_reviews' in json_data:
            for review in json_data['user_reviews']:
                reviews.append(review['review']['review_text'])

    return reviews

def main():
    ######################################################################
    # get restaurant ids
    # cities = get_cities()

    # restaurant_ids = get_restaurant_ids(cities)

    # restaurant_json = json.dumps({'restaurant_ids': restaurant_ids})

    # with open('restaurant_ids.json', 'w') as fp:
    #     json.dump(restaurant_json, fp, ensure_ascii=False)
    ######################################################################

    ######################################################################
    # get reviews
    # with open('restaurant_ids.json', 'r') as fp:
    #     restaurant_ids = json.load(fp)['restaurant_ids']

    # reviews = get_restaurant_reviews(restaurant_ids)

    # reviews_json = json.dumps({'reviews': reviews})

    # with open('reviews.json', 'w') as fp:
    #     json.dump(reviews_json, fp, ensure_ascii=False)
    ######################################################################

    with open('reviews.json', 'r') as fp:
        reviews = json.load(fp)['reviews']

if __name__ == '__main__':
    main()