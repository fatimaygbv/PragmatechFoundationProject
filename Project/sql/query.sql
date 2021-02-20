CREATE TABLE Post_tag(
    id INTEGER PRIMARY KEY,
    Post_id INTEGER,
    Tag_id INTEGER,
    FOREIGN KEY (Post_id)
    REFERENCES Posts(id)
    FOREIGN KEY (Tag_id)
    REFERENCES Tag(id)
)
SELECT * FROM Post_tag