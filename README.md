### Cat and Dogs and More

(Originally, this was part of a group project to create a Mapping and Graphing tool to be be used for people looking to relocate.  What you are seeing here is a cleaned up version of our end product. You can find the original repo that I forked off of above.)

We started with the idea of ranking and mapping states that had more dogs or cats, and how that might impact where someone might choose to live. (Team dog here.) We expanded our state data set to include several other factors that may influence where someone might choose to live:
    - happiness 
    - nationally ranked (US News & World Report) universities
    - state/federal parks
    - violent crime incidents
    - average income 
    
This data was largely acquired through web scraping but a few CSV's were downloaded.  The violent crime data was acquired from an API call to the FBI DataBase. (This is the work you can see in the notebooks_create_jsons folder.)

Deployment was done through a flask server and the final GeoJSON is created dynamically from the JSON files created in the notebooks and loaded into a MongoDB instance.  From there it is inserted into the bootstrap based web page via Flask's render template.  The data is pulled into both Leaflet for mapping and ChartJS for graphing.  Both visualizations allow the user to select the data in a variety of views.

For this instance I added a remote Mongo DB server to hold the geoJSON and deployed via Heroku to allow online access, rather than having to deploy through a local server in order to see the end product.

(For the ETL section of the project, the Happiness Scraping, College Scraping and Parks Scraping were all my work. For deployment, I set up the flask server as well as the MongoDB instance and the python script that compiled the final GeoJSON. I was the one who created the ChartJS visualizations and I have adapted the Leaflet views.)


____________________________________________________________________________
## Team: "I Don't Think That Should be an Issue"

Gabriella Burns, Michael Raines, Clare Specht and Zane Zmola.

Project Goal:
    Develop a tool that could visualize selected quality of life issues across the United States.  

Scope of Work:
    Web scraping and data retrieval of five subject areas; State Happiness Ratings, Pet Ownership, Violent Crime Incidents, Nationally Ranked Universities and State/National Parks each by state primarily done Pandas/Python.

    Output JSON files for each subject area.
    
    Created GeoJSON incorporting all data with mapping information. 
    
    Loading GeoJSON file into MongoDB.
    
    Establish Flask Server to retrieve data and app to render html templates.

    Mapping data in Leaflet.

    Graphing results in Chart JS.



Thank you mshafrir for your json of state names and abreviations
https://gist.github.com/mshafrir/2646763
