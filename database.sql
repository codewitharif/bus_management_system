CREATE DATABASE  IF NOT EXISTS `bus_booking` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bus_booking`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: bus_booking
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `book_ticket`
--

DROP TABLE IF EXISTS `book_ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_ticket` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `leaving_from` varchar(45) DEFAULT NULL,
  `going_to` varchar(45) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `travelling_with` varchar(45) DEFAULT NULL,
  `bus_type` varchar(45) DEFAULT NULL,
  `bill_rate` varchar(45) DEFAULT NULL,
  `pay_rate` varchar(45) DEFAULT NULL,
  `mop` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_ticket`
--

LOCK TABLES `book_ticket` WRITE;
/*!40000 ALTER TABLE `book_ticket` DISABLE KEYS */;
INSERT INTO `book_ticket` VALUES (1,'vimal','Bokaro','Delhi','2021-01-01','Self','GPS-Enabled Bus','400','400','Online'),(2,'sita','Bokaro','Goa','2021-01-01','Self','General','300','300','Cash'),(3,'Golu','Bokaro','Ahemadabad','2021-01-01','Self','General','300','300','Cash'),(4,'Gita','Bokaro','Bhopal','2021-01-01','Self','Ac-Sleeper','450','450','Cash'),(5,'Shobhit','Bokaro','Kolkata','2021-03-07','Family','Ac-Sleeper','250','250','Cash'),(6,'Mehar','Bokaro','Delhi','2021-03-06','Self','GPS-Enabled Bus','400','400','Online'),(7,'Madhu','Bokaro','Delhi','2021-02-04','Self','GPS-Enabled Bus','400','400','Online'),(8,'Raju','Bokaro','Delhi','2021-03-06','Self','GPS-Enabled Bus','400','400','Online'),(9,'Rahul','Bokaro','Bihar','2021-03-07','Family','Ac-Sleeper','150','150','Online'),(10,'Gaurav','Bokaro','Ranchi','2021-03-07','Self','GPS-Enabled Bus','500','500','Online'),(11,'Raghav','Bokaro ','Punjab','2021-03-07','Friends','General','550','550','Cash'),(12,'Rahim','Bokaro','Haryana','2021-03-10','Friends','Ac-Sleeper','200','200','Cash'),(13,'sajid','Bokaro','Bihar','2021-03-10','Self','General','150','150','Online'),(14,'Sahbaaj','Bokaro','MP','2021-03-10','Self','General','400','400','Online'),(15,'Payal','BOKARO','Gujrat','2021-03-10','Self','General','600','600','Online');
/*!40000 ALTER TABLE `book_ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin','arif123','1234'),(2,'arif','arif653','1234');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-12 17:16:33
