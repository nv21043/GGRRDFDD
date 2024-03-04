from pymongo import MongoClient

# Replace the connection string with your own
connection_string = "mongodb+srv://grdfifte:MtqxDlcsgXIRINUV@cluster0.aumyesn.mongodb.net"

try:
    # Connect to the MongoDB cluster
    client = MongoClient(connection_string)

    # List all database names
    database_names = client.list_database_names()

    # Print the list of database names
    print("Database names:")
    for db_name in database_names:
        print(db_name)

except Exception as e:
    print("An error occurred:", e)
