#"photo.jpg, Warsaw, 2013-09-05 14:08:15"

def solution(S):
    # write your code in Python 3.6

    from datetime import datetime

    list_S = [line for line in S.split("\n") if line != "" and len(line.split(", ")) == 3]
    cities_dict = {}

    for line in list_S:
        line_info = line.split(", ")

        if len(line_info) != 3:
            continue

        photo_name = line_info[0]

        city = line_info[1]
        date = line_info[2]

        date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

        if not city in cities_dict:
            cities_dict[city] = []

        cities_dict[city].append({"photo_name": photo_name, "date": date})

    cities_ordered_dict = {}

    for city in cities_dict.keys():
        cities_ordered_dict[city] = {"count": len(cities_dict[city]), "ordered": sorted(cities_dict[city], key=lambda x: x["date"])}


    string_result = ""

    for line in list_S:
        line_info = line.split(", ")

        if len(line_info) != 3:
            continue

        photo_name = line_info[0]
        city = line_info[1]

        photo_in_ordered_city = [ordered_city for ordered_city in cities_ordered_dict[city]["ordered"] if ordered_city["photo_name"] == photo_name][0]
        photo_index_in_city = cities_ordered_dict[city]["ordered"].index(photo_in_ordered_city) + 1

        photo_print_index = str(photo_index_in_city).zfill(len(str(cities_ordered_dict[city]["count"])))
        photo_format = photo_name.split(".")[1]

        photo_print_result = f"{city}{photo_print_index}.{photo_format}"

        string_result += photo_print_result

        if line != list_S[-1]:
            string_result += "\n"


    return string_result


test = ("photo.jpg, Warsaw, 2013-09-05 14:08:15\n"
"john.png, London, 2015-06-20 15:13:22\n"
"myFriends.png, Warsaw, 2013-09-05 14:07:13\n"
"Eiffel.jpg, Paris, 2015-07-23 08:03:02\n"
"pisatower.jpg, Paris, 2015-07-22 23:59:59\n"
"BOB.jpg, London, 2015-08-05 00:02:03\n"
"notredame.png, Paris, 2015-09-01 12:00:00\n"
"me.jpg, Warsaw, 2013-09-06 15:40:22\n"
"a.png, Warsaw, 2016-02-13 13:33:50\n"
"b.jpg, Warsaw, 2016-01-02 15:12:22\n"
"c.jpg, Warsaw, 2016-01-02 14:34:30\n"
"d.jpg, Warsaw, 2016-01-02 15:15:01\n"
"e.png, Warsaw, 2016-01-02 09:49:09\n"
"f.png, Warsaw, 2016-01-02 10:55:32\n"
"g.jpg, Warsaw, 2016-02-29 22:13:11\n")


print(solution(test))