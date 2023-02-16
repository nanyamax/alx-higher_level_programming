-- creates a database , table , FK & PK.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities`(
	PRIMARY KEY(`id`),
	`id` INT AUTO_INCREMENT  NOT NULL,
	`state_id` INT NOT NULL,
	FOREIGN KEY(`state_id`)
	REFEERENCES `hbtn_0d_usa`.`states`(`id`)
	`name` VARCHAR(256) NOT NULL
);
