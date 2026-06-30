--
-- PostgreSQL database dump
--

\restrict dUwRsOUpfYbAJEqkYl444BcKCVtJjUq7D7iU6JeH5gMnhbueRDoMGItGWtbIeSN

-- Dumped from database version 18.4
-- Dumped by pg_dump version 18.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: goal_skills; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.goal_skills (
    goal_id integer NOT NULL,
    skill_id integer NOT NULL
);


ALTER TABLE public.goal_skills OWNER TO postgres;

--
-- Name: goals; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.goals (
    goal_id integer NOT NULL,
    goal_name character varying(50)
);


ALTER TABLE public.goals OWNER TO postgres;

--
-- Name: skills; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.skills (
    skill_id integer NOT NULL,
    skill_name character varying(50),
    reason text
);


ALTER TABLE public.skills OWNER TO postgres;

--
-- Name: user_skills; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_skills (
    user_id integer NOT NULL,
    skill_id integer NOT NULL
);


ALTER TABLE public.user_skills OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    name character varying(50),
    email character varying(100),
    hashed_password character varying(255),
    goal_id integer
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_user_id_seq OWNER TO postgres;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: goal_skills; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.goal_skills (goal_id, skill_id) FROM stdin;
1	1
1	2
1	3
1	4
1	5
1	6
1	7
1	8
1	9
1	12
1	13
1	14
1	15
1	22
2	1
2	2
2	3
2	7
2	8
2	9
2	10
2	11
3	1
3	2
3	4
3	5
3	6
3	7
3	8
3	12
3	13
3	14
3	15
3	25
3	26
4	1
4	2
4	4
4	5
4	6
4	7
4	8
4	12
4	13
4	14
4	15
4	16
4	17
4	18
4	19
4	20
4	21
5	1
5	2
5	3
5	4
5	5
5	25
5	26
5	27
5	28
6	2
6	8
6	9
6	10
6	11
7	1
7	3
7	4
7	5
7	23
7	24
7	25
7	26
7	28
7	30
8	1
8	3
8	4
8	5
8	22
8	23
8	24
8	25
8	26
8	30
9	1
9	4
9	13
9	22
9	25
9	26
9	27
10	1
10	8
10	13
10	16
10	17
10	18
10	19
10	20
10	21
\.


--
-- Data for Name: goals; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.goals (goal_id, goal_name) FROM stdin;
1	Data Scientist
2	Data Analyst
3	Machine Learning Engineer
4	AI Engineer
5	Data Engineer
6	Business Analyst
7	Backend Python Developer
8	Full Stack Python Developer
9	MLOps Engineer
10	NLP Engineer
\.


--
-- Data for Name: skills; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.skills (skill_id, skill_name, reason) FROM stdin;
1	Python	Python is the foundation of data science, machine learning, and automation.
2	SQL	SQL is used to retrieve, filter, and manage data stored in databases.
3	PostgreSQL	PostgreSQL is a powerful relational database used in real-world applications.
4	Git	Git helps track code changes and manage project versions.
5	GitHub	GitHub is used to store projects, collaborate, and showcase your work.
6	NumPy	NumPy provides fast numerical computing and array operations.
7	Pandas	Pandas is used for data cleaning, manipulation, and analysis.
8	Statistics	Statistics helps you understand data patterns and build reliable models.
9	Data Visualization	Data Visualization helps communicate insights using charts and graphs.
10	Excel	Excel is widely used for data analysis and business reporting.
11	Power BI	Power BI is used to create interactive dashboards and business reports.
12	Scikit-learn	Scikit-learn provides tools to build and evaluate machine learning models.
13	Machine Learning	Machine Learning enables computers to learn patterns and make predictions.
14	Feature Engineering	Feature Engineering improves model performance by creating useful features.
15	Model Evaluation	Model Evaluation helps measure and compare model performance.
16	Deep Learning	Deep Learning is used for complex tasks like image and speech recognition.
17	TensorFlow	TensorFlow is a popular framework for building deep learning models.
18	PyTorch	PyTorch is widely used for deep learning research and development.
19	Natural Language Processing	Natural Language Processing enables computers to understand human language.
20	Generative AI	Generative AI creates new content such as text, images, and code.
21	Prompt Engineering	Prompt Engineering helps obtain better results from AI models.
22	Streamlit	Streamlit helps build interactive data science web applications quickly.
23	Flask	Flask is a lightweight Python framework for building web applications.
24	FastAPI	FastAPI is used to build fast and modern REST APIs with Python.
25	Docker	Docker packages applications into portable containers for deployment.
26	Linux	Linux is widely used for servers, cloud computing, and development.
27	AWS Basics	AWS Basics introduces cloud services used in modern applications.
28	MongoDB	MongoDB stores unstructured and flexible NoSQL data.
29	Data Structures & Algorithms	Data Structures and Algorithms improve problem-solving and coding efficiency.
30	System Design Basics	System Design Basics help build scalable and reliable software systems.
\.


--
-- Data for Name: user_skills; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_skills (user_id, skill_id) FROM stdin;
14	1
14	2
14	4
14	3
14	5
14	6
14	7
14	8
14	9
14	12
14	13
15	2
15	1
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (user_id, name, email, hashed_password, goal_id) FROM stdin;
14	Dhrub Gupta	guptadhrub233@gmail.com	$2b$12$jglU0kmeIx1bO8UyP6tsx.UpZ5y3qFELiij0nWdr00Jc769nrHpMS	1
15	Tanmay Gupta	tanmay@gmail.com	$2b$12$nKpt2YHl2QECFsP3FjBgAuGAWenaIfRUXJIgqYAGoQI31KYWDD926	3
\.


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_user_id_seq', 15, true);


--
-- Name: goal_skills goal_skills_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.goal_skills
    ADD CONSTRAINT goal_skills_pkey PRIMARY KEY (goal_id, skill_id);


--
-- Name: goals goals_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.goals
    ADD CONSTRAINT goals_pkey PRIMARY KEY (goal_id);


--
-- Name: skills skills_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.skills
    ADD CONSTRAINT skills_pkey PRIMARY KEY (skill_id);


--
-- Name: user_skills user_skills_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_skills
    ADD CONSTRAINT user_skills_pkey PRIMARY KEY (user_id, skill_id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: goal_skills goal_skills_goal_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.goal_skills
    ADD CONSTRAINT goal_skills_goal_id_fkey FOREIGN KEY (goal_id) REFERENCES public.goals(goal_id);


--
-- Name: goal_skills goal_skills_skill_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.goal_skills
    ADD CONSTRAINT goal_skills_skill_id_fkey FOREIGN KEY (skill_id) REFERENCES public.skills(skill_id);


--
-- Name: user_skills user_skills_skill_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_skills
    ADD CONSTRAINT user_skills_skill_id_fkey FOREIGN KEY (skill_id) REFERENCES public.skills(skill_id);


--
-- Name: user_skills user_skills_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_skills
    ADD CONSTRAINT user_skills_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: users users_goal_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_goal_id_fkey FOREIGN KEY (goal_id) REFERENCES public.goals(goal_id);


--
-- PostgreSQL database dump complete
--

\unrestrict dUwRsOUpfYbAJEqkYl444BcKCVtJjUq7D7iU6JeH5gMnhbueRDoMGItGWtbIeSN

