# atlantic_data
Data wrangling test for The Atlantic

** Files **
- sample_data.txt - Generated using Mockaroo. Source: https://www.mockaroo.com (Schema: https://www.mockaroo.com/fa830660)
- droopy - Droopy upload server (customized to add call to process_data script). Source: https://github.com/stackp/Droopy
- process_data.py - Script to process uploaded TSV files


*To Run:*
mkdir ./upload
./droopy -d ./upload

Visit http://localhost:8000/ and upload a file.