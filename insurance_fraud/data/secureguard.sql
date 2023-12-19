-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 28, 2023 at 05:40 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `secureguard`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add claims', 7, 'add_claims'),
(26, 'Can change claims', 7, 'change_claims'),
(27, 'Can delete claims', 7, 'delete_claims'),
(28, 'Can view claims', 7, 'view_claims'),
(29, 'Can add client', 8, 'add_client'),
(30, 'Can change client', 8, 'change_client'),
(31, 'Can delete client', 8, 'delete_client'),
(32, 'Can view client', 8, 'view_client'),
(33, 'Can add client_info', 9, 'add_client_info'),
(34, 'Can change client_info', 9, 'change_client_info'),
(35, 'Can delete client_info', 9, 'delete_client_info'),
(36, 'Can view client_info', 9, 'view_client_info'),
(37, 'Can add driver_info', 10, 'add_driver_info'),
(38, 'Can change driver_info', 10, 'change_driver_info'),
(39, 'Can delete driver_info', 10, 'delete_driver_info'),
(40, 'Can view driver_info', 10, 'view_driver_info'),
(41, 'Can add product', 11, 'add_product'),
(42, 'Can change product', 11, 'change_product'),
(43, 'Can delete product', 11, 'delete_product'),
(44, 'Can view product', 11, 'view_product'),
(45, 'Can add vehicle_info', 12, 'add_vehicle_info'),
(46, 'Can change vehicle_info', 12, 'change_vehicle_info'),
(47, 'Can delete vehicle_info', 12, 'delete_vehicle_info'),
(48, 'Can view vehicle_info', 12, 'view_vehicle_info'),
(49, 'Can add accident_info', 13, 'add_accident_info'),
(50, 'Can change accident_info', 13, 'change_accident_info'),
(51, 'Can delete accident_info', 13, 'delete_accident_info'),
(52, 'Can view accident_info', 13, 'view_accident_info'),
(53, 'Can add user payment', 14, 'add_userpayment'),
(54, 'Can change user payment', 14, 'change_userpayment'),
(55, 'Can delete user payment', 14, 'delete_userpayment'),
(56, 'Can view user payment', 14, 'view_userpayment'),
(57, 'Can add order', 15, 'add_order'),
(58, 'Can change order', 15, 'change_order'),
(59, 'Can delete order', 15, 'delete_order'),
(60, 'Can view order', 15, 'view_order'),
(61, 'Can add invoice', 16, 'add_invoice'),
(62, 'Can change invoice', 16, 'change_invoice'),
(63, 'Can delete invoice', 16, 'delete_invoice'),
(64, 'Can view invoice', 16, 'view_invoice'),
(65, 'Can add cart', 17, 'add_cart'),
(66, 'Can change cart', 17, 'change_cart'),
(67, 'Can delete cart', 17, 'delete_cart'),
(68, 'Can view cart', 17, 'view_cart'),
(69, 'Can add payment', 18, 'add_payment'),
(70, 'Can change payment', 18, 'change_payment'),
(71, 'Can delete payment', 18, 'delete_payment'),
(72, 'Can view payment', 18, 'view_payment'),
(73, 'Can add admin', 19, 'add_admin'),
(74, 'Can change admin', 19, 'change_admin'),
(75, 'Can delete admin', 19, 'delete_admin'),
(76, 'Can view admin', 19, 'view_admin'),
(77, 'Can add blog post', 20, 'add_blogpost'),
(78, 'Can change blog post', 20, 'change_blogpost'),
(79, 'Can delete blog post', 20, 'delete_blogpost'),
(80, 'Can view blog post', 20, 'view_blogpost'),
(81, 'Can add blog_comment', 21, 'add_blog_comment'),
(82, 'Can change blog_comment', 21, 'change_blog_comment'),
(83, 'Can delete blog_comment', 21, 'delete_blog_comment'),
(84, 'Can view blog_comment', 21, 'view_blog_comment'),
(85, 'Can add contact_message', 22, 'add_contact_message'),
(86, 'Can change contact_message', 22, 'change_contact_message'),
(87, 'Can delete contact_message', 22, 'delete_contact_message'),
(88, 'Can view contact_message', 22, 'view_contact_message'),
(89, 'Can add staff', 23, 'add_staff'),
(90, 'Can change staff', 23, 'change_staff'),
(91, 'Can delete staff', 23, 'delete_staff'),
(92, 'Can view staff', 23, 'view_staff');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(13, 'myapp', 'accident_info'),
(19, 'myapp', 'admin'),
(20, 'myapp', 'blogpost'),
(21, 'myapp', 'blog_comment'),
(17, 'myapp', 'cart'),
(7, 'myapp', 'claims'),
(8, 'myapp', 'client'),
(9, 'myapp', 'client_info'),
(22, 'myapp', 'contact_message'),
(10, 'myapp', 'driver_info'),
(16, 'myapp', 'invoice'),
(15, 'myapp', 'order'),
(18, 'myapp', 'payment'),
(11, 'myapp', 'product'),
(23, 'myapp', 'staff'),
(12, 'myapp', 'vehicle_info'),
(6, 'sessions', 'session'),
(14, 'user_payment', 'userpayment');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-09-23 17:15:30.409995'),
(2, 'auth', '0001_initial', '2023-09-23 17:15:38.906260'),
(3, 'admin', '0001_initial', '2023-09-23 17:15:41.680538'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-09-23 17:15:41.733188'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-09-23 17:15:41.788779'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-09-23 17:15:42.395011'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-09-23 17:15:43.289298'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-09-23 17:15:43.402598'),
(9, 'auth', '0004_alter_user_username_opts', '2023-09-23 17:15:43.471709'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-09-23 17:15:43.957085'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-09-23 17:15:43.988953'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-09-23 17:15:44.036929'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-09-23 17:15:44.221486'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-09-23 17:15:44.498395'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-09-23 17:15:44.657374'),
(16, 'auth', '0011_update_proxy_permissions', '2023-09-23 17:15:44.789523'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-09-23 17:15:44.929566'),
(18, 'myapp', '0001_initial', '2023-09-23 17:15:51.349934'),
(19, 'sessions', '0001_initial', '2023-09-23 17:15:52.093262'),
(20, 'user_payment', '0001_initial', '2023-09-23 17:15:53.618997'),
(21, 'myapp', '0002_order_invoice', '2023-09-30 18:39:52.735850'),
(22, 'myapp', '0003_cart_payment_invoice_customer_name_invoice_email_and_more', '2023-10-01 16:55:26.678430'),
(23, 'myapp', '0004_cart_id_alter_cart_email', '2023-10-03 18:37:16.801072'),
(24, 'myapp', '0005_alter_cart_id', '2023-10-07 20:42:10.810535'),
(25, 'myapp', '0006_remove_cart_id_alter_cart_email', '2023-10-07 20:42:12.921323'),
(26, 'myapp', '0007_cart_id_alter_cart_email', '2023-10-07 20:43:45.382321'),
(27, 'myapp', '0008_cart_cart_session_alter_cart_id', '2023-10-08 15:47:16.811180'),
(28, 'myapp', '0009_admin', '2023-10-09 15:41:25.030605'),
(29, 'myapp', '0010_delete_admin', '2023-10-09 15:43:23.731433'),
(30, 'myapp', '0011_admin', '2023-10-09 15:44:38.360923'),
(31, 'myapp', '0012_blogpost', '2023-10-13 12:29:00.860930'),
(32, 'myapp', '0013_alter_blogpost_date', '2023-10-13 15:02:01.854771'),
(33, 'myapp', '0014_blog_comment', '2023-10-14 14:33:42.766050'),
(34, 'myapp', '0015_contact_message', '2023-10-31 13:05:59.223240'),
(35, 'myapp', '0016_alter_contact_message_message', '2023-10-31 13:10:48.351452'),
(36, 'myapp', '0017_contact_message_message_posted', '2023-10-31 18:26:14.901407'),
(37, 'myapp', '0018_cart_order_id_payment_order_id_alter_order_order_id', '2023-11-03 08:10:22.402228'),
(38, 'myapp', '0019_alter_invoice_invoice_id', '2023-11-03 11:49:04.338680'),
(39, 'myapp', '0020_claims_probability', '2023-11-27 18:31:03.893793'),
(40, 'myapp', '0021_staff', '2023-11-27 18:52:57.117623');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('3ek88q6316wgxyhy3aa2k3qqanwysnwj', 'eyJlbWFpbCI6ImNvd29iNTk4NTZAanVjYXR5by5jb20ifQ:1qywI4:_tolEflq5tndRb6AiGnzsNiJYFEjuSJ2HbA4I5oeYd8', '2023-11-17 15:40:56.025316'),
('3trq6slbim2ra00nrtzu91kuttpjro3u', 'eyJlbWFpbCI6ImtoYW5kYWthci5hcnJhZkBnbWFpbC5jb20iLCJjYXJ0X3Nlc3Npb24iOjg0NzJ9:1qpYgW:ud_f1IygRWQnyg0rXdDlsz4tABGCAJvkvagBZ2CDNxQ', '2023-10-22 18:39:24.580507'),
('900nhycl6wlimcrb7thwmbv5lvasvdpb', 'eyJlbWFpbCI6ImtoYW5kYWthci5hcnJhZkBnbWFpbC5jb20ifQ:1qyH63:Crh6_NmS0Gz5QW6DbJFBYALKGEto_oqkxpadVUe99JM', '2023-11-15 19:41:47.331960'),
('aja320a3xx9ssxdghcax1thf5ohw9glb', 'eyJlbWFpbCI6ImtoYW5kYWthci5hcnJhZkBnbWFpbC5jb20ifQ:1r1X0I:thT6O3hsHETI5KXmT3R7TXtuWIhXx0WVonVLnLZAAfg', '2023-11-24 19:17:18.876721'),
('b5mjovrprdjdwq2p9sgmfnc5amxnsdfe', '.eJyrVkrNTczMUbJSys5IzEtJzE4s0kssKkpMc0gHiesl5-cq6SiVFqcWxScXpaak5pVkJhJSnZOfnpkXX1ySWFJarGRlWAsAF8UkDQ:1qpDii:wtjZPEEDtvnIjSEQcxPBXSRJl_apvi7L2mKg0nSyEd4', '2023-10-21 20:16:16.244834'),
('brkmeagysfzdegt3msczb6pnra1h53je', 'eyJhZG1pbl9sb2dpbiI6ImFkbWlucGFzc2VkIn0:1qqyo2:LbJ1oDLmO4mx6SXSIeGxMUf6ijl1PE78Qzv9S0umgq0', '2023-10-26 16:45:02.368995'),
('edgvd07u6146zildsnxe1j1ypqeof1k5', 'eyJlbWFpbCI6ImtoYW5kYWthci5hcnJhZkBnbWFpbC5jb20iLCJhZG1pbl9sb2dpbiI6ImFkbWlucGFzc2VkIn0:1r1Y9y:N3qJ8xsGJWFWZwabZGXQbS7d6vyJBvOcIIXzVwuPCDg', '2023-11-24 20:31:22.532478'),
('h1nvoncmiioku1aql4dr3ts24q5hk19g', 'eyJlbWFpbCI6ImtoYW5kYWthci5hcnJhZkBnbWFpbC5jb20iLCJhZG1pbl9sb2dpbiI6ImFkbWlucGFzc2VkIn0:1qpwDC:IrxUgWU2uUW7NJBvAF11yPLIzuy9N9kUiDVlXQIHKKg', '2023-10-23 19:46:42.473339'),
('hd5qmdlp6fphk6g7inloy9naic4oji18', 'eyJlbWFpbCI6ImFycmFmQGxpdmUuY29tIn0:1r19dH:-6MDVBpVr5GV94X3hNewlSSdIcRdd4GtHlqmw142g4g', '2023-11-23 18:19:59.329616'),
('hdre1lk0ylsd10rvpbmuac488j475gr7', 'eyJhZG1pbl9sb2dpbiI6ImFkbWlucGFzc2VkIn0:1qz0hY:oKjlAvKFffrU9OM2Yb57gd123zvKfdjyLH23X23y3WY', '2023-11-17 20:23:32.074441'),
('hl9q4hxh0y8zfm733tcgsug39v6atj48', 'eyJhZG1pbl9sb2dpbiI6ImFkbWlucGFzc2VkIn0:1qxCHQ:dmsclsJcBJTgC6jgdA2Ft6S2GwyJ-cfjVDOZw-ffHsM', '2023-11-12 20:21:04.339262'),
('i8n50kikfh7aa1vggnie6i3f5z1q680b', '.eJyrVkrNTczMUbJSys5IzEtJzE4s0kssKkpMc0gHiesl5-cq6SiVFqcWxScXpaak5pVkJhKlOjNFycpYRyknPz0zL764JLGktFjJyrAWANhdJ9U:1qyes7:L15FJmiTZjoA-0Hie9-kQtpUMZjmeLfaYuxIENEg6uc', '2023-11-16 21:04:59.161460'),
('igfak4qssj0xrmqenhngef3qjmtcgvj3', 'eyJlbWFpbCI6ImtoYW5kYWthci5hcnJhZkBnbWFpbC5jb20ifQ:1r0OQa:lcjA5Ui81xvxXS4NQ0AMc3xnOyHnmMePz78uvSCXnsM', '2023-11-21 15:55:44.850372'),
('ikq0at9b888gz4ctz07tnbf2rkh0p4nh', 'eyJhZG1pbl9sb2dpbiI6ImFkbWlucGFzc2VkIn0:1qtwKB:BoLV0QXOMysWEddvLhferDicCMH2e9R4WWD8F51NzNE', '2023-11-03 20:42:27.992080'),
('k39wigvaldib9py3arusfxrna37rppns', 'eyJlbWFpbCI6ImtoYW5kYWthci5hcnJhZkBnbWFpbC5jb20ifQ:1qpEXP:xip35aYDotfO2ttThB5pnrGbFiHX0_psfCU6LbA44zs', '2023-10-21 21:08:39.650088'),
('k46s957xcqgnotf2nnbp18vsq575t9zs', '.eJyrVkrNTczMUbJSys5IzEtJzE4s0kssKkpMc0gHiesl5-cq6SiVFqcWxScXpaak5pVkJhKlOjNFycpYRyknPz0zL764JLGktFjJyrAWANhdJ9U:1qxW9O:X2d70N4sIUCwqD_lrCpBIgwp44q9yKVyhD4tOPVLi-Q', '2023-11-13 17:34:06.490611'),
('k702c2u9pt5l4ipj3rpvlwtjm52kd4d7', '.eJyrVkrNTczMUbJSys5IzEtJzE4s0kssKkpMc0gHiesl5-cq6SiVFqcWxScXpaak5pVkJhKlOjNFycpYRyknPz0zL764JLGktFjJyrAWANhdJ9U:1qrgGe:mbUisnxIl_u_kV7aGEj1ZCLE02eqaLjIYxGH0W_LXdY', '2023-10-28 15:09:28.897465'),
('l12za0pk2os3joefxvi4t3l6c2woogm1', 'eyJlbWFpbCI6ImtoYW5kYWthci5hcnJhZkBnbWFpbC5jb20ifQ:1r1Xmo:a4Pm44CELHTc8qMz2Af4VqYCxcBRBTO7fmqDj2XhFUo', '2023-11-24 20:07:26.290039'),
('m0z6ndopfte4xnvl14365dkz1o4akq92', 'eyJlbWFpbCI6ImtoYW5kYWthci5hcnJhZkBnbWFpbC5jb20ifQ:1qyq8w:TCAZL5R-ODgmHwmYp7qlbK5fvyQMMGVCvjB2wzJ3Bn8', '2023-11-17 09:07:06.550436'),
('n564alociseyn2wz4ycvylb4h0plvmme', '.eJyrVkrNTczMUbJSys5IzEtJzE4s0kssKkpMc0gHiesl5-cq6SiVFqcWxScXpaak5pVkJhKlOjNFycpYRyknPz0zL764JLGktFjJyrAWANhdJ9U:1qpDnU:sNPaLt_3EHocTE9A-xd-bscBeZ74M1zkeNv143nM5hw', '2023-10-21 20:21:12.114223'),
('oweibl0pxk98kifsr69zi9sz0ytjiwqs', 'eyJlbWFpbCI6ImtoYW5kYWthci5hcnJhZkBnbWFpbC5jb20iLCJhZG1pbl9sb2dpbiI6ImFkbWlucGFzc2VkIn0:1qslX4:PiDUBQG3rctnqgnaNUTBI2QETZszephYNfUlk7tjgXs', '2023-10-31 14:58:54.235528'),
('oyil0le3bkrs0e8hljmd8eg0jj6t4lc8', '.eJyrVkrNTczMUbJSys5IzEtJzE4s0kssKkpMc0gHiesl5-cq6SiVFqcWxScXpaak5pVkJhKlOjNFycpSRyknPz0zL764JLGktFjJyrAWANjPJ9s:1r0RJw:r7ehVUmUx-55Tv-4YxoSPIxpUHtmPm0M-8ObseyDaig', '2023-11-21 19:01:04.284844'),
('sh0bvj86veja3qfaktersvep9m72upzo', 'eyJlbWFpbCI6ImtoYW5kYWthci5hcnJhZkBnbWFpbC5jb20ifQ:1qucLu:ZQQUKgRIMqaP2oybROhIrXiO8DUicGoXb3IJppLxZkE', '2023-11-05 17:35:02.441031'),
('tp7demlnnz8k5vuu9v9y9xp8xpz4ilpv', 'eyJhZG1pbl9sb2dpbiI6ImFkbWlucGFzc2VkIn0:1qrK90:fhsczAvZcs1-85mVZiK0L4iaBlNqATGOEHW5FzM1ZF4', '2023-10-27 15:32:06.770618'),
('tq8kch6jpvmjccindfz1vp9ry2kawzym', '.eJwdis0NgCAMRnfp2TCAJ53EfAHEBlpMORp3t3h8Pw8pJNNKuxlOWigLuDnXC5pQYQGzbGX6ELv4gySsR-uF1c-fboyRE70fRAEbzA:1r7hs7:Hb7sZlOQSJ_ZA0874A9CNITYwLMO5Z87hSYMGzL91aU', '2023-12-11 20:06:23.176003'),
('tuophcioohsoj6pkz66hr26iu3wgfpck', '.eJwdi8EKhSAQRf9l1iEjGUir_iQuo5WUFtpbPKJ_L1uec8-9yEeEjXpaFySHFVkhZ0zDXL2SPVJDCdG_yTe8uO1zKKeMEPllyJ96Vtbo1hirLXPHrE1DcDGksbapfisdKMU7uh8nBibG:1r7ppq:vQmJidCR0fGJPzIlYC_M5udgW76G7Egu01QHlHyGg_A', '2023-12-12 04:36:34.158413'),
('ut7jgn4eyoseuizc43uvuw8t78fk95q4', 'eyJhZG1pbl9sb2dpbiI6ImFkbWlucGFzc2VkIn0:1qs30D:KdQJKpV0tUl4sYkCV5jktERAWO3lDrJ95HjqBUxvTDg', '2023-10-29 15:26:01.574241'),
('way6ljxlqo4i49m2pmgwpmwq2ih7t7p4', '.eJyrVkrNTczMUbJSys5IzEtJzE4s0kssKkpMc0gHiesl5-cq6SiVFqcWxScXpaak5pVkJhKlOjNFycpYRyknPz0zL764JLGktFjJyrAWANhdJ9U:1quE4e:tVAWCtLJbcnmAS6WpocXKgfJGSsoUh7sEVr1yHLo6-U', '2023-11-04 15:39:36.514960'),
('wqm8xkucgt9zv4rlq8dg9ov97n0my52k', 'eyJlbWFpbCI6ImtoYW5kYWthci5hcnJhZkBnbWFpbC5jb20iLCJhZG1pbl9sb2dpbiI6ImFkbWlucGFzc2VkIn0:1r1Nfc:foMhM-7N50b1nh5PzbtJfft_6Sslx4ZAdJYs4ZRWTBw', '2023-11-24 09:19:20.743951'),
('ybu6yc38w0h79ibshtwqzr7de6wlm8q8', '.eJyrVkrNTczMUbJSys5IzEtJzE4s0kssKkpMc0gHiesl5-cq6SiVFqcWxScXpaak5pVkJhKlOjNFycpYRyknPz0zL764JLGktFjJyrAWANhdJ9U:1qxnUd:JZ4XzzM7sT2avKIaY2L5E25UtWgddGLb-AoECapalbE', '2023-11-14 12:05:11.755507'),
('zrddis1v29l2d4gs5d1rabhlmtcmh6o5', '.eJyrVkrNTczMUbJSys5IzEtJzE4s0kssKkpMc0gHiesl5-cq6SiVFqcWxWemKFkZQ9nJRakpqXklmYmEdObkp2fmxReXJJaUFitZGdYCAL1xJ9U:1qpDcf:9M2b6R5AlpsHZFAonf9jd4sfC9pKJvGlqyPV2FaggHU', '2023-10-21 20:10:01.056925');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_accident_info`
--

CREATE TABLE `myapp_accident_info` (
  `id` bigint(20) NOT NULL,
  `witness` tinyint(1) DEFAULT NULL,
  `accident_loaction` varchar(255) DEFAULT NULL,
  `claim_id_id` varchar(40) NOT NULL,
  `vehicle_id_id` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `myapp_admin`
--

CREATE TABLE `myapp_admin` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_admin`
--

INSERT INTO `myapp_admin` (`id`, `name`, `email`, `password`) VALUES
(1, 'michael Doe', 'admin@example.com', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_blogpost`
--

CREATE TABLE `myapp_blogpost` (
  `id` bigint(20) NOT NULL,
  `author_name` varchar(100) DEFAULT NULL,
  `blog_title` varchar(200) DEFAULT NULL,
  `user_image` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `writing` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_blogpost`
--

INSERT INTO `myapp_blogpost` (`id`, `author_name`, `blog_title`, `user_image`, `date`, `writing`) VALUES
(4, 'Jansen', 'Insurance fraud', 'uploads/blogs/download_1.jfif', '2023-11-14', 'Auto insurance fraud is a pervasive issue that costs the industry billions of dollars annually. As technology advances, so do the methods employed by fraudsters. In response, the insurance industry has turned to innovative solutions, particularly in the realm of fraud detection. This blog will delve into the importance of auto insurance fraud detection and explore the cutting-edge technologies and strategies being employed to combat this growing menace.\r\n\r\nAuto insurance fraud comes in various forms, ranging from staged accidents and false claims to more sophisticated scams involving identity theft and organized crime rings. These fraudulent activities not only lead to financial losses for insurance companies but also contribute to increased premiums for law-abiding policyholders.\r\n\r\nAs technology continues to evolve, so does the battle against auto insurance fraud. The integration of advanced technologies, from data analytics and machine learning to blockchain and IoT, empowers insurance companies to stay one step ahead of fraudsters. The collective efforts of the insurance industry in developing and implementing effective fraud detection strategies will not only protect the financial interests of insurers but also foster a more trustworthy and reliable insurance ecosystem for all stakeholders.'),
(5, 'Volf Hammer', 'Role of technology', 'uploads/blogs/download_1_raIQSiS.jfif', '2023-11-14', 'Data Analytics and Machine Learning:\r\nHarnessing the power of big data analytics and machine learning, insurance companies can sift through vast amounts of information to identify patterns and anomalies. These technologies enable insurers to analyze historical data, detect irregularities, and predict potential fraud based on behavior patterns.\r\n\r\nTelematics and IoT Devices:\r\nThe advent of telematics and the Internet of Things (IoT) has revolutionized the insurance industry. By leveraging data from connected devices, such as in-car sensors and GPS systems, insurers can gain real-time insights into a driver\'s behavior. This not only aids in risk assessment but also helps in identifying suspicious activities or inconsistent claims.\r\n\r\nSocial Media Monitoring:\r\nSocial media platforms have become treasure troves of information. Insurance companies are increasingly using social media monitoring tools to investigate claims and verify the authenticity of reported incidents. This proactive approach helps in preventing fraudulent claims before they escalate.\r\n\r\nBlockchain Technology:\r\nBlockchain\'s decentralized and tamper-resistant nature makes it a valuable tool in the fight against fraud. Insurers can use blockchain to create a secure and transparent ledger of insurance transactions, making it more difficult for fraudsters to manipulate data or submit false claims.');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_blog_comment`
--

CREATE TABLE `myapp_blog_comment` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `user_name` varchar(100) DEFAULT NULL,
  `comment` longtext DEFAULT NULL,
  `comment_date` date DEFAULT NULL,
  `blog_id_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_blog_comment`
--

INSERT INTO `myapp_blog_comment` (`id`, `user_id`, `user_name`, `comment`, `comment_date`, `blog_id_id`) VALUES
(39, 17, 'Arraf', 'Awesome post on critical topic', '2023-11-14', 4);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_cart`
--

CREATE TABLE `myapp_cart` (
  `email` varchar(254) DEFAULT NULL,
  `item_name` varchar(100) DEFAULT NULL,
  `item_price` varchar(100) DEFAULT NULL,
  `total` double DEFAULT NULL,
  `id` bigint(20) NOT NULL,
  `cart_session` double DEFAULT NULL,
  `order_id_id` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_cart`
--

INSERT INTO `myapp_cart` (`email`, `item_name`, `item_price`, `total`, `id`, `cart_session`, `order_id_id`) VALUES
('khandakar.arraf@gmail.com', 'Insurance book', '22', 22, 70, NULL, '7622'),
('khandakar.arraf@gmail.com', 'Insurance book', '22', 22, 71, NULL, '9504'),
('khandakar.arraf@gmail.com', 'Insurance book', '22', 22, 72, NULL, '4347'),
('khandakar.arraf@gmail.com', 'Insurance book', '22', 22, 73, NULL, '5273');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_claims`
--

CREATE TABLE `myapp_claims` (
  `claim_id` varchar(40) NOT NULL,
  `claim_payout` double DEFAULT NULL,
  `liability_claim_percentage` double DEFAULT NULL,
  `policy_channel` varchar(255) DEFAULT NULL,
  `third_party_policy` varchar(255) DEFAULT NULL,
  `fraud` tinyint(1) DEFAULT NULL,
  `probability` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `myapp_client`
--

CREATE TABLE `myapp_client` (
  `client_id` int(11) NOT NULL,
  `client_name` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `account_status` varchar(10) NOT NULL,
  `user_image` varchar(100) DEFAULT NULL,
  `client_password` varchar(255) DEFAULT NULL,
  `client_confirm_password` varchar(255) DEFAULT NULL,
  `role` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_client`
--

INSERT INTO `myapp_client` (`client_id`, `client_name`, `email`, `phone_number`, `dob`, `address`, `gender`, `age`, `account_status`, `user_image`, `client_password`, `client_confirm_password`, `role`) VALUES
(17, 'Arraf', 'khandakar.arraf@gmail.com', '01821685567', '2023-11-04', '19/1, Daffodil Concord Tower, Panthapath, Dhaka 1205', 'male', 1, 'active', 'uploads/cart1.jpg', 'pbkdf2_sha256$600000$K88DmmumYj7vByEeM1YzmL$GfPepOdMZcgHYPwsBRtpCzV8jBsmGJhpjY9e69aaDlw=', 'pbkdf2_sha256$600000$HNZUSCoa6jlKdogTZKcDFD$9UBSG9+Y3qpLDmlXDpal4WWak241X45rEYsvBWTiY/0=', '');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_client_info`
--

CREATE TABLE `myapp_client_info` (
  `phone_number` varchar(30) NOT NULL,
  `claim_number` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `myapp_contact_message`
--

CREATE TABLE `myapp_contact_message` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `subject` varchar(100) DEFAULT NULL,
  `message` longtext DEFAULT NULL,
  `message_posted` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_contact_message`
--

INSERT INTO `myapp_contact_message` (`id`, `name`, `email`, `phone`, `subject`, `message`, `message_posted`) VALUES
(1, 'arraf', 'khandakar.arraf@gmail.com', '01821-685567', 'inquiry for insurance service', 'dawdawddawd jmrddw', '2023-11-01'),
(2, 'arraf', 'jon.example@gmail.com', '4252512', 'inquiry for insurance service', 'fawfawfaw jjtffzdsvsd ', '2023-11-01'),
(3, 'Arraf', 'khandakar.arraf@gmail.com', '01821685567', 'Inquiry for insurance ML', 'Hi , I am interested to know whether ML is promising about detecting fraud, especially auto insurance.', '2023-11-11'),
(4, 'arraf', 'khandakar.arraf@gmail.com', '4252512', 'inquiry for insurance service', 'dawdawwd', '2023-11-14'),
(5, 'arraf', 'khandakar.arraf@gmail.com', '4252512', 'inquiry for insurance service', 'I need help for insurance fraud', '2023-11-16');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_driver_info`
--

CREATE TABLE `myapp_driver_info` (
  `vehicle_id` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `age` double DEFAULT NULL,
  `zip_code` varchar(255) DEFAULT NULL,
  `number_of_claims_five_years` int(11) DEFAULT NULL,
  `marital_status` varchar(255) DEFAULT NULL,
  `living_status` varchar(255) DEFAULT NULL,
  `address_change` varchar(255) DEFAULT NULL,
  `claim_id_id` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `myapp_invoice`
--

CREATE TABLE `myapp_invoice` (
  `invoice_id` varchar(10) NOT NULL,
  `order_date` date DEFAULT NULL,
  `order_id_id` varchar(10) NOT NULL,
  `customer_name` varchar(100) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `gateway` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_invoice`
--

INSERT INTO `myapp_invoice` (`invoice_id`, `order_date`, `order_id_id`, `customer_name`, `email`, `gateway`) VALUES
('C58332', '2023-11-11', '7622', 'Arraf', 'khandakar.arraf@gmail.com', 'rocket'),
('J15265', '2023-11-19', '4347', 'Arraf', 'khandakar.arraf@gmail.com', 'rocket'),
('O86010', '2023-11-11', '9504', 'Arraf', 'khandakar.arraf@gmail.com', 'rocket');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_order`
--

CREATE TABLE `myapp_order` (
  `order_id` varchar(10) NOT NULL,
  `order_date` date DEFAULT NULL,
  `customer_name` varchar(100) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `total` double DEFAULT NULL,
  `gateway` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_order`
--

INSERT INTO `myapp_order` (`order_id`, `order_date`, `customer_name`, `email`, `status`, `total`, `gateway`) VALUES
('4347', '2023-11-12', 'arraf', 'khandakar.arraf@gmail.com', 'approved', 22, 'rocket'),
('5121', '2023-11-19', 'Arraf', 'khandakar.arraf@gmail.com', 'pending', 66, 'rocket'),
('5273', '2023-11-12', 'arraf', 'khandakar.arraf@gmail.com', 'pending', 22, 'rocket'),
('7622', '2023-11-11', 'arraf', 'khandakar.arraf@gmail.com', 'approved', 22, 'rocket'),
('9504', '2023-11-11', 'arraf', 'khandakar.arraf@gmail.com', 'approved', 22, 'rocket');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_payment`
--

CREATE TABLE `myapp_payment` (
  `payment_id` int(11) NOT NULL,
  `transaction_number` varchar(255) DEFAULT NULL,
  `phone_number` varchar(255) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `order_id_id` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `myapp_product`
--

CREATE TABLE `myapp_product` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `price` double NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `myapp_staff`
--

CREATE TABLE `myapp_staff` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_staff`
--

INSERT INTO `myapp_staff` (`id`, `name`, `email`, `password`) VALUES
(1, 'John sans', 'john@live.com', 'staff');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_vehicle_info`
--

CREATE TABLE `myapp_vehicle_info` (
  `id` bigint(20) NOT NULL,
  `price` double DEFAULT NULL,
  `weight` varchar(255) DEFAULT NULL,
  `color` varchar(255) DEFAULT NULL,
  `vehicle_age` double DEFAULT NULL,
  `claim_id_id` varchar(40) NOT NULL,
  `vehicle_id_id` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_payment_userpayment`
--

CREATE TABLE `user_payment_userpayment` (
  `id` bigint(20) NOT NULL,
  `payment_bool` tinyint(1) NOT NULL,
  `stripe_checkout_id` varchar(500) NOT NULL,
  `client_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `myapp_accident_info`
--
ALTER TABLE `myapp_accident_info`
  ADD PRIMARY KEY (`id`),
  ADD KEY `myapp_accident_info_vehicle_id_id_aec86081_fk_myapp_dri` (`vehicle_id_id`),
  ADD KEY `myapp_accident_info_claim_id_id_2bd59b7c_fk_myapp_cla` (`claim_id_id`);

--
-- Indexes for table `myapp_admin`
--
ALTER TABLE `myapp_admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_blogpost`
--
ALTER TABLE `myapp_blogpost`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_blog_comment`
--
ALTER TABLE `myapp_blog_comment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `blog_id_id` (`blog_id_id`);

--
-- Indexes for table `myapp_cart`
--
ALTER TABLE `myapp_cart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `myapp_cart_order_id_id_c3b5b6f5_fk` (`order_id_id`);

--
-- Indexes for table `myapp_claims`
--
ALTER TABLE `myapp_claims`
  ADD PRIMARY KEY (`claim_id`);

--
-- Indexes for table `myapp_client`
--
ALTER TABLE `myapp_client`
  ADD PRIMARY KEY (`client_id`);

--
-- Indexes for table `myapp_client_info`
--
ALTER TABLE `myapp_client_info`
  ADD PRIMARY KEY (`phone_number`);

--
-- Indexes for table `myapp_contact_message`
--
ALTER TABLE `myapp_contact_message`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_driver_info`
--
ALTER TABLE `myapp_driver_info`
  ADD PRIMARY KEY (`vehicle_id`),
  ADD KEY `myapp_driver_info_claim_id_id_c1f64bdb_fk_myapp_claims_claim_id` (`claim_id_id`);

--
-- Indexes for table `myapp_invoice`
--
ALTER TABLE `myapp_invoice`
  ADD PRIMARY KEY (`invoice_id`),
  ADD KEY `myapp_invoice_order_id_id_3a22260f_fk` (`order_id_id`);

--
-- Indexes for table `myapp_order`
--
ALTER TABLE `myapp_order`
  ADD PRIMARY KEY (`order_id`);

--
-- Indexes for table `myapp_payment`
--
ALTER TABLE `myapp_payment`
  ADD PRIMARY KEY (`payment_id`),
  ADD KEY `myapp_payment_order_id_id_70d622f8_fk` (`order_id_id`);

--
-- Indexes for table `myapp_product`
--
ALTER TABLE `myapp_product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_staff`
--
ALTER TABLE `myapp_staff`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_vehicle_info`
--
ALTER TABLE `myapp_vehicle_info`
  ADD PRIMARY KEY (`id`),
  ADD KEY `myapp_vehicle_info_claim_id_id_ff804c77_fk_myapp_claims_claim_id` (`claim_id_id`),
  ADD KEY `myapp_vehicle_info_vehicle_id_id_192ccb66_fk_myapp_dri` (`vehicle_id_id`);

--
-- Indexes for table `user_payment_userpayment`
--
ALTER TABLE `user_payment_userpayment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_payment_userpay_client_id_id_27bb94af_fk_myapp_cli` (`client_id_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=93;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `myapp_accident_info`
--
ALTER TABLE `myapp_accident_info`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;

--
-- AUTO_INCREMENT for table `myapp_admin`
--
ALTER TABLE `myapp_admin`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `myapp_blogpost`
--
ALTER TABLE `myapp_blogpost`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `myapp_blog_comment`
--
ALTER TABLE `myapp_blog_comment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT for table `myapp_cart`
--
ALTER TABLE `myapp_cart`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=74;

--
-- AUTO_INCREMENT for table `myapp_client`
--
ALTER TABLE `myapp_client`
  MODIFY `client_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `myapp_contact_message`
--
ALTER TABLE `myapp_contact_message`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `myapp_payment`
--
ALTER TABLE `myapp_payment`
  MODIFY `payment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=104;

--
-- AUTO_INCREMENT for table `myapp_product`
--
ALTER TABLE `myapp_product`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `myapp_staff`
--
ALTER TABLE `myapp_staff`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `myapp_vehicle_info`
--
ALTER TABLE `myapp_vehicle_info`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;

--
-- AUTO_INCREMENT for table `user_payment_userpayment`
--
ALTER TABLE `user_payment_userpayment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `myapp_accident_info`
--
ALTER TABLE `myapp_accident_info`
  ADD CONSTRAINT `myapp_accident_info_claim_id_id_2bd59b7c_fk_myapp_cla` FOREIGN KEY (`claim_id_id`) REFERENCES `myapp_claims` (`claim_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `myapp_accident_info_vehicle_id_id_aec86081_fk_myapp_dri` FOREIGN KEY (`vehicle_id_id`) REFERENCES `myapp_driver_info` (`vehicle_id`);

--
-- Constraints for table `myapp_blog_comment`
--
ALTER TABLE `myapp_blog_comment`
  ADD CONSTRAINT `myapp_blog_comment_blog_id_id_209aa0a7_fk_myapp_blogpost_id` FOREIGN KEY (`blog_id_id`) REFERENCES `myapp_blogpost` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `myapp_cart`
--
ALTER TABLE `myapp_cart`
  ADD CONSTRAINT `myapp_cart_order_id_id_c3b5b6f5_fk` FOREIGN KEY (`order_id_id`) REFERENCES `myapp_order` (`order_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `myapp_driver_info`
--
ALTER TABLE `myapp_driver_info`
  ADD CONSTRAINT `myapp_driver_info_claim_id_id_c1f64bdb_fk_myapp_claims_claim_id` FOREIGN KEY (`claim_id_id`) REFERENCES `myapp_claims` (`claim_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `myapp_invoice`
--
ALTER TABLE `myapp_invoice`
  ADD CONSTRAINT `myapp_invoice_order_id_id_3a22260f_fk` FOREIGN KEY (`order_id_id`) REFERENCES `myapp_order` (`order_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `myapp_payment`
--
ALTER TABLE `myapp_payment`
  ADD CONSTRAINT `myapp_payment_order_id_id_70d622f8_fk` FOREIGN KEY (`order_id_id`) REFERENCES `myapp_order` (`order_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `myapp_vehicle_info`
--
ALTER TABLE `myapp_vehicle_info`
  ADD CONSTRAINT `myapp_vehicle_info_claim_id_id_ff804c77_fk_myapp_claims_claim_id` FOREIGN KEY (`claim_id_id`) REFERENCES `myapp_claims` (`claim_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `myapp_vehicle_info_vehicle_id_id_192ccb66_fk_myapp_dri` FOREIGN KEY (`vehicle_id_id`) REFERENCES `myapp_driver_info` (`vehicle_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `user_payment_userpayment`
--
ALTER TABLE `user_payment_userpayment`
  ADD CONSTRAINT `user_payment_userpay_client_id_id_27bb94af_fk_myapp_cli` FOREIGN KEY (`client_id_id`) REFERENCES `myapp_client` (`client_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
