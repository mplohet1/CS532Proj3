# CS532Proj3
This project contains the source code from the JSON file that is imported into MongoDB and the queries that will be used in the demo

Commands:
Command to find information on "Anarchism":
db.proj3.aggregate(
	{$unwind:'$mediawiki.page'},
	{$match:{'mediawiki.page.title':'Anarchism'}}
)
