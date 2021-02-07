/*Timers Table*/
create table timers
(
    random_Id     varchar(50) not null
        primary key,
    activity_name varchar(50) null,
    amount        int         null,
    untildate     datetime    null
);

INSERT INTO web_project_g11.timers (random_Id, activity_name, amount, untildate) VALUES ('1', 'Wheelchair', 2677, '2021-02-21 10:10:10');
INSERT INTO web_project_g11.timers (random_Id, activity_name, amount, untildate) VALUES ('2', 'trip', 4900, '2021-02-27 10:10:10');
INSERT INTO web_project_g11.timers (random_Id, activity_name, amount, untildate) VALUES ('3', 'Home equipment', 2750, '2021-03-27 10:10:10');

/*Contact Us Table*/
create table connact_us
(
    Email        varchar(50)  not null
        primary key,
    first_Name   varchar(50)  null,
    last_name    varchar(50)  null,
    phone_number int          null,
    Text_message varchar(100) null
);

INSERT INTO web_project_g11.connact_us (Email, first_Name, last_name, phone_number, Text_message) VALUES ('ahmada@post', 'ahmad', 'atamleh', 455455454, 'find job ');
INSERT INTO web_project_g11.connact_us (Email, first_Name, last_name, phone_number, Text_message) VALUES ('amera@gmail.com', 'yosef', 'leve', 522977383, 'its anew ');
INSERT INTO web_project_g11.connact_us (Email, first_Name, last_name, phone_number, Text_message) VALUES ('bar@gmail', 'bar', 'leve', 563688888, 'anew job');
INSERT INTO web_project_g11.connact_us (Email, first_Name, last_name, phone_number, Text_message) VALUES ('gal@post.bgu.ac.il', 'GAL', 'ZANO', 544444544, 'find a new jop');
INSERT INTO web_project_g11.connact_us (Email, first_Name, last_name, phone_number, Text_message) VALUES ('haytham@dsd', 'noam', 'dsa', 833822383, 'find job ');
INSERT INTO web_project_g11.connact_us (Email, first_Name, last_name, phone_number, Text_message) VALUES ('haytham@post', 'haytham', 'khmasi', 233944232, 'get the');
INSERT INTO web_project_g11.connact_us (Email, first_Name, last_name, phone_number, Text_message) VALUES ('hend@pdkd', 'hend', 'khmaisi', 433922934, 'find job ');
INSERT INTO web_project_g11.connact_us (Email, first_Name, last_name, phone_number, Text_message) VALUES ('hmam@post', 'hmam', 'khmaisi', 399499393, 'send a');
INSERT INTO web_project_g11.connact_us (Email, first_Name, last_name, phone_number, Text_message) VALUES ('hmam@xxx', 'hmam', 'kh', 522977818, 'its a new job');
INSERT INTO web_project_g11.connact_us (Email, first_Name, last_name, phone_number, Text_message) VALUES ('khaled@gmail', 'khaled', 'khaled', 488344334, 'anew job');
INSERT INTO web_project_g11.connact_us (Email, first_Name, last_name, phone_number, Text_message) VALUES ('lee@post.bgu', 'lee', 'kohen', 522977844, 'get new ');
INSERT INTO web_project_g11.connact_us (Email, first_Name, last_name, phone_number, Text_message) VALUES ('mahmod@post.bgu.ac.il', 'Mahmod', 'saleh', 522777222, 'anew job');
INSERT INTO web_project_g11.connact_us (Email, first_Name, last_name, phone_number, Text_message) VALUES ('mohamd@gmail.com', 'mohamad', 'khateb', 522933848, 'find job ');

/*Credit Card Table*/

create table credit_card
(
    Id                 varchar(50) not null
        primary key,
    Email              varchar(50) null,
    first_Name         varchar(50) null,
    last_name          varchar(50) null,
    phone_number       int         null,
    amount             int         null,
    donation_type      varchar(50) null,
    cerdit_holder_name varchar(50) null,
    card_number        varchar(50) null,
    expiration_year    int         null,
    expiration_month   int         null,
    CCV                int         null
);

