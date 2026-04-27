This project focuses on designing and implementing a relational database system for managing medical imaging equipment parts in a radiology and imaging laboratory. The system is built to support the storage, organization, and analysis of information related to medical device components, manufacturers, clients, and service offers.

The database includes several interconnected tables:

- Parts table (tblPiese) – stores information about imaging equipment components such as name, code, price, and available quantity.
- Manufacturer table (tblProducatori)– contains details about companies that produce and supply the parts, including contact information and the associated parts they provide.
- Client table (tblClienti) – records data about customers who report issues or request services, including personal details and the type of problem reported.
- Offer table (tblOfertare) – manages service offers, linking clients, manufacturers, and parts, while also storing pricing and time-related information.
<img width="911" height="755" alt="image" src="https://github.com/user-attachments/assets/5a95dd47-9ab6-49f2-bfce-88302dc272fd" />

The project is implemented using SQLite for database creation and SQL queries, and Python (sqlite3 library) for database interaction and automation.

**Key Functionalities**

The system supports:

- Creating and managing relational tables with primary and foreign keys
- Inserting and retrieving data using SQL queries
- Joining multiple tables to extract meaningful information (e.g., linking parts with manufacturers or clients with service requests)
- Performing statistical analysis such as calculating average or total costs of offers
- Ensuring data integrity through constraints and relational rules
- Automation Features

Two automated behaviors were implemented using Python:

- When a new part is added, a default manufacturer entry is automatically created.
- When a manufacturer is deleted, all related parts are also removed to maintain database consistency.
  
**Additional Contributions**

The project also includes personal enhancements such as:

- Exporting database tables into CSV files for external analysis and reporting
- Visualizing data using charts (e.g., part quantities) to better understand usage and demand trends
  
**Purpose**
The main goal of the system is to support technicians, commercial staff, and manufacturers by providing a centralized and efficient way to manage medical equipment parts, track service requests, and analyze operational data in a structured and automated environment.

