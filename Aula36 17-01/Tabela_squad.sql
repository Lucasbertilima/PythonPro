CREATE TABLE SQUADS_DEV (
codigo INT(11) NOT NULL AUTO_INCREMENT,
NAME_SQUAD VARCHAR(100) NOT NULL,
descricao VARCHAR(200) NOT NULL,
numero_pessoas INT(5) NOT NULL,
lingugemBackEnd VARCHAR(100) NOT NULL,
linguagemFrontEnd VARCHAR(100) NOT NULL,
PRIMARY KEY (CODIGO)
);

-----------------------------

CREATE TABLE SQUAD (
ID INT(11) NOT NULL AUTO_INCREMENT,
NAME_SQUAD VARCHAR(100) NOT NULL,
DESCRICAO VARCHAR(200) NOT NULL,
NUMERO_PESSOAS INT(5) NOT NULL,
ID_BACKEND INT(11) NOT NULL,
ID_FRONTEND INT(11) NOT NULL,
PRIMARY KEY (ID),
FOREIGN KEY (ID_BACKEND) REFERENCES BACKEND (ID),
FOREIGN KEY (ID_FRONTEND) REFERENCES FRONTEND (ID)
);

CREATE TABLE BACKEND (
ID INT(11) NOT NULL AUTO_INCREMENT,
LINGUAGEMBACKEND VARCHAR(200) NOT NULL,
PRIMARY KEY (ID)
);

CREATE TABLE FRONTEND (
ID INT(11) NOT NULL AUTO_INCREMENT,
LINGUAGEMFRONTEND VARCHAR(200) NOT NULL,
PRIMARY KEY (ID)
);

CREATE TABLE SGBDS (
ID INT(11) NOT NULL AUTO_INCREMENT,
NOME VARCHAR(200) NOT NULL,
PRIMARY KEY (ID)  
);