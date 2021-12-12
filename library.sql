-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 03, 2020 at 08:44 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `bks_id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `author` varchar(20) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`bks_id`, `name`, `author`, `quantity`) VALUES
(101, 'aliens', 'george bush', 5),
(103, 'the grandfather', 'richard powers', 7),
(104, 'my life my passion', 'Baba ramdev', 10),
(102, 'the new delhi conspi', 'meenakshi lekhi', 13),
(105, 'mind master', 'vishwanathan anand', 26),
(106, 'my journey', 'apj kalam', 11),
(107, 'india of my dreams', 'mahatma gandhi', 12);

-- --------------------------------------------------------

--
-- Table structure for table `issue`
--

CREATE TABLE `issue` (
  `b_id` int(11) NOT NULL,
  `b_name` varchar(20) NOT NULL,
  `p_id` int(11) NOT NULL,
  `qtyissue` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `issue`
--

INSERT INTO `issue` (`b_id`, `b_name`, `p_id`, `qtyissue`) VALUES
(106, 'my journey', 4, 1),
(104, 'my life my mission', 3, 3),
(101, 'aliens', 1, 5),
(107, 'india of my dreams', 5, 4),
(105, 'mind master', 6, 3);

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`) VALUES
('2020123', 'manish@123');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `phone_no` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `birth_date` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `name`, `phone_no`, `city`, `birth_date`) VALUES
(1, 'manish gholam', '7738818493', 'mumbai', '13.06.1994'),
(2, 'mandar gholam', '8897642145', 'aurangabad', '14.03.1997'),
(3, 'dipesh tambe', '6792816486', 'ratnagiri', '05.05.1997'),
(4, 'vikrant ghag', '8108569352', 'chennai', '15.03.1997'),
(5, 'abhishek more', '9965736465', 'delhi', '06.09.1996'),
(6, 'abhijeet more', '6542323641', 'vikroli', '26.01.1990');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
