CREATE TABLE admin (
    admin_id INTEGER PRIMARY KEY,
    image_ TEXT,
    user TEXT,
    password TEXT
);  

CREATE TABLE privilege(
    privilege_id INTEGER PRIMARY KEY,
    privilege_name TEXT NOT NULL,
    privilege_description TEXT NOT NULL
);

CREATE TABLE replies (
    image_file TEXT,
    user TEXT,
    replied_on TEXT,
    privilege TEXT,
    post_text TEXT,
    replying_to TEXT
);