import mysql.connector


def initialize():
    """
    This function initializes the database and table.
    """
    # Create a connection to the MySQL server
    create = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="936700"
    )

    create_cursor = create.cursor()

    # Create a database if it doesn't exist
    create_cursor.execute("CREATE DATABASE IF NOT EXISTS DB")

    # Show all databases
    create_cursor.execute("SHOW DATABASES")

    # Connect to the newly created database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="936700",
        database="DB"
    )

    db_cursor = db.cursor()
    
    # Reset the table
    db_cursor.execute("DROP TABLE IF EXISTS list")

    db_cursor.execute("""
                    CREATE TABLE IF NOT EXISTS list (
                    id INT, 
                    name VARCHAR(100), 
                    type VARCHAR(100), 
                    sector VARCHAR(100), 
                    resources TEXT,
                    individual VARCHAR(100),
                    email VARCHAR(100),
                    phone VARCHAR(100),
                    address VARCHAR(100),
                    date DATE
                    )
                    """)

    # Check if the table is empty
    db_cursor.execute("SELECT COUNT(*) FROM list")

    # If the table is empty, insert some data
    if db_cursor.fetchone()[0] == 0:
        # SQL query to insert data into the list table
        sql = "INSERT INTO list (id, name, type, sector, resources, individual, email, phone, address, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        # Data to be inserted into the list table
        data = [
            (1, 'ABC Tech Solutions', 'Business', 'Technology', 'IT consulting, mentorship', 'John Doe', 'john.doe@abctech.com', '559-111-1111', '123 Main St', '2023-01-01'),
            (2, 'Community Health Clinic', 'Community', 'Healthcare', 'Health education programs', 'Jane Smith', 'jane.smith@healthclinic.org', '559-111-1123', '456 Oak Ave', '2023-02-15'),
            (3, 'Green Energy Co-op', 'Business', 'Energy', 'Renewable energy resources', 'Sam Green', 'sam.green@greenenergycoop.com', '559-111-1135', '789 Pine Rd', '2023-03-20'),
            (4, 'Local Arts Foundation', 'Community', 'Arts', 'Art exhibitions, workshops', 'Alex Turner', 'alex.turner@artsfoundation.org', '559-111-1147', '321 Elm St', '2023-04-10'),
            (5, 'XYZ Manufacturing', 'Business', 'Manufacturing', 'Internship programs, factory tours', 'Maria Rodriguez', 'maria.rodriguez@xyzmanufacturing.com', '559-111-1159', '987 Steel Blvd', '2023-05-05'),
            (6, 'Youth Mentorship Alliance', 'Community', 'Education', 'Mentorship programs for students', 'Carlos Gonzalez', 'carlos.gonzalez@youthalliance.org', '559-111-1171', '654 Maple Ln', '2023-06-18'),
            (7, 'Financial Literacy Institute', 'Business', 'Finance', 'Financial education workshops', 'Emily Johnson', 'emily.johnson@financeliteracy.org', '559-111-1183', '876 Oak Ridge', '2023-07-12'),
            (8, 'Local Environmental Group', 'Community', 'Environment', 'Environmental cleanup events', 'Chris Anderson', 'chris.anderson@envirogroup.net', '559-111-1195', '543 Pine Ave', '2023-08-25'),
            (9, 'Global Food Bank', 'Business', 'Non-profit', 'Food donations, volunteer opportunities', 'Sophia Lee', 'sophia.lee@globalfoodbank.org', '559-111-1207', '234 Walnut St', '2023-09-30'),
            (10, 'Small Business Network', 'Community', 'Entrepreneurship', 'Business development workshops', 'Michael Brown', 'michael.brown@smallbiznetwork.com', '559-111-1219', '789 Birch Rd', '2023-10-05'),
            (11, 'ABC Tech Innovations', 'Business', 'Technology', 'Innovative solutions, technology consulting', 'Alice Johnson', 'alice.johnson@abctech.com', '559-111-1231', '456 Tech Lane', '2023-11-11'),
            (12, 'Community Health Foundation', 'Community', 'Healthcare', 'Health initiatives and community programs', 'Robert Miller', 'robert.miller@healthfoundation.org', '559-111-1243', '987 Health Blvd', '2023-12-12'),
            (13, 'Green Energy Innovators', 'Business', 'Energy', 'Cutting-edge renewable energy projects', 'Eva Green', 'eva.green@greenenergyinnovators.com', '559-111-1255', '123 Wind Rd', '2024-01-15'),
            (14, 'Local Arts Collective', 'Community', 'Arts', 'Collaborative art projects and exhibitions', 'Olivia Turner', 'olivia.turner@artscollective.org', '559-111-1267', '321 Gallery St', '2024-02-20'),
            (15, 'XYZ Manufacturing Solutions', 'Business', 'Manufacturing', 'Efficient manufacturing processes and solutions', 'Carlos Rodriguez', 'carlos.rodriguez@xyzmanufacturing.com', '559-111-1279', '654 Steel Ave', '2024-03-25'),
            (16, 'Youth Empowerment Alliance', 'Community', 'Education', 'Empowering youth through education programs', 'Isabella Gonzalez', 'isabella.gonzalez@youthalliance.org', '559-111-1291', '876 Education Ln', '2024-04-30'),
            (17, 'Financial Literacy Center', 'Business', 'Finance', 'Comprehensive financial literacy programs', 'Daniel Johnson', 'daniel.johnson@financeliteracy.org', '559-111-1303', '543 Finance Ave', '2024-05-05'),
            (18, 'Local Environmental Conservation', 'Community', 'Environment', 'Conserving local ecosystems and habitats', 'Sophie Anderson', 'sophie.anderson@enviroconservation.net', '559-111-1315', '789 Conservation Rd', '2024-06-10'),
            (19, 'Global Food Assistance', 'Business', 'Non-profit', 'Providing food assistance globally', 'Noah Lee', 'noah.lee@globalfoodassistance.org', '559-111-1327', '234 Assistance St', '2024-07-15'),
            (20, 'Small Business Hub', 'Community', 'Entrepreneurship', 'Supporting small businesses and entrepreneurship', 'Emma Brown', 'emma.brown@smallbizhub.com', '559-111-1339', '789 Hub Rd', '2024-08-20'),
            (21, 'Tech Innovations XYZ', 'Business', 'Technology', 'Cutting-edge innovations in technology', 'Alice Smith', 'alice.smith@techinnovationsxyz.com', '559-111-1351', '456 Innovate Lane', '2024-09-25'),
            (22, 'Community Health Initiatives XYZ', 'Community', 'Healthcare', 'Community-driven health initiatives', 'Robert Johnson', 'robert.johnson@healthinitiativesxyz.org', '559-111-1363', '987 Initiatives Blvd', '2024-10-30'),
            (23, 'Green Energy Pioneers', 'Business', 'Energy', 'Pioneering sustainable energy solutions', 'Eva Rodriguez', 'eva.rodriguez@greenenergypioneers.com', '559-111-1375', '123 Pioneer Rd', '2024-11-15'),
            (24, 'Local Arts Guild', 'Community', 'Arts', 'Supporting local artists and creative projects', 'Oliver Turner', 'oliver.turner@artsguild.org', '559-111-1387', '321 Artistic St', '2024-12-20'),
            (25, 'XYZ Manufacturing Innovations', 'Business', 'Manufacturing', 'Innovative manufacturing practices', 'Maria Rodriguez', 'maria.rodriguez@xyzmanufacturinginnovations.com', '559-111-1399', '654 Innovation Ave', '2025-01-25'),
            (26, 'Youth Empowerment Network', 'Community', 'Education', 'Connecting youth with empowerment resources', 'Isaac Gonzalez', 'isaac.gonzalez@youthempowernetwork.org', '559-111-1411', '876 Empower Ln', '2025-02-28'),
            (27, 'Financial Literacy Institute XYZ', 'Business', 'Finance', 'Advanced financial literacy education', 'Danielle Johnson', 'danielle.johnson@financeliteracyinstitutexyz.org', '559-111-1423', '543 Financial Ave', '2025-03-15'),
            (28, 'Local Environmental Stewards', 'Community', 'Environment', 'Stewardship for local environmental conservation', 'Sophia Turner', 'sophia.turner@envirostewards.net', '559-111-1435', '789 Steward Rd', '2025-04-20'),
            (29, 'Green Initiative Collective', 'Community', 'Environment', 'Promoting green initiatives and sustainability', 'Jacob Green', 'jacob.green@greeninitiativecollective.org', '559-111-1447', '456 Eco Lane', '2025-05-25'),
            (30, 'Tech Innovate Solutions', 'Business', 'Technology', 'Innovative solutions for tech advancement', 'Lily Tech', 'lily.tech@techinnovatesolutions.com', '559-111-1459', '654 Tech Blvd', '2025-06-30')
                ]
    db_cursor.executemany(sql, data)
    db.commit()
    # Print the rows to check if the rows are properly in place
    db_cursor.execute("SELECT * FROM list")
    lists=db_cursor.fetchall()
    for i in lists:
        print(i)
    return  


def main():
    initialize()
    
if __name__ == "__main__":
    main()