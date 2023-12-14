-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: jardineria
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `movimiento`
--

DROP TABLE IF EXISTS `movimiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movimiento` (
  `sku` varchar(50) NOT NULL,
  `fecha` datetime DEFAULT NULL,
  `cantidad` int NOT NULL DEFAULT '0',
  `razon` varchar(50) NOT NULL DEFAULT ' ',
  `fecha_modificacion` datetime DEFAULT NULL,
  `responsable` varchar(255) DEFAULT NULL,
  `ubicacion` int DEFAULT NULL,
  KEY `sku` (`sku`),
  CONSTRAINT `movimiento_ibfk_1` FOREIGN KEY (`sku`) REFERENCES `tipo_producto` (`sku`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movimiento`
--

LOCK TABLES `movimiento` WRITE;
/*!40000 ALTER TABLE `movimiento` DISABLE KEYS */;
INSERT INTO `movimiento` VALUES ('ACC-1','2023-11-27 01:04:46',10,'Compra','2023-11-27 01:04:46','ngaray@utem.cl',16),('ACC-2','2023-11-27 01:05:03',15,'Compra','2023-11-27 01:05:03','ngaray@utem.cl',14),('ACC-3','2023-11-27 01:05:16',12,'Compra','2023-11-27 01:05:16','ngaray@utem.cl',15),('DEC-1','2023-11-27 01:05:30',8,'Compra','2023-11-27 01:05:30','ngaray@utem.cl',16),('DEC-1','2023-11-27 01:05:37',12,'Compra','2023-11-27 01:05:37','ngaray@utem.cl',16),('DEC-2','2023-11-27 01:05:48',16,'Compra','2023-11-27 01:05:48','ngaray@utem.cl',12),('DEC-3','2023-11-27 01:06:05',6,'Compra','2023-11-27 01:06:05','ngaray@utem.cl',14),('PLT-1','2023-11-27 01:06:17',10,'Compra','2023-11-27 01:06:17','ngaray@utem.cl',13),('PLT-2','2023-11-27 01:06:38',12,'Compra','2023-11-27 01:06:38','ngaray@utem.cl',15),('PLT-3','2023-11-27 01:06:48',14,'Compra','2023-11-27 01:06:48','ngaray@utem.cl',12),('PLT-4','2023-11-27 01:06:59',20,'Compra','2023-11-27 01:06:59','ngaray@utem.cl',12),('ACC-1','2023-11-27 01:07:11',4,'Venta','2023-11-27 01:07:11','ngaray@utem.cl',16),('ACC-1','2023-11-27 01:07:20',6,'Merma','2023-11-27 01:07:20','ngaray@utem.cl',16),('ACC-1','2023-11-27 01:07:28',4,'Repuesto','2023-11-27 01:07:28','ngaray@utem.cl',16),('ACC-1','2023-11-27 01:07:33',2,'Baja','2023-11-27 01:07:33','ngaray@utem.cl',16),('ACC-3','2023-11-27 01:08:04',10,'Venta','2023-11-27 01:08:04','ngaray@utem.cl',15),('DEC-2','2023-11-27 01:08:45',8,'Merma','2023-11-27 01:08:45','ngaray@utem.cl',12),('DEC-2','2023-11-27 01:08:52',4,'Baja','2023-11-27 01:08:52','ngaray@utem.cl',12),('DEC-2','2023-11-27 01:08:56',4,'Repuesto','2023-11-27 01:08:56','ngaray@utem.cl',12),('PLT-2','2023-11-27 01:09:33',10,'Merma','2023-11-27 01:09:33','ngaray@utem.cl',15),('DEC-3','2023-11-27 01:15:07',4,'Venta','2023-11-27 01:15:07','ngaray@utem.cl',14),('PLT-4','2023-11-27 01:15:20',2,'Baja','2023-11-27 01:15:20','ngaray@utem.cl',12);
/*!40000 ALTER TABLE `movimiento` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-27  1:18:26
