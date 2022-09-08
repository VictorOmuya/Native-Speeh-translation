-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Nov 04, 2021 at 04:37 PM
-- Server version: 5.6.21
-- PHP Version: 5.6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `pythonlogin`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE IF NOT EXISTS `account` (
`id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`id`, `username`, `password`, `email`) VALUES
(1, 'faq', 'faqpass', 'faqpass@yahoo.com'),
(2, 'ayo', 'ayopass', 'ayo@yahoo.com'),
(3, 'tola', 'tolapass', 'ayo@yahoo.com'),
(4, 'bolanle', 'owosun', 'vic@yahoo.com');

-- --------------------------------------------------------

--
-- Table structure for table `emr`
--

CREATE TABLE IF NOT EXISTS `emr` (
  `username` varchar(20) NOT NULL,
  `age` int(11) NOT NULL,
  `medical_condition` varchar(40) NOT NULL,
  `drug_prescription` varchar(50) NOT NULL,
  `date` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `emr`
--

INSERT INTO `emr` (`username`, `age`, `medical_condition`, `drug_prescription`, `date`) VALUES
('bolanle', 21, 'none', 'none', ''),
('lolade', 12, 'headache', 'paracetamol', '<class ''datetim'),
('kola', 23, 'headache', 'panadol', '2021-11-04');

-- --------------------------------------------------------

--
-- Table structure for table `records`
--

CREATE TABLE IF NOT EXISTS `records` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `words` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `records`
--

INSERT INTO `records` (`id`, `username`, `words`) VALUES
(4, 'bolanle', 'Enter Text for translation'),
(4, 'bolanle', 'what did you want me to do?'),
(4, 'bolanle', 'you need to see what that boy did to him'),
(4, 'bolanle', 'moso  fun e lanna wipe mo feran re'),
(4, 'bolanle', 'Enter Text for translation: ');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
 ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=5;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
