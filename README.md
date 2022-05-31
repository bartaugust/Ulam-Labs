# Ulam-Labs

## API
API was built using Google App Engine.

### Updates
In order to apply changes from Github you need to download repository.
Using gcloud CLI terminal in projects working directory write command
```
gcloud app deploy
```
Only works after correct login using 
```
gcloud init
```
### URL
https://ulam-labs.lm.r.appspot.com/

### Home Page

There is an empty textfield to write text you want to encode.
When the textfield is filled 'Encode' button will take you to Encode Page

### Encode Page

You can only go to this page from Home Page.
There is a textfield with encoded text form Home Page inside. 
This text can be eddited.
'Decode' button will take you to Decode Page 

### Decode Page

You can only go to this page from Encode Page.
Shows decoded text from Encode Page.
If text was not correctly encoded site will show Internal Server Error.

## Project Structure

### Functionality
All functionality is written in python using Flask for web integrastion.
Encoding and decoding function are located in main.py along with flask functions for web requests.

### Test
Test are made using pytest. 
They are located in tests directory.
encode_tests.py contains tests for encoder and decode_tests.py contains tests for decoder.

### HTML
HTML templates for sites are located in templates directory.



