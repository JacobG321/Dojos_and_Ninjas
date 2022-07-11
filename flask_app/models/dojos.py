
from flask_app.config.mysqlconnection import connectToMySQL

class Dojos:
    db_name = 'dojos_and_ninjas_schema'
    def __init__(self , data ):
        self.id = data['id']
        self.dojo_name = data['dojo_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #display all dojos
    @classmethod
    def get_all( cls ):
        query = 'SELECT * FROM dojos'
        #access class variables using cls in front of the variable in a method
        results = connectToMySQL(cls.db_name).query_db(query)
        if len(results) == 0:
            return []
        else:
            dojos = []
            for dojo in results:
                dojos.append( cls(dojo) )
            return dojos

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO dojos ( dojo_name ) VALUE ( %(dojo_name)s )"
        return connectToMySQL(cls.db_name).query_db( query, data )

    #display all ninjas from specific dojo
    @classmethod
    def get_all_ninjas_from_dojo( cls, data ):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas on ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s'
        return connectToMySQL(cls.db_name).query_db( query, data )


#cls is calling on the constructor, we use CLS in place of Dojos because we are in a class method
