DROP TABLE IF EXISTS `animal`.dog;

CREATE TABLE `animal`.dog (
	id INT PRIMARY KEY auto_increment,
	breed varchar(25) NOT NULL,
	color varchar(10) NOT NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;
