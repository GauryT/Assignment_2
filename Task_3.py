from collections import Counter
import csv
from transformers import AutoTokenizer  # Import the BioBERT tokenizer

# Initialize the BioBERT tokenizer
biobert_tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")

# Sample text for tokenization
text = "Your biomedical text here."

# Count word occurrences
def count_word_occurrences(filename, num_top_words):
    word_counts = Counter()
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            word_counts.update(words)
    
    top_words = word_counts.most_common(num_top_words)
    return top_words

# Write word occurrences to a CSV file
def write_word_occurrences_to_csv(filename, word_occurrences):
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Word', 'Count'])
        csv_writer.writerows(word_occurrences)

# Count token occurrences using the BioBERT tokenizer
def count_token_occurrences(text, tokenizer, num_top_tokens):
    tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(text)))
    token_counts = Counter(tokens)
    
    top_tokens = token_counts.most_common(num_top_tokens)
    return top_tokens

# Usage
filename = 'combined_text.txt'
num_top_words = 30
num_top_tokens = 30