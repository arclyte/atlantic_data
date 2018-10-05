# atlantic_data
Data wrangling test for The Atlantic

** Files **
- atlantic_data.txt - Test TSV upload data generated using Mockaroo. Source: https://www.mockaroo.com (Schema: https://www.mockaroo.com/fa830660)
- droopy - Droopy upload server (customized to add call to process_data script). Source: https://github.com/stackp/Droopy
- process_data.py - Script to process uploaded TSV files
- models/* - SQLAlchemy models, base.py contains the DSN url
- README.md - this file
- requirements.txt - pip requirements file
- schema.sql - mysqldump of tables required for test (contains create database statement)
- upload/ - files processed by droopy are dropped here

** Assumptions **
- Python3 (scripts tested on version 3.6.5)
- MySQL on localhost with no password. (Tested on version 8.0.12 Homebrew (OSX))


**To Run:**
1. Install requirements: `pip3 install -r requirements.txt`
2. Import DB schema: `mysql -h localhost -u root < schema.sql`
3. Run modified droopy server: `./droopy -d ./upload`
4. Visit http://localhost:8000/ and upload a file.
5. DB tables contain migrated data.

Note: process_data.py also contains two lines at the end of the file (marked DEBUG) that allow running it directly from the command line for testing.