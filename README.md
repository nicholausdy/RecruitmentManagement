# Tugas Besar Teknologi Sistem Terintegrasi (II3160)
## Recruitment Management
### Overview
A web-based application that enables job applicants to submit their professional and social data based on their LinkedIn and Twitter data (using APIs), while recruiters or Human Resources could see the aforementioned applicants' professional and social data.
### Created By :
Kelompok 20:
1. William Halim / 18217021 (Commit name: WilliamHalim98)
2. Nicholaus Danispadmanaba Y / 18217028 (Commmit name: nicholausdy or osboxes.org or Cloud User)
### Table of Contents
* [Overview](https://github.com/nicholausdy/RecruitmentManagement#overview)
* [Created by](https://github.com/nicholausdy/RecruitmentManagement#created-by-)
* [Functionalities](https://github.com/nicholausdy/RecruitmentManagement#functionalities)
* [Stack](https://github.com/nicholausdy/RecruitmentManagement#stack)
* [System Requirements](https://github.com/nicholausdy/RecruitmentManagement#system-requirements)
  - [Without Installation](https://github.com/nicholausdy/RecruitmentManagement#a-without-installation)
  - [With Installation](https://github.com/nicholausdy/RecruitmentManagement#b-with-installation)
* [List of Endpoints](https://github.com/nicholausdy/RecruitmentManagement#list-of-endpoints)
* [Usage](https://github.com/nicholausdy/RecruitmentManagement#usage)
* [Log Act](https://github.com/nicholausdy/RecruitmentManagement#log-act)
### Functionalities
1. Job applicants could submit their LinkedIn email or account ID.
2. Job applicants could submit their Twitter username.
3. Job applicants could submit their photos.
4. Recruiters or Human Resources could see applicants' professional data based on LinkedIn API.
5. Recruiters or Human Resources could see applicants' social data based on Twitter API.
6. Recruiters or Human Resources could see applicants' uploaded photos.
### Stack
1. Virtual machine: Amazon Web Service EC2 t2.micro
2. Operating system: Red Hat Enterprise Linux (RHEL) 8
3. Web server: Nginx 1.14.1
4. Front End: HTML, CSS, native JavaScript, and bootstrao
5. Back End: Python 3.6.8 Base HTTP Server
6. Database: PostgreSQL 10.10
### System Requirements
#### A. Without Installation
1. Browser with support for HTML rendering and JavaScript.
#### B. With Installation
1. Operating system: RHEL 8 or CentOS 8
2. Interpreter: Python 3.6.8
3. RDBMS: PostgreSQL 10.10
4. Versioning: Git
### List of Endpoints
| Method | Host | Path | Function |
| :---: | :---: | :---: | :---: |
| GET| 3.227.193.57:8001 | /applicants |Show list of LinkedIn email and Twitter username |
| GET| 3.227.193.57:8001 | /users/all |Show list of all LinkedIn profiles with all attributes (general, workplace, and education | /users/accounts/general | Show list of all LinkedIn profiles with only general attribute |
| GET| 3.227.193.57:8001 | /users/accounts/education | Show list of all LinkedIn profiles with only education attribute |
| GET| 3.227.193.57:8001 | /users/accounts/workplace | Show list of all LinkedIn profiles with only workplace attribute |
| GET| 3.227.193.57:8001 | /user/account/general/email/'LinkedIn email' | Show a LinkedIn profile with the provided email with only general attribute |
| GET| 3.227.193.57:8001 | /user/account/education/email/'LinkedIn email' | Show a LinkedIn profile with the provided email with only education attribute |
| GET| 3.227.193.57:8001 | /user/account/workplace/email/'LinkedIn email' | Show a LinkedIn profile with the provided email with only workplace attribute |
| GET| 3.227.193.57:8001 | /user/account/general/'LinkedIn ID' | Show a LinkedIn profile with the provided ID with only general attribute |
| GET| 3.227.193.57:8001 | /user/account/education/'LinkedIn ID' | Show a LinkedIn profile with the provided ID with only education attribute |
| GET| 3.227.193.57:8001 | /user/account/workplace/'LinkedIn ID' | Show a LinkedIn profile with the provided ID with only workplace attribute |
| POST | 3.227.193.57:8001 | /applicants | Insert JSON containing LinkedIn email and Twitter username to register applicants to system |
| GET | 3.227.193.57:8002 | /users/accounts/profile/'Twitter username' | Show a Twitter profile information based on the provided username |
| GET | 3.227.193.57:8002 | /users/accounts/stats/'Twitter username' | Show Twitter account statistics based on the provided username |
| GET | 3.227.193.57:8002 | /users/accounts/tweets/'Twitter username' | Show last 5 tweets of a Twitter account based on the provided username |
| PUT | 3.227.193.57:8002 | /users/accounts/photo/'Twitter username' | Upload photo |

### Usage
1. For Human Resource page, access this URL: http://3.227.193.57:8003
2. For applicants' page, access this URL: http://3.227.193.57:8003/applicants.html
### Log Act
1. November 5: Pembuatan rencana manajemen proyek aplikasi Recruitment Management (Done by: Nicholaus Danispadmanaba Y and William Halim)
2. November 12: Revisi rencana manajemen proyek aplikasi (Done by: Nicholaus Danispadmanaba Y and William Halim)
3. November 16: Revisi LinkedIn API untuk memudahkan integrasi dengan front end (Done by: Nicholaus Danispadmanaba Y)
4. November 16: Deployment LinkedIn API hasil revisi ke AWS EC2 (Done by: Nicholaus Danispadmanaba Y)
5. November 29: Deployment LinkedIn API dengan AWS EC2 dan Nginx reverse proxy (Done by: Nicholaus Danispadmanaba Y)
6. November 29: Revisi source code Twitter server (Done by: William Halim)
7. November 29: Menambah file database Twitter (Done by: William Halim)
8. November 29: Revisi modul pengambilan data untuk Twitter API (Done by: William Halim)
9. November 29: Deployment Twitter API dengan AWS EC2 dan Nginx reverse proxy (Done by: Nicholaus Danispadmanaba Y)
10. November 30: Finalisasi tampilan Recruitment Management (Done by: William Halim)
11. November 30: Integrasi front-end dengan back-end (Done by: William Halim and Nicholaus Danispadmanaba Y)
12. November 30: Penambahan fungsi upload photo pada front-end dan back-end (Done by: Nicholaus Danispadmanaba Y)
13. Desember 1: Testing dan debugging aplikasi (Done by: Nicholaus Danispadmanaba Y and William Halim)
14. Desember 1: Deployment tampilan front end ke AWS EC2 dengan web server Nginx (Done by: Nicholaus Danispadmanaba Y)
15. Desember 2: Pembuatan laporan akhir
