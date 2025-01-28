--CREATE USER mrqwer WITH PASSWORD 'qwerty';
--ALTER ROLE mrqwer CREATEDB;
--ALTER ROLE mrqwer SUPERUSER;
--
--CREATE DATABASE construction_ecosystem;
-- \c construction_ecosystem;
--
-- -- Create User Table
-- CREATE TABLE IF NOT EXISTS "User" (
--                                       id serial PRIMARY KEY,
--                                       firstname varchar(255),
--     lastname varchar(255),
--     password varchar(255),
--     phone varchar(25),
--     email varchar(255),
--     address varchar(255),
--     user_type varchar(255),
--     city varchar(255),
--     country varchar(255),
--     iin varchar(255),
--     about text,
--     created_at timestamp
--     );
--
-- -- Create Entity Table
-- CREATE TABLE IF NOT EXISTS "Entity" (
--                                         id serial PRIMARY KEY,
--                                         name varchar(255),
--     user_id integer,
--     bin varchar(255),
--     position varchar(255),
--     description text,
--     role varchar(255),
--     FOREIGN KEY (user_id) REFERENCES "User" (id)
--     );
--
-- -- Create Contractor Table
-- CREATE TABLE IF NOT EXISTS "Contractor" (
--                                             id serial PRIMARY KEY,
--                                             entity_id integer,
--                                             FOREIGN KEY (entity_id) REFERENCES "Entity" (id)
--     );
--
-- -- Create Project Table
-- CREATE TABLE IF NOT EXISTS "Project" (
--                                          id serial PRIMARY KEY,
--                                          contractor_id integer,
--                                          address varchar(255),
--     description text,
--     FOREIGN KEY (contractor_id) REFERENCES "Contractor" (id)
--     );
--
-- -- Create Provider Table
-- CREATE TABLE IF NOT EXISTS "Provider" (
--                                           id serial PRIMARY KEY,
--                                           entity_id integer,
--                                           FOREIGN KEY (entity_id) REFERENCES "Entity" (id)
--     );
--
-- -- Create Category Table
-- CREATE TABLE IF NOT EXISTS "Category" (
--                                           id serial PRIMARY KEY,
--                                           name varchar(255)
--     );
--
-- -- Create Product Table
-- CREATE TABLE IF NOT EXISTS "Product" (
--                                          provider_id integer,
--                                          name varchar(255),
--     category_id integer,
--     description text,
--     image bytea,
--     location varchar(255),
--     price float,
--     isnegotiable bool,
--     FOREIGN KEY (provider_id) REFERENCES "Provider" (id),
--     FOREIGN KEY (category_id) REFERENCES "Category" (id)
--     );
--
-- -- Create Constructor Table
-- CREATE TABLE IF NOT EXISTS "Constructor" (
--                                              id serial PRIMARY KEY,
--                                              entity_id integer,
--                                              FOREIGN KEY (entity_id) REFERENCES "Entity" (id)
--     );
--
-- -- Create ConstructionSite Table
-- CREATE TABLE IF NOT EXISTS "ConstructionSite" (
--                                                   id serial PRIMARY KEY,
--                                                   name varchar(255),
--     description text,
--     constructor_id integer,
--     address varchar(255),
--     FOREIGN KEY (constructor_id) REFERENCES "Constructor" (id)
--     );
--
-- -- Create Document Table
-- CREATE TABLE IF NOT EXISTS "Document" (
--                                           constructionssite_id integer,
--                                           name varchar(255),
--     path varchar(255),
--     FOREIGN KEY (constructionssite_id) REFERENCES "ConstructionSite" (id)
--     );
--
-- -- Create Lot Table
-- CREATE TABLE IF NOT EXISTS "Lot" (
--                                      id serial PRIMARY KEY,
--                                      constructor_id integer,
--                                      contractor_id integer,
--                                      image varchar(255),
--     title varchar(255),
--     description text,
--     fromTime timestamp,
--     toTime timestamp,
--     FOREIGN KEY (constructor_id) REFERENCES "Constructor" (id),
--     FOREIGN KEY (contractor_id) REFERENCES "Contractor" (id)
--     );
