# Automated User Behaviour Analysis (AUBA) Tool
## Command line tool to profile User behaviour based on their activity data like google takeout data, Automate the analysis phase of google data **Export** Important data to csv, and then list the **TOP-20** count of data finally generate a pdf report.

Process involves in the PROJECT are:-
- **GET-DATA**: Get the google data of a person with their legal consent 
              from:- http://takeout.google.com/
- **PARSE-DATA**: Parse the Archive to the python script.
- **ANALYSE-DATA** : Analyse the each and every files of google data
- **NORMALIZE-DATA** : Get only the Cricital details from the raw file using **Regular Expression**
- **EXPORT-TO-CSV** : Export the Important data to CSV file for IN-DEPTH ANALYSIS
- **GENERATE-PDF** : Generate a PDF REPORT of TOP-20 ACTIVITY which gives an Outline of a person
## WorkFlow
![AUBA_WorkFlow](https://user-images.githubusercontent.com/30696072/54470584-4ea95280-47d0-11e9-92d0-f2f63cd2e53b.png)

## INTERESTING SCRIPTS:
- **TOP EMAIL-ID**:
- **TOP LOCATIONS VISTED**: - CREATED A HEATMAP OF LOCATION'S VISITED
- **TOP MUSICS**:
- **TOP YOUTUBE**:
- **TOP CHROME HISTORY**:
- **TOP GOOGLE-ASSISTANT**:
  
## Requirements
- Python 2.7
- Python pip
- requests
- Basemap (sudo apt-get install python-mpltoolkits.basemap)

```sh
# git clone https://github.com/prabhudeva17/AUBA.git
# cd AUBA
# sudo ./runscript.py  takeout-20143434.zip
```

### Development

Want to contribute? Great!
Open your favorite Terminal and fix bug if their any.
Still in development more plugin will added in future

License
----

MIT

**Free Software!**



