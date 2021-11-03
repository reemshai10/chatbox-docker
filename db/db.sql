CREATE DATABASE mydb;
CREATE TABLE `mydb`.`chat`(
    `room` INT,
    `user` CHAR(20) NOT NULL,
    `msg` CHAR(20) NOT NULL,
    `time` DATETIME,
    PRIMARY KEY (`room`));
 