
def word_counter (sentence):
    if not isinstance(sentence, str):
        return "Esta función solo recibe Strings"
    list_words = sentence.split()
    unique_words = set(list_words)
    frequency_words = [(word, list_words.count(word)) for word in unique_words]
    return order_list(frequency_words)

def order_list (list):
    return sorted(list, key=lambda a: a[1], reverse = True)

if __name__ == '__main__':
    print(word_counter("el perro es muy grande y el gato es muy pequeño"))
