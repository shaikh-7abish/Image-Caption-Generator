## Main Folder
### Preprocess.ipynb:
**Preprocess Notebook** is used to clean and visualize data from Image and Caption Dataset. This Notebook creates a text file `description.txt` with processed captions and image name as their indexes.

<hr>

### Main.ipynb:
**Main Notebook** is used to create and save model. This Notebook also uses **VGG16 Model** to extract features from Images and `description.txt` to create **Tokenizer** for vocabulary in captions.
Then creates, train's and save's a **LSTM Model** for Caption Generation.

<hr>
