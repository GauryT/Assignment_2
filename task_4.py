import spacy
from transformers import AutoTokenizer

# Initialize spaCy model
spacy_model = spacy.load('en_core_sci_sm')

# Initialize BioBERT tokenizer
biobert_tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")

def perform_ner(text, spacy_model, biobert_tokenizer):
    # NER using en_core_sci_sm
    doc_spacy = spacy_model(text)
    entities_spacy = [(ent.text, ent.label_) for ent in doc_spacy.ents]

    # NER using BioBERT
    tokens_biobert = biobert_tokenizer.tokenize(biobert_tokenizer.decode(biobert_tokenizer.encode(text)))
    tokens_biobert_str = ' '.join(tokens_biobert)
    entities_biobert = []

    for entity in tokens_biobert_str.split():
        if 'Disease' in entity:
            entities_biobert.append((entity, 'DISEASE'))
        elif 'Drug' in entity:
            entities_biobert.append((entity, 'CHEMICAL'))

    return entities_spacy, entities_biobert

# Sample text
text = "Your biomedical text here."

# Perform NER and get results
entities_spacy, entities_biobert = perform_ner(text, spacy_model, biobert_tokenizer)

# Compare the results
total_entities_spacy = len(entities_spacy)
total_entities_biobert = len(entities_biobert)

print("Total Entities (en_core_sci_sm):", total_entities_spacy)
print("Total Entities (BioBERT):", total_entities_biobert)
print("Entities (en_core_sci_sm):", entities_spacy)
print("Entities (BioBERT):", entities_biobert)