import json, os

def load_dictionary(file_name):
    if os.path.exists(file_name):
        try:
            with open(file_name, 'r') as file:
                return json.load(file)
        except:
            print("Error loading dictionary. Using default dictionary.")
    return {"hello": "hei", "world": "maailma"}

def save_dictionary(dictionary, file_name):
    try:

        script_dir = os.path.dirname(os.path.realpath(__file__))

        file_path = os.path.join(script_dir, file_name)
        
        with open(file_path, 'w') as file:
            json.dump(dictionary, file, indent=4)
            
    except Exception as e:
        print("Error saving dictionary:", str(e))

def search_word(dictionary, word):
    if word in dictionary:
        return dictionary[word]
    else:
        return None

def main():
    file_name = "dictionary.json"
    dictionary = load_dictionary(file_name)

    while True:
        word = input("Enter a word to translate (or press Enter to exit): ").strip()
        if not word:
            break

        translation = search_word(dictionary, word)
        if translation:
            print(f"The translation of '{word}' is: {translation}")
        else:
            print("not found.")
            definition = input("Please input a definition: ").strip()
            if definition:
                dictionary[word] = definition
                save_dictionary(dictionary, file_name)
                print(f"Word '{word}' with definition '{definition}' added to the dictionary.")

    print("Exiting.")

if __name__ == "__main__":
    main()
