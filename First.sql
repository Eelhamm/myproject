-- Create a new table called 'book' in schema 'search'
-- Drop the table if it already exists
IF OBJECT_ID('search.book', 'U') IS NOT NULL
DROP TABLE search.book
GO
-- Create the table in the specified schema
CREATE TABLE search.book
(
    bookId INT NOT NULL PRIMARY KEY, -- primary key column
    Column1 [NVARCHAR](50) NOT NULL,
    Column2 [NVARCHAR](50) NOT NULL
    -- specify more columns here
);
GO