def designerPdfViewer(h, word):
    # Write your code here
    letters_height = []
    for symbol in word:
        letters_height.append(h[ord(symbol)-97])
    return max(letters_height)*len(word)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