INSERT INTO web_project_g11.credit_card (Id, Email, first_Name, last_name, phone_number, amount, donation_type, cerdit_holder_name, card_number, expiration_year, expiration_month, CCV) VALUES ('232323232', 'moatazj@post', 'moataz', 'jabaren', 495959432, 78, 'Monthly donation', 'moataz', '3293939439439439', 2022, 3, 333);
INSERT INTO web_project_g11.credit_card (Id, Email, first_Name, last_name, phone_number, amount, donation_type, cerdit_holder_name, card_number, expiration_year, expiration_month, CCV) VALUES ('318589124', 'haythamk@post', 'haytham', 'khmais', 503434333, 550, 'Monthly donation', 'haytham', '4564545723435456', 2022, 3, 323);
INSERT INTO web_project_g11.credit_card (Id, Email, first_Name, last_name, phone_number, amount, donation_type, cerdit_holder_name, card_number, expiration_year, expiration_month, CCV) VALUES ('323234343', 'mahmod@post', 'mahmod', 'saleh', 533433434, 500, 'One-time donation', 'mahmod', '3453343495544345', 2024, 3, 333);
INSERT INTO web_project_g11.credit_card (Id, Email, first_Name, last_name, phone_number, amount, donation_type, cerdit_holder_name, card_number, expiration_year, expiration_month, CCV) VALUES ('324545456', 'moataz@post', 'moataz', 'jabaren', 533944242, 100, 'One-time donation', 'moataz', '5456645675574358', 2029, 10, 455);
INSERT INTO web_project_g11.credit_card (Id, Email, first_Name, last_name, phone_number, amount, donation_type, cerdit_holder_name, card_number, expiration_year, expiration_month, CCV) VALUES ('432343233', 'khaled@post', 'khaled', 'khaled', 543443343, 222, 'One-time donation', 'khaled', '4354343435456564', 2023, 5, 422);
INSERT INTO web_project_g11.credit_card (Id, Email, first_Name, last_name, phone_number, amount, donation_type, cerdit_holder_name, card_number, expiration_year, expiration_month, CCV) VALUES ('434534234', 'gal@post.bgu.sc.il', 'GAl', 'zano', 522977813, 250, 'One-time donation', 'gal', '1233454654364445', 2022, 7, 234);
INSERT INTO web_project_g11.credit_card (Id, Email, first_Name, last_name, phone_number, amount, donation_type, cerdit_holder_name, card_number, expiration_year, expiration_month, CCV) VALUES ('435345453', 'husam@gmail.com', 'husam', 'khmaisi', 544544678, 150, 'One-time donation', 'husam', '3454565467656786', 2025, 6, 567);
INSERT INTO web_project_g11.credit_card (Id, Email, first_Name, last_name, phone_number, amount, donation_type, cerdit_holder_name, card_number, expiration_year, expiration_month, CCV) VALUES ('473282342', 'hussen@post.bgu.ac.il', 'huseen', 'alshukaerat', 522944838, 450, 'Monthly donation', 'hussen', '4583843485439843', 2024, 6, 223);

/*To Volunteer Table*/
create table to_volunteer
(
    Email           varchar(50) not null
        primary key,
    first_Name      varchar(50) null,
    last_name       varchar(50) null,
    phone_number    int         null,
    Dob             date        null,
    Gender          varchar(50) null,
    past_experience varchar(5)  null
);

INSERT INTO web_project_g11.to_volunteer (Email, first_Name, last_name, phone_number, Dob, Gender, past_experience) VALUES ('dasd@das', 'sadsa', 'sadd', 548877372, '1998-09-28', 'f', 'no');
INSERT INTO web_project_g11.to_volunteer (Email, first_Name, last_name, phone_number, Dob, Gender, past_experience) VALUES ('haytham@kh', 'haythan', 'khmakd', 766488374, '1999-09-29', 'f', 'no');
INSERT INTO web_project_g11.to_volunteer (Email, first_Name, last_name, phone_number, Dob, Gender, past_experience) VALUES ('hussen@gmail.com', 'hussen', 'bsam', 522933842, '1998-09-28', 'F', 'yes');
INSERT INTO web_project_g11.to_volunteer (Email, first_Name, last_name, phone_number, Dob, Gender, past_experience) VALUES ('hussen@post', 'huassen', 'alshukaerat', 574837453, '1996-10-29', 'M', 'no');
INSERT INTO web_project_g11.to_volunteer (Email, first_Name, last_name, phone_number, Dob, Gender, past_experience) VALUES ('qweqwe@qweqwe', 'qweqwe', 'qweqwe', 522988384, '2002-12-31', 'M', 'yes');