# Basic script to check a CV.
# Looking for keywords (positive and negative) and length of a summary statement
# Ouputs a score
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


# List of keywords and phrases to look for in the CV
keywords = ['TEXT1', 'TEXT2', 'ETC']

# List of words and phrases to avoid in the CV
negative_keywords = ['TEXT1', 'TEXT2', 'ETC']

# Open the CV file and read the text
with open('FILELOCATION', 'r') as cv_file:
  cv_text = cv_file.read()

# Tokenize the text and lowercase all the words
cv_tokens = nltk.word_tokenize(cv_text.lower())

# Use NLTK's Part of Speech tagger to tag each token
cv_pos_tags = nltk.pos_tag(cv_tokens)

# Count the number of times each keyword appears in the CV
keyword_count = 0
for keyword in keywords:
  keyword_count += cv_tokens.count(keyword)

# Count the number of times each negative keyword appears in the CV
negative_keyword_count = 0
for negative_keyword in negative_keywords:
  negative_keyword_count += cv_tokens.count(negative_keyword)


# Count the number of grammar and punctuation errors in the CV
error_count = 0

for token, pos_tag in cv_pos_tags:
  # Check for articles, prepositions, and conjunctions
  if pos_tag in ['DT', 'IN', 'CC']:
    error_count += 1

  # Check for punctuation
  elif token in [',', '.', ';', ':', '!', '?']:
    error_count += 1
  # Check for plural nouns and verbs
  elif pos_tag in ['NNS', 'VBP']:
    error_count += 1
  # Check for possessive nouns
  elif pos_tag == 'NNS' and token[-2:] == "'s":
    error_count += 1

# check for length of summary (or whatever paragraph you want to check)
start_index = cv_text.index("STARTING TEXT")
end_index = cv_text.index("ENDING TEXT")

statement = cv_text[start_index:end_index]
statement_len = statement.split()

# Arbitrary scoring for length of statment
num_words = len(statement_len)
if num_words < 10:
    statement_score = -50

# Calculate the score based on the number of keywords, negative keywords, and errors
score = (keyword_count - negative_keyword_count - error_count) / len(keywords) * 100
score = score - statement_score 

# Print the score
print(f"CV score: {score:.2f}")