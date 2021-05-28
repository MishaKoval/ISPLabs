-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add author',7,'add_author'),(26,'Can change author',7,'change_author'),(27,'Can delete author',7,'delete_author'),(28,'Can view author',7,'view_author'),(29,'Can add book',8,'add_book'),(30,'Can change book',8,'change_book'),(31,'Can delete book',8,'delete_book'),(32,'Can view book',8,'view_book'),(33,'Can add book instance',9,'add_bookinstance'),(34,'Can change book instance',9,'change_bookinstance'),(35,'Can delete book instance',9,'delete_bookinstance'),(36,'Can view book instance',9,'view_bookinstance'),(37,'Set book as returned',9,'can_mark_returned'),(38,'Can add genre',10,'add_genre'),(39,'Can change genre',10,'change_genre'),(40,'Can delete genre',10,'delete_genre'),(41,'Can view genre',10,'view_genre'),(42,'Can add language',11,'add_language'),(43,'Can change language',11,'change_language'),(44,'Can delete language',11,'delete_language'),(45,'Can view language',11,'view_language');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$216000$6t3TwJPpn1LI$zpILYPKujvXSMA5i8QFtQZCDk4XRFOuHyETXcYIRD7U=','2021-05-28 23:09:42.104049',1,'miko','','','ksasha754@gmail.com',1,1,'2021-05-28 22:07:33.817000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `catalog_author`
--

DROP TABLE IF EXISTS `catalog_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `catalog_author` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `date_of_death` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catalog_author`
--

