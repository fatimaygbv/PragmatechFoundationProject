CREATE TABLE Posts(
    id INTEGER PRIMARY KEY,
    Post_cover_url VARCHAR(50),
    Post_title VARCHAR(250),
    Post_author VARCHAR(100),
    Post_date DATE,
    Post_read_min TIME,
    Post_description TEXT,
    Post_content TEXT,
    Post_img_url VARCHAR(250),
    FOREIGN KEY (Post_author)
    REFERENCES Authors(id)
)