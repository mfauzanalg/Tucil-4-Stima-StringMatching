from nltk.tokenize import sent_tokenize

def main():
    # f = open ("text.txt", "r")
    # T = f.read()
    # P = "COVID-19"
    text = "God is Great! I won a lottery."
    print(sent_tokenize(text))
    
    

if __name__ == "__main__":
    main()