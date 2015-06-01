# ************************************************************
# Sequel Pro SQL dump
# Version 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 127.0.0.1 (MySQL 5.6.24)
# Database: beyond
# Generation Time: 2015-05-31 12:44:46 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table team_admin_users
# ------------------------------------------------------------

LOCK TABLES `team_admin_users` WRITE;
/*!40000 ALTER TABLE `team_admin_users` DISABLE KEYS */;

INSERT INTO `team_admin_users` (`id`, `team_id`, `user_name`, `email`, `password`, `del_flg`, `created_at`, `updated_at`)
VALUES
	(1,1,'大佐','g5.philip7322@gmail.com','9761504c58686e574ca644049978101fb5e5d37d',0,'0000-00-00 00:00:00','0000-00-00 00:00:00');

/*!40000 ALTER TABLE `team_admin_users` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table team_game_innings
# ------------------------------------------------------------

LOCK TABLES `team_game_innings` WRITE;
/*!40000 ALTER TABLE `team_game_innings` DISABLE KEYS */;

INSERT INTO `team_game_innings` (`id`, `team_game_id`, `inning`, `del_flg`, `created_at`, `updated_at`)
VALUES
	(1,1,1,0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(2,1,2,0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(3,1,3,0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(4,1,4,0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(5,1,5,0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(6,1,6,0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(7,1,7,0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(8,1,8,0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(9,1,9,0,'0000-00-00 00:00:00','0000-00-00 00:00:00');

/*!40000 ALTER TABLE `team_game_innings` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table team_game_player_scores
# ------------------------------------------------------------

LOCK TABLES `team_game_player_scores` WRITE;
/*!40000 ALTER TABLE `team_game_player_scores` DISABLE KEYS */;

INSERT INTO `team_game_player_scores` (`id`, `team_game_inning_id`, `team_game_player_id`, `status`, `out_flg`, `del_flg`, `created_at`, `updated_at`)
VALUES
	(1,1,1,0,0,0,'1970-01-01 00:00:00','1970-01-01 00:00:00'),
	(2,1,2,0,1,0,'1970-01-01 00:00:00','1970-01-01 00:00:00'),
	(3,1,3,0,1,0,'1970-01-01 00:00:00','1970-01-01 00:00:00'),
	(4,1,4,0,1,0,'1970-01-01 00:00:00','1970-01-01 00:00:00');

/*!40000 ALTER TABLE `team_game_player_scores` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table team_game_players
# ------------------------------------------------------------

LOCK TABLES `team_game_players` WRITE;
/*!40000 ALTER TABLE `team_game_players` DISABLE KEYS */;

INSERT INTO `team_game_players` (`id`, `team_game_id`, `team_player_id`, `stolen_base_count`, `del_flg`, `created_at`, `updated_at`)
VALUES
	(1,1,1,0,0,'1970-01-01 00:00:00','1970-01-01 00:00:00'),
	(2,1,2,0,0,'1970-01-01 00:00:00','1970-01-01 00:00:00'),
	(3,1,3,0,0,'1970-01-01 00:00:00','1970-01-01 00:00:00'),
	(4,1,4,0,0,'1970-01-01 00:00:00','1970-01-01 00:00:00'),
	(8,1,5,0,0,'1970-01-01 00:00:00','1970-01-01 00:00:00'),
	(9,1,6,0,0,'1970-01-01 00:00:00','1970-01-01 00:00:00'),
	(11,1,7,0,0,'1970-01-01 00:00:00','1970-01-01 00:00:00'),
	(12,1,8,0,0,'1970-01-01 00:00:00','1970-01-01 00:00:00'),
	(13,1,9,0,0,'1970-01-01 00:00:00','1970-01-01 00:00:00');

/*!40000 ALTER TABLE `team_game_players` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table team_game_second_half_scores
# ------------------------------------------------------------

LOCK TABLES `team_game_second_half_scores` WRITE;
/*!40000 ALTER TABLE `team_game_second_half_scores` DISABLE KEYS */;

INSERT INTO `team_game_second_half_scores` (`id`, `team_game_id`, `team_game_inning`, `score`, `del_flg`, `created_at`, `updated_at`)
VALUES
	(1,1,1,1,0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(2,1,2,0,0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(3,1,3,0,0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(4,1,4,0,0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(5,1,5,0,0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(6,1,6,0,0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(7,1,7,0,0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(8,1,8,0,0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(9,1,9,1,0,'0000-00-00 00:00:00','0000-00-00 00:00:00');

/*!40000 ALTER TABLE `team_game_second_half_scores` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table team_game_first_half_scores
# ------------------------------------------------------------

LOCK TABLES `team_game_first_half_scores` WRITE;
/*!40000 ALTER TABLE `team_game_first_half_scores` DISABLE KEYS */;

INSERT INTO `team_game_first_half_scores` (`id`, `team_game_id`, `team_game_inning`, `score`, `created_at`, `updated_at`)
VALUES
	(1,1,1,0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(2,1,2,0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(4,1,3,0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(5,1,4,5,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(6,1,5,2,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(7,1,6,3,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(8,1,7,1,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(9,1,8,4,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(10,1,9,0,'0000-00-00 00:00:00','0000-00-00 00:00:00');

/*!40000 ALTER TABLE `team_game_first_half_scores` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table team_games
# ------------------------------------------------------------

LOCK TABLES `team_games` WRITE;
/*!40000 ALTER TABLE `team_games` DISABLE KEYS */;

INSERT INTO `team_games` (`id`, `team_id`, `game_date`, `first_half_team_name`, `second_half_team_name`, `del_flg`, `created_at`, `updated_at`)
VALUES
	(1,1,'2015-06-12 00:00:00','ソウルズ','ジェンキンス',0,'1970-01-01 00:00:00','1970-01-01 00:00:00');

/*!40000 ALTER TABLE `team_games` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table team_players
# ------------------------------------------------------------

LOCK TABLES `team_players` WRITE;
/*!40000 ALTER TABLE `team_players` DISABLE KEYS */;

INSERT INTO `team_players` (`id`, `team_id`, `player_name`, `del_flg`, `created_at`, `updated_at`)
VALUES
	(1,1,'辻',0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(2,1,'大佐',0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(3,1,'ともちん',0,'0000-00-00 00:00:00','0000-00-00 00:00:00'),
	(4,1,'A',0,'1970-01-01 00:00:00','1970-01-01 00:00:00'),
	(5,1,'B',0,'1970-01-01 00:00:00','1970-01-01 00:00:00'),
	(6,1,'C',0,'1970-01-01 00:00:00','1970-01-01 00:00:00'),
	(7,1,'D',0,'1970-01-01 00:00:00','1970-01-01 00:00:00'),
	(8,1,'E',0,'1970-01-01 00:00:00','1970-01-01 00:00:00'),
	(9,1,'F',0,'1970-01-01 00:00:00','1970-01-01 00:00:00');

/*!40000 ALTER TABLE `team_players` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table teams
# ------------------------------------------------------------

LOCK TABLES `teams` WRITE;
/*!40000 ALTER TABLE `teams` DISABLE KEYS */;

INSERT INTO `teams` (`id`, `team_name`, `del_flg`, `created_at`, `updated_at`)
VALUES
	(1,'アライドアーキテクツ',0,'0000-00-00 00:00:00','0000-00-00 00:00:00');

/*!40000 ALTER TABLE `teams` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
