# **Introduction**

Not only SQL databases: the objective of this activity is to learn the concepts related to NoSQL using as tool MongoDB and Compass.

# **Execution instructions**

## **You can execute the activity by**

    1. Installing MongoDB and Compass.  
    
    2. Following the queries examples using Mongo's shell, Mongosh:

* *Create database:*

      use unit18

* *Create two collections:*
   
      db.createCollection("Books")

      db.createCollection("Client")

* *Insert one document:* 
 
      db.Books.insertOne({_id: 1,
                          Name: 'Alice in Wonderland',
                          Author: 'Lewis Carrol', 
                          Genre: 'Fantasy'})

      db.Client.insertOne({_id: 1, Name: 'Mary'})


* *Insert many documents simultaneously:*

      db.Books.insertMany([{_id: 2,
                            Name: 'Adventures of Tom Sawyer',
                            Author: 'Mark Twain'},
                            {_id: 3, 
                             Name: 'A passage to India',
                             Author: 'E.M.Forster'}])

      db.Client.insertMany([{_id: 2,
                             Name: 'Peter',
                             LastName: 'Gomez'},
                             {_id: 3,
                              Name: 'Sara',
                              City: 'Cordoba'}])


* *Show the documents inside collections:*
   
      db.Books.find()

      db.Client.find()


* *Show a specific document inside a collection:*

      db.Books.find({Author: 'Mark Twain'})

      db.Client.find({City: 'Cordoba'})


* *Update a register:*

      db.Books.updateOne({_id: 1}, {$set: {InStock: 'no'}})

      db.Client.updateOne({_id: 2}, {$set: {Name: 'Peter Adrei'}})


* *Update many registers simultaneously:*

      db.Books.updateMany({_id: {$gt: 1}}, {$set: {Genre: 'Realistic'}})

      db.Client.updateMany({}, {$set: {Bill: 'yes'}})

## **Results**

You can export the results as .json files like in this folder. 




