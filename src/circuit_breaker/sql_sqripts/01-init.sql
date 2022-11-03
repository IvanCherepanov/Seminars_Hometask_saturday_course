USE cism;

--DROP TABLE IF EXISTS pet_type;
CREATE TABLE IF NOT EXISTS pet_type
(
    id    SERIAL NOT NULL PRIMARY KEY ,
    pet_type_name  VARCHAR(256) NOT NULL
    );

insert into pet_type (id, pet_type_name) values (1, 'Dasypus novemcinctus');
insert into pet_type (id, pet_type_name) values (2, 'Theropithecus gelada');
insert into pet_type (id, pet_type_name) values (3, 'Aonyx cinerea');
insert into pet_type (id, pet_type_name) values (4, 'Crotalus adamanteus');
insert into pet_type (id, pet_type_name) values (5, 'Dicrurus adsimilis');
insert into pet_type (id, pet_type_name) values (6, 'Microcebus murinus');
insert into pet_type (id, pet_type_name) values (7, 'Columba palumbus');
insert into pet_type (id, pet_type_name) values (8, 'Odocoileus hemionus');
insert into pet_type (id, pet_type_name) values (9, 'Anastomus oscitans');
insert into pet_type (id, pet_type_name) values (10, 'Physignathus cocincinus');
insert into pet_type (id, pet_type_name) values (11, 'Anthropoides paradisea');
insert into pet_type (id, pet_type_name) values (12, 'Callipepla gambelii');
insert into pet_type (id, pet_type_name) values (13, 'Tadorna tadorna');
insert into pet_type (id, pet_type_name) values (14, 'Zosterops pallidus');
insert into pet_type (id, pet_type_name) values (15, 'Dipodomys deserti');
insert into pet_type (id, pet_type_name) values (16, 'Gymnorhina tibicen');
insert into pet_type (id, pet_type_name) values (17, 'Bubo sp.');
insert into pet_type (id, pet_type_name) values (18, 'Kobus defassa');
insert into pet_type (id, pet_type_name) values (19, 'Phoenicopterus chilensis');
insert into pet_type (id, pet_type_name) values (20, 'Ara macao');