import string
from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/cal_sim', methods=['POST'])
def cal_sim_api():
    """
    POST request:
    accept: JSON {
    "text1":"tssd sd asd asd asd ",
    "text2":"tssds asd sd ad asd s"
}
	Returns:
		{"Similarity": 0.5 }
    """
    text1 = request.json.get("text1")
    text2 = request.json.get("text2")
    if not (text1 and text2):
        return 'bad input parameter!', 500
    words_1 = find(text1)
    words_2 = find(text2)
    freq_dict_1 = freq(words_1)
    freq_dict_2 = freq(words_2)
    return {"Similarity" : calc_sim(freq_dict_1, freq_dict_2)}

def find(text):
    """
    text: string
    returns: list of words from input text
    """
    text = text.replace("\n", " ")
    for char in string.punctuation:
        text = text.replace(char, " ")
    words = text.split(" ")
    return words

def freq(words):
    """
    words: list of words
    returns: frequency dictionary for input words
    """

    freq_dict = {}

    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict

def calc_sim(dict1, dict2):
    """
    dict1: frequency dictionary for one text
    dict2: frequency dictionary for another text
    returns: float, representing how similar both texts are to each other
    """
    diff = 0
    total = 0

    for word in dict1.keys():
        if word in dict2.keys():
            diff += abs(dict1[word] - dict2[word])
        else:
            diff += dict1[word]

    for word in dict2.keys():
        if word not in dict1.keys():
            diff += dict2[word]

    total = sum(dict1.values()) + sum(dict2.values())
    difference = diff / total
    similar = 1.0 - difference

    return round(similar, 2)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')