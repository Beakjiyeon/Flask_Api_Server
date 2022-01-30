# Flask API Server

### Purpose
- Flask를 사용하여 요구사항에 맞는 서비스를 제공하는 API Server 개발

### Specification
- Python 3.6+
- Git
- Flask 2.0+
- Flask-SQLAlchemy

### Requirement
1. Layered Architecture


2. 구현 서비스 상세
    
    a. 해당 API는 임의의 서비스가 보내온 정보들을 처리하는 API (CRUD)
    
    b. 보내온 데이터 정보
        
        i. 해당 데이터를 보내온 서비스 이름 (ServiceId)
        
        1. 해당 서비스를 호출하는 서비스 (QueryService, BoardService, MonitoringService)
        
        ii. 데이터 아이디 (DataId)
        
        iii. 데이터 정보 (Content - Json Format Text)
        
        iv. 최초 등록 시간 / 업데이트 시간 (UpdateDatetime / RegistDatetime)
    
    c. 서비스가 보내온 데이터는 임의의 가상의 데이터이므로 자유롭게 테스트

3. 서비스 테스트 구현 (Integration Test)

4. 응답 포맷 공통화 (Overrided Response)

5. 만약에 API가 version 2를 제공하고 현재 버전을 유지해야하는 상황에서 어떻게 설계, 구현 
6. 요청이 들어올때마다 들어온 아이피, 서비스, 걸린시간, 응답상태같은 정보를 로그로 남기는 기능 구현


