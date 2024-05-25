/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 80027
 Source Host           : localhost:3306
 Source Schema         : IrisRecognition

 Target Server Type    : MySQL
 Target Server Version : 80027
 File Encoding         : 65001

 Date: 25/05/2024 20:00:07
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for ad_Time
-- ----------------------------
DROP TABLE IF EXISTS `ad_Time`;
CREATE TABLE `ad_Time` (
  `ID` varchar(255) DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  `type` int DEFAULT NULL,
  `studentID` varchar(255) DEFAULT NULL,
  `Information` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for administrator
-- ----------------------------
DROP TABLE IF EXISTS `administrator`;
CREATE TABLE `administrator` (
  `ad_account` varchar(255) DEFAULT NULL,
  `ad_password` varchar(255) DEFAULT NULL,
  `ad_IrisPhoto` varchar(255) DEFAULT NULL,
  `ad_Name` varchar(255) DEFAULT NULL,
  `ad_LastTime` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for Time
-- ----------------------------
DROP TABLE IF EXISTS `Time`;
CREATE TABLE `Time` (
  `StudentID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `Time` varchar(255) DEFAULT NULL,
  `InorOut` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `Name` varchar(255) DEFAULT NULL,
  `Gender` varchar(255) DEFAULT NULL,
  `College` varchar(255) DEFAULT NULL,
  `StudentID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `PhoneNumber` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `IrisPhoto` varchar(255) DEFAULT NULL,
  `Password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Status` varchar(255) DEFAULT NULL,
  `LastTime` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

SET FOREIGN_KEY_CHECKS = 1;
