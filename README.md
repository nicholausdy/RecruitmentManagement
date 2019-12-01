# Tugas Besar Teknologi Sistem Terintegrasi (II3160)
## Recruitment Management
### Overview
A web-based application that enables job applicants to submit their professional and social data based on their LinkedIn and Twitter data (using APIs), while recruiters or Human Resources could see the aforementioned applicants' professional and social data.
### Created By :
Kelompok 20:
1. William Halim / 18217021 (Commit name: WilliamHalim98)
2. Nicholaus Danispadmanaba Y / 18217028 (Commmit name: osboxes.org or Cloud User)
### Table of Contents
* [Overview](https://github.com/nicholausdy/RecruitmentManagement/new/master?readme=1#overview)
* [Created by](https://github.com/nicholausdy/RecruitmentManagement/new/master?readme=1#created-by-)
* [Functionalities](https://github.com/nicholausdy/RecruitmentManagement/new/master?readme=1#functionalities)
* [Stack](https://github.com/nicholausdy/RecruitmentManagement/new/master?readme=1#stack)
* [System Requirements](https://github.com/nicholausdy/RecruitmentManagement/new/master?readme=1#system-requirements)
  - [Without Installation](https://github.com/nicholausdy/RecruitmentManagement/new/master?readme=1#a-without-installation)
  - [With Installation](https://github.com/nicholausdy/RecruitmentManagement/new/master?readme=1#b-with-installation)
* [Usage](https://github.com/nicholausdy/RecruitmentManagement/new/master?readme=1#usage)
* [Log Act](https://github.com/nicholausdy/RecruitmentManagement/new/master?readme=1#log-act)
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
11. Desember 1: Testing dan debugging aplikasi (Done by: Nicholaus Danispadmanaba Y and William Halim)
12. Desember 1: Deployment tampilan front end ke AWS EC2 dengan web server Nginx (Done by: Nicholaus Danispadmanaba Y)
13. Desember 1: Pembuatan laporan akhir
