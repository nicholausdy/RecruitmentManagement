--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10
-- Dumped by pg_dump version 12.0

-- Started on 2019-11-29 16:18:48

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

--
-- TOC entry 196 (class 1259 OID 16406)
-- Name: twittertable; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.twittertable (
    account_username character varying(50) NOT NULL,
    account_name character varying(50),
    account_description character varying(255),
    account_status integer,
    account_friends integer,
    account_followers integer
);


ALTER TABLE public.twittertable OWNER TO postgres;

--
-- TOC entry 2791 (class 0 OID 16406)
-- Dependencies: 196
-- Data for Name: twittertable; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.twittertable (account_username, account_name, account_description, account_status, account_friends, account_followers) FROM stdin;
\.


--
-- TOC entry 2669 (class 2606 OID 16410)
-- Name: twittertable twittertable_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.twittertable
    ADD CONSTRAINT twittertable_pkey PRIMARY KEY (account_username);


-- Completed on 2019-11-29 16:18:48

--
-- PostgreSQL database dump complete
--

