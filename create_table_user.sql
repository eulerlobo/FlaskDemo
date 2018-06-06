CREATE TABLE IF NOT EXISTS BucketList.user (
    user_id BIGINT NOT NULL AUTO_INCREMENT,
    user_name VARCHAR(45) NOT NULL,
    user_username VARCHAR(45) NOT NULL,
    user_password VARCHAR(45) NOT NULL,

    CONSTRAINT PK_USER PRIMARY KEY (user_id),
    CONSTRAINT UC_USERNAME UNIQUE (user_username)
)