CREATE TABLE IF NOT EXISTS Users (
	id int(11) AUTO_INCREMENT,
	username varchar(255) NOT NULL,
	livello int NOT NULL,
	score int NOT NULL,
	tempo time NOT NULL,
	PRIMARY KEY (id)
);