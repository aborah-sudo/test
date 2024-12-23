class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print("Creating a new DatabaseConnection instance.")
            cls._instance = super(DatabaseConnection, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.connection_status = "Not Connected"

    def connect(self):
        if self.connection_status != "Connected":
            print("Connecting to the database...")
            self.connection_status = "Connected"

    def disconnect(self):
        if self.connection_status != "Not Connected":
            print("Disconnecting from the database...")
            self.connection_status = "Not Connected"


if __name__ == "__main__":
    # Create the first instance
    db1 = DatabaseConnection()
    db1.connect()
    print(f"db1 status: {db1.connection_status}")

    # Create the second instance
    db2 = DatabaseConnection()
    print(f"db2 status: {db2.connection_status}")

    # Verify that both instances are the same
    print(f"db1 is db2: {db1 is db2}")

    # Disconnect using db2
    db2.disconnect()
    print(f"db1 status after db2 disconnect: {db1.connection_status}")
