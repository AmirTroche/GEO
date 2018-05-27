-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Värd: 127.0.0.1
-- Tid vid skapande: 25 maj 2018 kl 10:33
-- Serverversion: 10.1.31-MariaDB
-- PHP-version: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Databas: `yourgeo`
--

-- --------------------------------------------------------

--
-- Tabellstruktur `answers`
--

CREATE TABLE `answers` (
  `answersID` int(11) NOT NULL,
  `right_answer` varchar(255) NOT NULL,
  `wrong_answer_1` varchar(255) NOT NULL,
  `wrong_answer_2` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumpning av Data i tabell `answers`
--

INSERT INTO `answers` (`answersID`, `right_answer`, `wrong_answer_1`, `wrong_answer_2`) VALUES
(1, 'Hekla', 'Etna', 'Katlan'),
(2, '2500km', '2000km', '4000km'),
(3, 'Kalksten', 'Koppar', 'Arsenik'),
(4, 'Kemi älv', 'Vouksen', 'Torneälv'),
(5, '1:a plats', '2:a plats', '3:e plats'),
(6, 'Jylland', 'Lolland', 'Møn'),
(7, 'Tallinn ', 'Tartu', 'Narva'),
(8, 'Lettiska', 'Lettlandska', 'Lettska'),
(9, 'I landet hittar man Europas geografiska mittpunkt', 'Landet har ett medelhavsklimat', 'Landet hör inte till de baltiska länderna'),
(10, 'Shannon', 'Nore', 'Suir'),
(11, 'Manchester', 'Wales', 'Skottland'),
(12, 'Sierra Nevada', 'Alperna', 'Harz'),
(13, 'Hälften av landet ligger under havsytans nivå', 'En fjärdedel av landet är 50 meter över havsytans nivå', 'En fjärdedel av landet ligger under havsytans nivå'),
(14, 'Svalt i norr och hett i söder', 'Både svalt och hett i hela Frankrike', 'Extrema klimatförhållanden råder ofta'),
(15, 'ca 11 miljoner', 'ca 9 miljoner', 'ca 5 miljoner'),
(16, 'Tyska', 'Engelska', 'Danska'),
(17, 'Snezka', 'Seska', 'Lalezka'),
(18, 'Förbundsrepublik', 'Demokrati', 'Konstitutionell monarki'),
(19, 'Plats 46', 'Plats 10', 'Plats 34'),
(20, 'Bergssterräng', 'Skogsterräng', 'Sandterräng'),
(21, 'Hög punkt', 'Flod', 'Sjö'),
(22, 'Kanarieöarna', 'Bahamas', 'Amiralsöarna'),
(23, 'Ett av kontinentens varmaste länder', 'Ett av de minsta länderna', 'Ett extremt kallt väder på sommaren'),
(24, 'Över 60 miljoner', 'Över 30 miljoner', 'Över 80 miljoner'),
(25, 'Fem', 'Fyra', 'Två'),
(26, 'Europas tredje skogstätaste land', 'Europas femte största land till ytan', 'Ca 50% av landet är skyddat som Natura 2000'),
(27, 'Donau', 'Sava', 'Themsen'),
(28, 'Dinara', 'Triglav', 'Maglic'),
(29, 'Landets kustlinje är 24 km lång', 'Landet är för det mesta bergigt och skogsklätt', 'Landet är ett av Europas minsta länder'),
(30, 'Skodersjön', 'Tarasjön', 'Lim'),
(31, 'Medelhavsklimat', 'Kontinentalt klimat', 'Inlandsklimat'),
(32, 'Serbiska', 'Engelska', 'Albanska'),
(33, 'Snö och is', 'Extrema väderförhållanden', 'Torka'),
(34, 'Sofia', 'Anna', 'Henrik'),
(35, 'Vardar', 'Ohrid', 'Crna Reka'),
(36, 'Inlandsklimat', 'Medelhavsklimat', 'Snö och is året om'),
(37, 'Valletta', 'Mariette', 'Nora'),
(38, 'San Marino', 'Lasarote', 'Novaw'),
(39, 'Plats 49', 'Plats 43', 'Plats 56'),
(40, 'Jordbruk', 'Skog', 'Vatten'),
(41, 'Warszawa', 'Zakopane', 'Sopot'),
(42, 'Ca 5 miljoner', 'Ca 0,5 miljoner', 'Ca 4 miljoner'),
(43, 'Donau', 'Axios', 'Sava'),
(44, 'Grönsaker', 'Frukt', 'Vin'),
(45, 'Minsk', 'Munk', 'Levala'),
(46, 'Albanska', 'Azerbajdzjanska', 'Serbiska'),
(47, 'Inlandsklimat', 'Stäppklimat', 'Subtropiskt'),
(48, 'Svarta havet', 'Röda havet', 'Medelhavet'),
(49, '26 kilometer', '80 kilometer', '18 kilometer');

-- --------------------------------------------------------

--
-- Tabellstruktur `questions`
--

CREATE TABLE `questions` (
  `QuestionID` int(11) NOT NULL,
  `Question` varchar(255) NOT NULL,
  `Area` varchar(255) NOT NULL,
  `Country` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumpning av Data i tabell `questions`
--

INSERT INTO `questions` (`QuestionID`, `Question`, `Area`, `Country`) VALUES
(1, 'Vad heter den kända vulkanen?', 'Norra Europa', 'Island'),
(2, 'Ungefär hur stor kustlinje har landet?', 'Norra Europa', 'Norge'),
(3, 'Vilken av följande är inte en av Sveriges naturtillgångar?', 'Norra Europa', 'Sverige'),
(4, 'Vilken flod är landets längsta?', 'Norra Europa', 'Finland'),
(5, 'På vilken plats hamnar Ryssland ytmässigt i Europa?', 'Norra Europa', 'Ryssland'),
(6, 'Vad heter landets halvö?', 'Norra Europa', 'Danmark'),
(7, 'Vad heter landets huvudstad?', 'Norra Europa', 'Estland'),
(8, 'Vad heter landets officiella språk?', 'Norra Europa', 'Lettland'),
(9, 'Vad stämmer in på landet?', 'Norra Europa', 'Litauen'),
(10, 'Vad heter landets längsta flod?', 'Västra Europa', 'Irland'),
(11, 'Landet är uppdelat i tre självstyrande riksdelar, vilken av följande är inte en sådan?', 'Västra Europa', 'Storbritannien'),
(12, 'Vilket berg finns inte i Tyskland?', 'Västra Europa', 'Tyskland'),
(13, 'Vad är anmärkningsvärt med landets geografi?', 'Västra Europa', 'Nederländerna'),
(14, 'Vad passar landets klimat?', 'Västra Europa', 'Frankrike'),
(15, 'Hur många invånare hade landet 2016?', 'Västra Europa', 'Belgien'),
(16, 'Vilket språk av följande är ett officiellt språk i landet?', 'Västra Europa', 'Luxemburg'),
(17, 'Vad heter den högsta punkten i landet?', 'Västra Europa', 'Tjeckien'),
(18, 'Vilket sorts statsskick har landet?', 'Västra Europa', 'Schweiz'),
(19, 'På vilken plats hamnar landet innan i ytstorlek?', 'Västra Europa', 'Liechtenstein'),
(20, 'Vad för terräng består landet främst av?', 'Västra Europa', 'Andorra'),
(21, 'Vilken av följande finns i landet?', 'Västra Europa', 'Monaco'),
(22, 'En stor ögrupp ligger i Atlanten, vad heter gruppen?', 'Södra Europa', 'Spanien'),
(23, 'Vad stämmer in på landet?', 'Södra Europa', 'Portugal'),
(24, 'Hur många invånare hade ungefär landet 2016?', 'Södra Europa', 'Italien'),
(25, 'Hur många landskapsregioner består landet av?', 'Södra Europa', 'Österrike'),
(26, 'Vad stämmer in på landet?', 'Södra Europa', 'Slovenien'),
(27, 'Vilken stor flod reser bland annat genom Ungern?', 'Södra Europa', 'Ungern'),
(28, 'Vad heter landets högsta punkt?', 'Södra Europa', 'Kroatien'),
(29, 'Vad stämmer inte överens med landet?', 'Södra Europa', 'Bosnien och Hercegovina'),
(30, 'Vilken sjö delas mellan Montenegro och Albanien?', 'Södra Europa', 'Montenegro'),
(31, 'Vilket sorts klimat råder vid landets kust?', 'Södra Europa', 'Albanien'),
(32, 'Vilket språk är landets officiella språk?', 'Södra Europa', 'Serbien'),
(33, 'Vad är vanligt i landet i vissa delar?', 'Södra Europa', 'Grekland'),
(34, 'Vad heter huvudstaden?', 'Södra Europa', 'Bulgarien'),
(35, 'Vad heter landets längsta flod?', 'Södra Europa', 'Makedonien'),
(36, 'Vad stämmer in på det inre området i landet?', 'Södra Europa', 'Turkiet'),
(37, 'Vad heter huvudstaden?', 'Södra Europa', 'Malta'),
(38, 'Vad heter huvudstaden?', 'Södra Europa', 'San Marino'),
(39, 'På vilken plats hamnar landet ytmässigt i Europa?', 'Södra Europa', 'Vatikanstaden'),
(40, 'Vad är landets viktiga exportvara?', 'Östra Europa', 'Ukraina'),
(41, 'Vad heter huvudstaden?', 'Östra Europa', 'Polen'),
(42, 'Hur många invånare hade landet, ungefär, 2009?', 'Östra Europa', 'Slovakien'),
(43, 'Vilken lång flod är landets längsta flod?', 'Östra Europa', 'Rumänien'),
(44, 'Vilken av följande är inte en av landets storodlingsvaror?', 'Östra Europa', 'Moldavien'),
(45, 'Vad heter landets huvudstad?', 'Östra Europa', 'Vitryssland'),
(46, 'Vilket är inte en av landets officiella språk?', 'Östra Europa', 'Kosovo'),
(47, 'Vilket av följande klimat råder inte i landet?', 'Östra Europa', 'Azerbajdzjan'),
(48, 'Vilket hav har landet kust mot?', 'Östra Europa', 'Georgien'),
(49, 'Hur många kilometer skiljer mellan Sveriges sydligaste och Kazakstans nordligaste punkt?', 'Östra Europa', 'Kazakstan');

--
-- Index för dumpade tabeller
--

--
-- Index för tabell `answers`
--
ALTER TABLE `answers`
  ADD PRIMARY KEY (`answersID`),
  ADD KEY `answersID` (`answersID`);

--
-- Index för tabell `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`QuestionID`),
  ADD UNIQUE KEY `QuestionID` (`QuestionID`);

--
-- AUTO_INCREMENT för dumpade tabeller
--

--
-- AUTO_INCREMENT för tabell `questions`
--
ALTER TABLE `questions`
  MODIFY `QuestionID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- Restriktioner för dumpade tabeller
--

--
-- Restriktioner för tabell `answers`
--
ALTER TABLE `answers`
  ADD CONSTRAINT `answers_ibfk_1` FOREIGN KEY (`answersID`) REFERENCES `questions` (`QuestionID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
