#!/usr/bin/bash

pwd
rm -rf deployment
rm shopify_unsubscribe.zip
mkdir deployment
pip install -r requirements.txt --target deployment
cd deployment
cp ../lambda_function.py .
cp -r ../templates .
zip -r ../shopify_unsubscribe.zip .
cd ..
aws lambda update-function-code --function-name shopify_unsubscribe --zip-file fileb://shopify_unsubscribe.zip

# rm -rf deployment
# mkdir deployment
# cp -r templates deployment
# cp lambda_function.py deployment
# cd deployment
# zip -r ../shopify_unsubscribe.zip .
# cd ..