# we12
Visualization project for the EuroSAI (1st Hackathon of EuroSAI in Prague 2020)

## Team WE12
France: Arnaud Périgord, Maria Heyaca, Xavier Bailly

Estonia: Thea Teinemaa, Kaia Philips

Croatia: Ivana Krizanic-Delisimunovic, Zeljka Dolezal-Bozic 

## Description
This solution helps make better use of the data collected in EUROSAI’s database of audit reports, which is administered by the Czech SAI. By providing visualizations, it enables users to see the data in a more analytical way and efficiently get an overview of the data. The end goal is to include these visualization options on the EUROSAI website.

For EUROSAI, this will offer insights into emerging trends in auditing, for example which topics have recently received more attention and where there could be potential for cooperation.  It will also help get a quick overview of how active different countries are in contributing to the database.

Auditors and other SAI professionals will be able to see which countries have worked most with certain topics they are interested in and could provide useful information, and which topics are covered less by their own SAI.
The solution also aims to increase the use of the database and encourage SAIs to contribute to it.

## Data set
EUROSAI database of audit reports 
https://www.eurosai.org/en/databases/audits/index.html 

## Solution
1. Scrapped data from the EUROSAI site with the following data for each reports : title, subject(s), year of publishing, country/countries, link to the EUROSAI report page
2. Visualization tools used : Flourish (free version)
3. Dashboard website to present it

## Screenshot
This is the main view of the app when you launch it. 

![Main View](https://github.com/aperigord/we12/blob/master/Screenshot/main_view.PNG)

You can have a view of the activity of all countries in EuroSAI

![Map View](https://github.com/aperigord/we12/blob/master/Screenshot/map_view.PNG)

We tried to show how reports are split amongst countries and themes. If you click on it, you are redirected to the reports themselves on the EuroSAI website

![Country Treemap](https://github.com/aperigord/we12/blob/master/Screenshot/country_treemap.PNG)


Another approach for an auditor would be to look at a specific subject to see what has been published.

![Subjects Treemap](https://github.com/aperigord/we12/blob/master/Screenshot/subject_treemap.PNG)

EuroSAI is quite new in publishing reports, so this is a timelapse

![Timelapse View](https://github.com/aperigord/we12/blob/master/Screenshot/timelapse_view.PNG)
