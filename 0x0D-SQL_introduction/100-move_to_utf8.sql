-- converts database, table and field from utf8mb4 to utf8mb4_unicode

ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8 COLLATE = utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0.`first_table` CONVERT TO CHARACTER SET utf8 COLLATE utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0.`first_table` CHANGE name name VARCHAR(256) CHARACTER SET utf8 COLLATE utf8mb4_unicode_ci;
