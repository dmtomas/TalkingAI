# SpeakingAI
language: Spanish


# Resume

The objective of this AI is to learn how to speak with a person reading my what's app messages. For this the AI will have a dictionary with spanish words vectorized and will train using the library TensorFlow.

# V0
results: Not Good, with overfitting it can make some good answers but most are bad.
- Each word has a vector of dimension 10 associated. The value is given by how much the word appears in the 10 different texts.
- A Neural network learns with about 30 examples and the gets overfitted running hundreds of times.
- Speking.py translates the vectors values into words (really Slow).

# Future work.
- Make one AI that takes the full message and compress it to just give the context of the conversation.
- Use word2Vec algorithm and use more text to improve the AI dictionary.
- Order the dictionary by angle and normalize the vectors so it is easier to find words in Speaking.py.
- Make more data to analize.
