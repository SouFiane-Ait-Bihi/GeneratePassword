def is_majuscule(letter):
    return letter.isupper()

def is_miniscule(letter):
    return letter.islower()

def analyze_text(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()

    analysis_results = []

    for word in words:
        word_analysis = []
        for letter in word:
            if is_majuscule(letter):
                word_analysis.append('majuscule')
            elif is_miniscule(letter):
                word_analysis.append('miniscule')
            else:
                word_analysis.append('neither')
        analysis_results.append(word_analysis)

    return analysis_results


filename = "GeneratePassword/myfile.txt"  
analysis_results = analyze_text(filename)

for i, word_analysis in enumerate(analysis_results):
    print(f"La Lign ||| {i + 1}: {' |||'.join(word_analysis)} |||")
