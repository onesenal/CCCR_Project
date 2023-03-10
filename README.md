# Kubernetes DevSecOps Toolchain Service

 프로젝트명 | 기술문서 | 발표자료 | Git Repository |프로젝트 기간 
:-------------: | :-------------: | :-------------: | :-------------: | :-------------:
여행 정보 웹 서비스 구현  | [Click](https://docs.google.com/document/d/1FUeSGaLt1wloDKpdShsZnwXNY3AuxZJV/edit?usp=sharing&ouid=106249240240065525675&rtpof=true&sd=true)  | [Click](https://docs.google.com/presentation/d/133Ozt6W4GKmPawqorqBASwCN6YqySAa9/edit?usp=sharing&ouid=106249240240065525675&rtpof=true&sd=true) | [Click](https://github.com/onesenal/CCCR_Project.git) | 22.12.12~22.12.30

## Contents:
  - [Intro](#Intro)
  - [Architecture](#Architecture)
  - [Organization](#Organization)
  - [Process](#Process)
  - [Documents](#Documents)
  - [Result](#Result)
  - [Feedback](#Feedback)

#### Intro
```sh
여행 정보 웹 서비스 구현이란?
  여행 관련 프로젝트를 지정하게 된 동기는 최근 COVID-19가 엔데믹으로 접어들면서 해외여행에 대한 수요가 증가하고 있기 때문입니다. 
  위 그래프에 따르면, 2020년 상반기에 COVID-19가 전세계로 확산되면서 2019년 대비 해외 여행객이 현저히 줄어들었으나 
  2021년 하반기부터 해외 여행객이 다시 코로나 전 수준을 향해 회복되고 있습니다. 이로 인해 해외 여행객 및 사용자에게 여행 시 숙지해야 할 사항을 제공하고 
  요구사항을 충족시킬 수 있는 방법을 모색하여 사용자에게 서비스를 제공하였습니다. 
```
#### Architecture
![](https://github.com/onesenal/CCCR_Project/blob/main/Picture/Architecture01.png)

#### Organization
![](https://github.com/onesenal/CCCR_Project/blob/main/Picture/Organization01.PNG)

#### Process
![](https://github.com/onesenal/CCCR_Project/blob/main/Picture/Schedule.PNG)
기간 | 작업
:-------------: | :-------------:
1주차  | 주제 선정 및 역할 분담
2주차  | 인프라 구축 및 개발
3주차  | 통합 테스트
  

#### Documents
유형 | 파일 | 파일내용
:-------------: | :-------------: | :-------------:
PowerPoint | [착수보고서](https://docs.google.com/presentation/d/1OtbHWVlUlpeUjpgk9LiI8YW-vreQ55d1/edit?usp=sharing&ouid=106249240240065525675&rtpof=true&sd=true) | 착수보고발표 문서입니다.
Google Docs | [1주차 주간보고](https://docs.google.com/presentation/d/13oVmL9rcOMAO42rxr-eAu5MVVy18o3Zw/edit?usp=sharing&ouid=106249240240065525675&rtpof=true&sd=true) | 1주차 주간발표 문서입니다.
Google Docs | [2주차 주간보고](https://docs.google.com/presentation/d/1ZSNOidpNiWG1RrAanJV38LZgoVNdk5Le/edit?usp=sharing&ouid=106249240240065525675&rtpof=true&sd=true) | 2주차 주간발표 문서입니다.
Google Docs | [기술문서](https://docs.google.com/document/d/1FUeSGaLt1wloDKpdShsZnwXNY3AuxZJV/edit?usp=sharing&ouid=106249240240065525675&rtpof=true&sd=true) | 프로젝트 기술문서 입니다.
Google Docs | [최종발표자료](https://docs.google.com/presentation/d/133Ozt6W4GKmPawqorqBASwCN6YqySAa9/edit?usp=sharing&ouid=106249240240065525675&rtpof=true&sd=true) | 최종발표 문서입니다.

#### Results
![](https://github.com/onesenal/CCCR_Project/blob/main/Video/CCCR_Project.gif)

#### Feedback
번호 | 유형 | 문제 | 추후 과제
:----: | :------: | :-------------: | :-------------:
1 | 인프라 | 리소스(메모리) 문제로 인한 K8s 환경(MySQL Operator, 모니터링, 로깅)을 갖추는데 제약 | 리소스 환경 또는 EKS환경 등에 대한 고민이 필요
2 | 서비스 | 웹 서비스에 대한 개발 완성도 미흡 | 서비스를 구현하는데 있어서 개발 기술에 대한 이해 필요
3 | 조직 | 협업 프로젝트에 대한 이해 부족 | 각각의 작업물을 통합시키는데 있어서 문제가 발생되고 업무 진행에 대한 보고 및 소통에 대한 문제를 해결하기 위한 업무 체계 확립이 필요
