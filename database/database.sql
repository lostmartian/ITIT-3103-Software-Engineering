CREATE TABLE posts (
    post_id INTEGER PRIMARY KEY,
    image_ TEXT,
    user TEXT,
    posted_on TEXT,
    board TEXT NOT NULL,
    post_text
);

CREATE TABLE board (
    board_id INTEGER PRIMARY KEY,
    board_name TEXT NOT NULL UNIQUE,
    board_description TEXT NOT NULL
);

CREATE TABLE reply (
    reply_id INTEGER PRIMARY KEY,
    board TEXT NOT NULL,
    reply_image TEXT,
    user TEXT,
    replied_on TEXT,
    post_text TEXT
);

CREATE TABLE replies (
    image_file TEXT,
    user TEXT,
    replied_on TEXT,
    board TEXT,
    post_text TEXT,
    replying_to TEXT
);