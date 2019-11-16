--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10
-- Dumped by pg_dump version 10.10

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

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: applicants; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.applicants (
    linkedin_email character varying(255) NOT NULL,
    twitter_username character varying(255) NOT NULL
);


ALTER TABLE public.applicants OWNER TO postgres;

--
-- Data for Name: applicants; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.applicants (linkedin_email, twitter_username) FROM stdin;
tes	tes
tandicky30@gmail.com	tandicky
t.williamhalim@gmail.com	fraptorwh
nicdanyos@gmail.com	danofjakarta
tes3	tes3
tes4	tes4
\.


--
-- Name: applicants applicants_linkedin_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.applicants
    ADD CONSTRAINT applicants_linkedin_email_key UNIQUE (linkedin_email);


--
-- Name: applicants applicants_twitter_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.applicants
    ADD CONSTRAINT applicants_twitter_username_key UNIQUE (twitter_username);


--
-- PostgreSQL database dump complete
--

