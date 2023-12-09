class DataCleaning():
    
    @staticmethod
    def clean_user_data(table):

        table.loc[table.index[  table.lat.apply( lambda lat: str.lower(str(lat)) ) == "null"  ], "lat" ] = None

        table.drop(table.index[  table.staff_numbers.apply( lambda code: len(str(code)) ) == 10  ], inplace=True)

        if "index" in table.columns: table.drop("index", axis=1, inplace=True)

        return table
