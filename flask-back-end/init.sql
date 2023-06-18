CREATE DATABASE  IF NOT EXISTS `ecommerce` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ecommerce`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: ecommerce
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `cart_item`
--

DROP TABLE IF EXISTS `cart_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart_item` (
  `member_id` int NOT NULL,
  `market_id` int NOT NULL,
  `product_id` int NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`member_id`,`market_id`,`product_id`),
  KEY `market_id` (`market_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `cart_item_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `cart_item_ibfk_2` FOREIGN KEY (`market_id`) REFERENCES `market` (`market_id`),
  CONSTRAINT `cart_item_ibfk_3` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart_item`
--

LOCK TABLES `cart_item` WRITE;
/*!40000 ALTER TABLE `cart_item` DISABLE KEYS */;
INSERT INTO `cart_item` VALUES (5,1,2,1),(5,4,15,1),(5,5,16,1),(7,2,9,1),(7,5,16,1);
/*!40000 ALTER TABLE `cart_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `market`
--

DROP TABLE IF EXISTS `market`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `market` (
  `market_id` int NOT NULL AUTO_INCREMENT,
  `market_name` varchar(20) NOT NULL,
  `user_id` int NOT NULL,
  `registered_on` datetime NOT NULL,
  PRIMARY KEY (`market_id`),
  UNIQUE KEY `market_name` (`market_name`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `market_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `market`
--

LOCK TABLES `market` WRITE;
/*!40000 ALTER TABLE `market` DISABLE KEYS */;
INSERT INTO `market` VALUES (1,'Joanna\'s Bookstore',1,'2023-06-16 15:34:40'),(2,'Dr.Ian',2,'2023-06-16 15:55:13'),(3,'Daphne\'s store',3,'2023-06-16 16:04:45'),(4,'Beauty',4,'2023-06-16 16:08:07'),(5,'Candy Candy',6,'2023-06-16 16:41:37'),(6,'test4',9,'2023-06-16 20:20:48');
/*!40000 ALTER TABLE `market` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_table`
--

DROP TABLE IF EXISTS `order_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_table` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `member_id` int NOT NULL,
  `market_id` int NOT NULL,
  `state` varchar(10) NOT NULL,
  `create_time` datetime NOT NULL,
  `shipping_address` varchar(100) NOT NULL,
  `consignee` varchar(20) NOT NULL,
  `payment_method` varchar(50) NOT NULL,
  `mode_of_transport` varchar(50) NOT NULL,
  `items` varchar(100) NOT NULL,
  `quantities` varchar(100) NOT NULL,
  `cashs` varchar(100) NOT NULL,
  `cost` int NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `member_id` (`member_id`),
  KEY `market_id` (`market_id`),
  CONSTRAINT `order_table_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `order_table_ibfk_2` FOREIGN KEY (`market_id`) REFERENCES `market` (`market_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_table`
--

LOCK TABLES `order_table` WRITE;
/*!40000 ALTER TABLE `order_table` DISABLE KEYS */;
INSERT INTO `order_table` VALUES (3,5,3,'已完成','2023-06-16 16:25:26','qewqrqwr','ccc','VISA','711','A9+濕拖無線吸塵器A9N-LITEMOP(銀)','1','9999',9999),(4,5,1,'已完成','2023-06-16 16:53:05','ㄐasdeqe','tp6','VISA','711','躲在蚊子後面的大象：那些隱藏在生活小事背後的深層情緒','8','1864',1864),(5,7,1,'已完成','2023-06-16 17:08:48','asgvazdh','adawe','VISA','711','這世界很煩，但你要很可愛2','3','900',900),(6,7,3,'已完成','2023-06-16 17:09:35','adad','zzz','VISA','711','Digital Slim Fluffy Extra SV18 輕量無線吸塵器','1','13818',13818),(7,5,1,'已完成','2023-06-16 17:12:27','n','nnn','VISA','711','這世界很煩，但你要很可愛2,原子習慣：細微改變帶來巨大成就的實證法則','1,1','300,260',560),(9,5,4,'配送中','2023-06-16 17:21:20','n','nnn','VISA','711','無極限超時輕粉底35ml ,新客入門首選經典青春露新客組','4,1','7600,2631',10231),(10,7,3,'配送中','2023-06-16 17:28:20','台北市文山區指南路二段64號','陳小姐','VISA','711','Digital Slim Fluffy Extra SV18 輕量無線吸塵器,A9+濕拖無線吸塵器A9N-LITEMOP(銀)','1,1','13818,9999',23817),(11,8,1,'已完成','2023-06-16 17:48:44','台北市文山區指南路二段64號','王先生','CASH','全家','這世界很煩，但你要很可愛2','4','1200',1200),(13,8,1,'已完成','2023-06-16 17:55:41','台北市文山區指南路二段64號','李先生','VISA','711','有錢人想的和你不一樣','1','197',197),(14,8,1,'已完成','2023-06-16 18:54:56','台北市文山區指南路二段64號','李先生','CASH','全家','躲在蚊子後面的大象,Die with Zero','1,1','233,525',758),(16,8,6,'已完成','2023-06-16 20:23:29','台北市文山區指南路二段','王先生','VISA','711','衛生紙','1','139',139),(17,8,1,'已完成','2023-06-16 20:25:59','sadasf','李小姐','VISA','711','這世界很煩，但你要很可愛2','1','300',300);
/*!40000 ALTER TABLE `order_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(100) NOT NULL,
  `category` varchar(20) NOT NULL,
  `brand` varchar(20) NOT NULL,
  `price` int NOT NULL,
  `stock` int NOT NULL,
  `status` tinyint(1) NOT NULL,
  `market_id` int NOT NULL,
  PRIMARY KEY (`product_id`),
  UNIQUE KEY `product_name` (`product_name`),
  KEY `market_id` (`market_id`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`market_id`) REFERENCES `market` (`market_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'這世界很煩，但你要很可愛2','書籍及雜誌期刊','幸福文化',300,2,0,1),(2,'原子習慣','書籍及雜誌期刊','方智',260,13,0,1),(3,'躲在蚊子後面的大象','書籍及雜誌期刊','平安文化',233,4,0,1),(4,'全新！新制多益TOEIC聽力／閱讀題庫解析','書籍及雜誌期刊','國際學村',1161,3,0,1),(5,'有錢人想的和你不一樣','書籍及雜誌期刊','大塊文化',197,14,0,1),(6,'富爸爸，窮爸爸','書籍及雜誌期刊','高寶',331,9,1,1),(7,'Die with Zero','書籍及雜誌期刊','Mariner Books',525,1,0,1),(8,'視易適葉黃素2入組(30粒/組)','美妝保健','大研生醫',1888,20,0,2),(9,'蜜露珂娜膠原蛋白2盒+15包(共75包)','美妝保健','Suntory',3818,7,0,2),(10,'六入御燕禮盒','美妝保健','老行家',1980,15,0,2),(11,'蜂王乳+芝麻明E+10日份','美妝保健','Suntory',2418,9,0,2),(12,'Digital Slim Fluffy Extra SV18 輕量無線吸塵器','居家生活','Dyson',13818,4,0,3),(13,'A9+濕拖無線吸塵器A9N-LITEMOP(銀)','居家生活','LG',9999,1,0,3),(14,'無極限超時輕粉底35ml ','美妝保健','植村秀',1900,9,0,4),(15,'新客入門首選經典青春露新客組','美妝保健','SK-II',2631,24,0,4),(16,'乖乖QQ 水果軟糖量販包','美食伴手禮','乖乖',85,100,0,5),(17,'衛生紙','居家生活','五月花',139,9,0,6);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(20) NOT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `registered_on` datetime NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Joanna','joanna@gmail.com','123456','dfcadgvs','0123456789','2023-06-16 15:33:31'),(2,'Ian','ian@gmail.com','123456','sdfsmak','0123456789','2023-06-16 15:54:21'),(3,'Daphne','daphne@gmail.com','123456','aegnaloewmo','0123456789','2023-06-16 16:00:23'),(4,'Kevin','kevin@gmail.com','123456','asdnamqarq','0123456789','2023-06-16 16:07:43'),(5,'test1','test1@gmail.com','123456','asdakgaeg','0123456789','2023-06-16 16:15:43'),(6,'candy','candy@gmail.com','123456','mkmkmkmk','0123456789','2023-06-16 16:36:34'),(7,'test2','test2@gmail.com','123456','adnwkjngjea','0123456789','2023-06-16 17:07:18'),(8,'test3@gmail.com','test3@gmail.com','123456','台北市文山區指南路二段6號','0123456789','2023-06-16 17:40:05'),(9,'test4','test4@gmail.com','123456','asdagfsa','0123456789','2023-06-16 20:20:23');
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

-- Dump completed on 2023-06-18 23:00:01
