import pymongo

# Connect to the test.proj3 database collection
client = pymongo.MongoClient("mongodb+srv://hoolio96:V3x_Myth0c145t@cluster0.vhnra.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
collection = db.proj3

input_category = ''
input_search = ''

while (input_category != 'quit'):
    print('Input field to query (title, redirect, category, references, author)')
    print('Input "quit" to exit')
    input_category = input('')

    if (input_category == 'title' or input_category == 'category' or input_category == 'references'):
        print('Input string to search for:')
        input_search = input('')

    elif (input_category == 'author'):
        print('Input regular expression to search for:')
        input_search = input('')
    
    if (input_category == 'title'):
        print('Searching for information on "' + input_search + '"...')

        pipeline = [{'$unwind':'$mediawiki.page'}, {'$match':{'mediawiki.page.title':input_search}}, {'$project':{'_id':0, 'mediawiki.siteinfo':0, 'mediawiki.@xmlns':0, 'mediawiki.@xmlns:xsi':0, 'mediawiki.@xsi:schemaLocation':0, 'mediawiki.@version':0, 'mediawiki.@xml:lang':0}}]

        cursor=collection.aggregate(pipeline)

        result = list(cursor)

        for item in result:
            print(item)
        
        if (len(result) == 0):
            print('None found')

    elif (input_category == 'redirect'):
        print('Searching for all pages that redirect to another...')

        pipeline = [{'$unwind':'$mediawiki.page'}, {'$match':{'mediawiki.page.revision.comment': {'$regex': 'Redirect'}}}, {'$project':{'_id':0, 'mediawiki.siteinfo':0, 'mediawiki.@xmlns':0, 'mediawiki.@xmlns:xsi':0, 'mediawiki.@xsi:schemaLocation':0, 'mediawiki.@version':0, 'mediawiki.@xml:lang':0, 'mediawiki.page.ns':0, 'mediawiki.page.id':0, 'mediawiki.page.revision':0}}]

        cursor=collection.aggregate(pipeline)

        result = list(cursor)

        for item in result:
            print(item)
        
        if (len(result) == 0):
            print('None found')

    elif (input_category == 'category'):
        print('Searching for all pages that are part of the category "' + input_search + '"...')

        input_search = '\[\[Category:' + input_search + '\]\]'

        pipeline = [{'$unwind':'$mediawiki.page'}, {'$match':{'mediawiki.page.revision.text.$': {'$regex': input_search}}}, {'$project':{'_id':0, 'mediawiki.siteinfo':0, 'mediawiki.@xmlns':0, 'mediawiki.@xmlns:xsi':0, 'mediawiki.@xsi:schemaLocation':0, 'mediawiki.@version':0, 'mediawiki.@xml:lang':0, 'mediawiki.page.ns':0, 'mediawiki.page.id':0, 'mediawiki.page.revision':0, 'mediawiki.page.redirect':0}}]

        cursor=collection.aggregate(pipeline)

        result = list(cursor)

        for item in result:
            print(item)
        
        if (len(result) == 0):
            print('None found')
    
    elif (input_category == 'references'):
        print('Searching for all pages that contain links to "' + input_search + '"...')

        input_search = '\[\[' + input_search + '\]\]'

        pipeline = [{'$unwind':'$mediawiki.page'}, {'$match':{'mediawiki.page.revision.text.$': {'$regex': input_search}}}, {'$project':{'_id':0, 'mediawiki.siteinfo':0, 'mediawiki.@xmlns':0, 'mediawiki.@xmlns:xsi':0, 'mediawiki.@xsi:schemaLocation':0, 'mediawiki.@version':0, 'mediawiki.@xml:lang':0, 'mediawiki.page.ns':0, 'mediawiki.page.id':0, 'mediawiki.page.revision':0, 'mediawiki.page.redirect':0}}]

        cursor=collection.aggregate(pipeline)

        result = list(cursor)

        for item in result:
            print(item)
        
        if (len(result) == 0):
            print('None found')
    
    elif (input_category == 'author'):
        print('Searching for all pages whose author contains the regular expression "' + input_search + '"...')

        pipeline = [{'$unwind':'$mediawiki.page'}, {'$match':{'mediawiki.page.revision.contributor.username': {'$regex': input_search}}}, {'$project':{'_id':0, 'mediawiki.siteinfo':0, 'mediawiki.@xmlns':0, 'mediawiki.@xmlns:xsi':0, 'mediawiki.@xsi:schemaLocation':0, 'mediawiki.@version':0, 'mediawiki.@xml:lang':0, 'mediawiki.page.ns':0, 'mediawiki.page.id':0, 'mediawiki.page.revision':0, 'mediawiki.page.redirect':0}}]

        cursor=collection.aggregate(pipeline)

        result = list(cursor)

        for item in result:
            print(item)
        
        if (len(result) == 0):
            print('None found')
    
    elif (input_category == 'quit'):
        print('Quitting...')
    
    else:
        print('Invalid input')