LOCK TABLES `catalog_author` WRITE;
/*!40000 ALTER TABLE `catalog_author` DISABLE KEYS */;
INSERT INTO `catalog_author` VALUES (1,'Stephen','King','1947-09-21',NULL);
/*!40000 ALTER TABLE `catalog_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `catalog_book`
--

DROP TABLE IF EXISTS `catalog_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `catalog_book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `summary` longtext NOT NULL,
  `isbn` varchar(13) NOT NULL,
  `author_id` int DEFAULT NULL,
  `language_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `catalog_book_isbn_30805834_uniq` (`isbn`),
  KEY `catalog_book_author_id_b0849980_fk_catalog_author_id` (`author_id`),
  KEY `catalog_book_language_id_447f859e_fk_catalog_language_id` (`language_id`),
  CONSTRAINT `catalog_book_author_id_b0849980_fk_catalog_author_id` FOREIGN KEY (`author_id`) REFERENCES `catalog_author` (`id`),
  CONSTRAINT `catalog_book_language_id_447f859e_fk_catalog_language_id` FOREIGN KEY (`language_id`) REFERENCES `catalog_language` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catalog_book`
--

LOCK TABLES `catalog_book` WRITE;
/*!40000 ALTER TABLE `catalog_book` DISABLE KEYS */;
INSERT INTO `catalog_book` VALUES (1,'1408','Good book','1111111111111',1,1);
/*!40000 ALTER TABLE `catalog_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `catalog_book_genre`
--

DROP TABLE IF EXISTS `catalog_book_genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `catalog_book_genre` (
  `id` int NOT NULL AUTO_INCREMENT,
  `book_id` int NOT NULL,
  `genre_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `catalog_book_genre_book_id_genre_id_d15f6922_uniq` (`book_id`,`genre_id`),
  KEY `catalog_book_genre_genre_id_77d7ffde_fk_catalog_genre_id` (`genre_id`),
  CONSTRAINT `catalog_book_genre_book_id_e5a77c43_fk_catalog_book_id` FOREIGN KEY (`book_id`) REFERENCES `catalog_book` (`id`),
  CONSTRAINT `catalog_book_genre_genre_id_77d7ffde_fk_catalog_genre_id` FOREIGN KEY (`genre_id`) REFERENCES `catalog_genre` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catalog_book_genre`
--

LOCK TABLES `catalog_book_genre` WRITE;
/*!40000 ALTER TABLE `catalog_book_genre` DISABLE KEYS */;
INSERT INTO `catalog_book_genre` VALUES (1,1,1);
/*!40000 ALTER TABLE `catalog_book_genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `catalog_bookinstance`
--

DROP TABLE IF EXISTS `catalog_bookinstance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `catalog_bookinstance` (
  `id` char(32) NOT NULL,
  `imprint` varchar(200) NOT NULL,
  `due_back` date DEFAULT NULL,
  `status` varchar(1) NOT NULL,
  `book_id` int DEFAULT NULL,
  `borrower_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `catalog_bookinstance_borrower_id_0d71c37c_fk_auth_user_id` (`borrower_id`),
  KEY `catalog_bookinstance_book_id_69f93415_fk_catalog_book_id` (`book_id`),
  CONSTRAINT `catalog_bookinstance_book_id_69f93415_fk_catalog_book_id` FOREIGN KEY (`book_id`) REFERENCES `catalog_book` (`id`),
  CONSTRAINT `catalog_bookinstance_borrower_id_0d71c37c_fk_auth_user_id` FOREIGN KEY (`borrower_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catalog_bookinstance`
--

LOCK TABLES `catalog_bookinstance` WRITE;
/*!40000 ALTER TABLE `catalog_bookinstance` DISABLE KEYS */;
INSERT INTO `catalog_bookinstance` VALUES ('75a8a11c1ed04f8b81b2aafc0c2f9487','20000','2021-05-31','o',1,1);
/*!40000 ALTER TABLE `catalog_bookinstance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `catalog_genre`
--

DROP TABLE IF EXISTS `catalog_genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `catalog_genre` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catalog_genre`
--

LOCK TABLES `catalog_genre` WRITE;
/*!40000 ALTER TABLE `catalog_genre` DISABLE KEYS */;
INSERT INTO `catalog_genre` VALUES (1,'Triller');
/*!40000 ALTER TABLE `catalog_genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `catalog_language`
--

DROP TABLE IF EXISTS `catalog_language`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `catalog_language` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catalog_language`
--

LOCK TABLES `catalog_language` WRITE;
/*!40000 ALTER TABLE `catalog_language` DISABLE KEYS */;
INSERT INTO `catalog_language` VALUES (1,'English');
/*!40000 ALTER TABLE `catalog_language` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-05-28 23:13:19.858178','1','King, Stephen',1,'[{\"added\": {}}]',7,1),(2,'2021-05-28 23:14:14.890271','1','Triller',1,'[{\"added\": {}}]',10,1),(3,'2021-05-28 23:14:24.278924','1','English',1,'[{\"added\": {}}]',11,1),(4,'2021-05-28 23:14:31.734514','1','1408',1,'[{\"added\": {}}]',8,1),(5,'2021-05-28 23:15:25.782594','75a8a11c-1ed0-4f8b-81b2-aafc0c2f9487','75a8a11c-1ed0-4f8b-81b2-aafc0c2f9487 (1408)',1,'[{\"added\": {}}]',9,1),(6,'2021-05-28 23:15:59.845048','75a8a11c-1ed0-4f8b-81b2-aafc0c2f9487','75a8a11c-1ed0-4f8b-81b2-aafc0c2f9487 (1408)',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',9,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'catalog','author'),(8,'catalog','book'),(9,'catalog','bookinstance'),(10,'catalog','genre'),(11,'catalog','language'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-05-28 23:08:42.112344'),(2,'auth','0001_initial','2021-05-28 23:08:42.356495'),(3,'admin','0001_initial','2021-05-28 23:08:43.383109'),(4,'admin','0002_logentry_remove_auto_add','2021-05-28 23:08:43.555009'),(5,'admin','0003_logentry_add_action_flag_choices','2021-05-28 23:08:43.579967'),(6,'contenttypes','0002_remove_content_type_name','2021-05-28 23:08:43.715971'),(7,'auth','0002_alter_permission_name_max_length','2021-05-28 23:08:43.801269'),(8,'auth','0003_alter_user_email_max_length','2021-05-28 23:08:43.891587'),(9,'auth','0004_alter_user_username_opts','2021-05-28 23:08:43.905035'),(10,'auth','0005_alter_user_last_login_null','2021-05-28 23:08:44.002402'),(11,'auth','0006_require_contenttypes_0002','2021-05-28 23:08:44.009537'),(12,'auth','0007_alter_validators_add_error_messages','2021-05-28 23:08:44.027589'),(13,'auth','0008_alter_user_username_max_length','2021-05-28 23:08:44.138493'),(14,'auth','0009_alter_user_last_name_max_length','2021-05-28 23:08:44.225229'),(15,'auth','0010_alter_group_name_max_length','2021-05-28 23:08:44.311861'),(16,'auth','0011_update_proxy_permissions','2021-05-28 23:08:44.330139'),(17,'auth','0012_alter_user_first_name_max_length','2021-05-28 23:08:44.441338'),(18,'catalog','0001_initial','2021-05-28 23:08:44.608665'),(19,'catalog','0002_auto_20160921_1401','2021-05-28 23:08:45.084523'),(20,'catalog','0003_auto_20160921_1420','2021-05-28 23:08:45.174800'),(21,'catalog','0004_auto_20160921_1422','2021-05-28 23:08:45.185202'),(22,'catalog','0005_auto_20160921_1433','2021-05-28 23:08:45.700835'),(23,'catalog','0006_auto_20160921_1439','2021-05-28 23:08:45.774988'),(24,'catalog','0007_auto_20160921_1444','2021-05-28 23:08:45.787914'),(25,'catalog','0008_auto_20160921_1511','2021-05-28 23:08:45.990171'),(26,'catalog','0009_remove_bookinstance_summary','2021-05-28 23:08:46.052698'),(27,'catalog','0010_auto_20160921_1527','2021-05-28 23:08:46.244299'),(28,'catalog','0011_auto_20160922_1029','2021-05-28 23:08:46.357038'),(29,'catalog','0012_bookinstance_date_acquired','2021-05-28 23:08:46.424335'),(30,'catalog','0013_auto_20160926_1901','2021-05-28 23:08:46.434955'),(31,'catalog','0014_remove_bookinstance_date_acquired','2021-05-28 23:08:46.532642'),(32,'catalog','0015_auto_20160927_1808','2021-05-28 23:08:46.633239'),(33,'catalog','0016_auto_20160927_1947','2021-05-28 23:08:46.757616'),(34,'catalog','0017_language','2021-05-28 23:08:46.985130'),(35,'catalog','0018_book_language','2021-05-28 23:08:47.073554'),(36,'catalog','0019_bookinstance_borrower','2021-05-28 23:08:47.188211'),(37,'catalog','0020_auto_20161012_1044','2021-05-28 23:08:47.208923'),(38,'catalog','0021_auto_20171229_1056','2021-05-28 23:08:47.219146'),(39,'catalog','0022_auto_20181028_1731','2021-05-28 23:08:47.233622'),(40,'catalog','0023_auto_20201201_0238','2021-05-28 23:08:47.318930'),(41,'catalog','0024_auto_20210302_0630','2021-05-28 23:08:47.461191'),(42,'sessions','0001_initial','2021-05-28 23:08:47.505163');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('84j4p73ygvvf4ddp60jv3j7b1vltbgei','.eJxVjDsOgzAQBe-ydWTZYGJDmT5nsLy73uB8jIQhTZS7J0g0tG9m3gfK-grvXPNSYehOEOK6jGGtaQ6ZYQADhw0jPVLZAN9juU2KprLMGdWmqJ1WdZ04PS-7ezgYYx3_tfPCybWGHVnx0mhthYzYxhovaLUg99Fhi9hRT51J1HISK70x-uy1h-8Pobc9lg:1lmllE:T2U_iRmpYpg8RWYFbJBdYsANjQuYNG3PGKkwCU3bWP8','2021-06-11 23:19:24.533539');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-29  2:26:01
