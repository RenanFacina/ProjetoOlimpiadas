-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: olimpiadasdatabase
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
-- Table structure for table `analise`
--

DROP TABLE IF EXISTS `analise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analise` (
  `id_analise` int NOT NULL AUTO_INCREMENT,
  `nome_analise` varchar(50) NOT NULL,
  `bra_part_v` int DEFAULT NULL COMMENT 'Participações do Brasil no Verão',
  `bra_ouro_v` int DEFAULT NULL COMMENT 'Medalhas de ouro do Brasil no Verão',
  `bra_bronze_v` int DEFAULT NULL COMMENT 'Medalhas de Bronze do Brasil no Verão',
  `bra_part_i` int DEFAULT NULL COMMENT 'Participações do Brasil no Inverno',
  `bra_ouro_i` int DEFAULT NULL COMMENT 'Medalhas de ouro do Brasil no Inverno',
  `bra_bronze_i` int DEFAULT NULL COMMENT 'Medalhas de Bronze do Brasil no Inverno',
  `pais_max_ouro_v` varchar(50) DEFAULT NULL COMMENT 'País que possui mais medalhas de ouro no Verão',
  `max_medalhas_ouro_v` int DEFAULT NULL COMMENT 'Número de medalhas de ouro do país no Verão',
  `pais_max_prata_v` varchar(50) DEFAULT NULL COMMENT 'País que possui mais medalhas de prata no Verão',
  `max_medalhas_prata_v` int DEFAULT NULL COMMENT 'Número de medalhas de prata do país no Verão',
  `pais_max_bronze_v` varchar(50) DEFAULT NULL COMMENT 'País que possui mais medalhas de bronze no Verão',
  `max_medalhas_bronze_v` int DEFAULT NULL COMMENT 'Número de medalhas de bronze do país no Verão',
  `pais_com_mais_participacao_v` varchar(50) DEFAULT NULL,
  `pais_com_mais_participacao_i` varchar(50) DEFAULT NULL,
  `pais_com_mais_participacao` varchar(50) DEFAULT NULL,
  `pais_com_menos_participacao` varchar(50) DEFAULT NULL,
  `nunca_ganharam_ouro` int DEFAULT NULL COMMENT 'Quantidade de paises que nunca ganharam medalhas de ouro',
  `nunca_ganharam_prata` int DEFAULT NULL COMMENT 'Quantidade de paises que nunca ganharam medalhas de prata',
  `nunca_ganharam_bronze` int DEFAULT NULL COMMENT 'Quantidade de paises que nunca ganharam medalhas de bronze',
  PRIMARY KEY (`id_analise`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `analise`
--

LOCK TABLES `analise` WRITE;
/*!40000 ALTER TABLE `analise` DISABLE KEYS */;
INSERT INTO `analise` VALUES (1,'Olimpiadas',23,37,71,9,0,0,'United States',1060,'United States',831,'United States',738,'France','Austria','France','British West Indies',41,19,21);
/*!40000 ALTER TABLE `analise` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-07 15:53:30
