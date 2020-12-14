# Descoberta de Conhecimento com Python

Este repositório faz referência à um trabalho sobre KDD (Knowledge Discovery in Databases) da disciplina de Banco de Dados II. Durante o trabalho foram abordadas todas as etapas de KDD, tendo como base de dados um arquivo com pedidos de uma pizzaria.


<h2> Seleção </h2>

SQL para criação do banco pizzaria e da tabela pedidos_full. Os dados para inserção podem ser importados através do <b>.csv</b> disponibilizado na pasta <b>selecao</b> ou através do SQL de inserção contido do arquivo <b>database.sql</b>

```
CREATE DATABASE  IF NOT EXISTS `pizzaria`;
USE `pizzaria`;

--
-- Table structure for table `pedidos`
--

DROP TABLE IF EXISTS `pedidos_full`;

CREATE TABLE `pedidos_full` (
  `numero` int(11) NOT NULL,
  `data_pedido` date DEFAULT NULL,
  `hora_pedido` time DEFAULT NULL,
  `cliente` varchar(20) DEFAULT NULL,
  `endereco` varchar(20) DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `tipo_entrega` varchar(20) DEFAULT NULL,
  `valor_pizza` float DEFAULT NULL,
  `valor_borda` float DEFAULT NULL,
  `valor_refrigerante` float DEFAULT NULL,
  `valor_entrega` float DEFAULT NULL,
  `valor_total` float DEFAULT NULL,
  `hora_entrega` time DEFAULT NULL,
  `tempo` time DEFAULT NULL,
  PRIMARY KEY (`numero`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

```
