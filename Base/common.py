import json


# def rename_header(dataframe):
#     temp_headers = json.load(open("../Data/Headers.json", "r"))
#     headers = {key: value['header'] for key, value in temp_headers.items()}
#     dataframe.rename(columns=headers, inplace=True)
#
#     return temp_headers


def get_category_wise_labels(question):
    data = json.load(open("../data/category_wise_labels.json", "r"))

    return data.get(question)
