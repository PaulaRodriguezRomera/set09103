-- Drop the 'albums' table if it exists
DROP TABLE IF EXISTS albums;

-- Create the 'albums' table
CREATE TABLE albums (
    title text,
    artist text,
    media_type text
);
