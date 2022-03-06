#!/usr/bin/bash

# pwd
# rm -rf deployment
# rm shopify_subscriber.zip
# mkdir deployment
# cd deployment
# pip install -r ../requirements.txt --target package
# cp ../lambda_function.py .
# zip -r ../shopify_subscriber.zip .
# cd ..
rm -rf deployment
mkdir deployment
cp -r templates deployment
cp lambda_function.py deployment
cd deployment
zip -r ../shopify_unsubscribe.zip .
cd ..
aws lambda update-function-code --function-name shopify_unsubscribe --zip-file fileb://shopify_unsubscribe.zip