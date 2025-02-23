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
-- Table structure for table `tipo_producto`
--

DROP TABLE IF EXISTS `tipo_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_producto` (
  `sku` varchar(50) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `fecha_modificacion` datetime DEFAULT NULL,
  `responsable` varchar(255) DEFAULT NULL,
  `descripcion` text,
  PRIMARY KEY (`sku`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_producto`
--

LOCK TABLES `tipo_producto` WRITE;
/*!40000 ALTER TABLE `tipo_producto` DISABLE KEYS */;
INSERT INTO `tipo_producto` VALUES ('ACC-1','Fertilizante ACME','2023-11-27 00:59:55','ngaray@utem.cl','Funciona... A veces'),('ACC-2','Insecticida','2023-11-27 01:00:33','ngaray@utem.cl','Pium Pium'),('ACC-3','Tierra','2023-11-27 01:00:48','ngaray@utem.cl','saco de 25kg'),('DEC-1','Durmiente','2023-11-27 01:01:18','ngaray@utem.cl','ZZzZZZzzzz'),('DEC-2','Farolito','2023-11-27 01:01:45','ngaray@utem.cl','Luz pequeña enterrable'),('DEC-3','Piedra Decorativa','2023-11-27 01:02:11','ngaray@utem.cl','Pack de 5 piedras de 15cm'),('PLT-1','Bugambilia','2023-11-27 00:58:25','ngaray@utem.cl','Arbusto de flor fucsia'),('PLT-2','Violeta de Persia','2023-11-27 00:58:46','ngaray@utem.cl','Flor de temporada '),('PLT-3','Bignonia','2023-11-27 00:59:04','ngaray@utem.cl','Arbusto big'),('PLT-4','Pitosporum','2023-11-27 00:59:34','ngaray@utem.cl','Arbusto robusto');
/*!40000 ALTER TABLE `tipo_producto` ENABLE KEYS */;
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
