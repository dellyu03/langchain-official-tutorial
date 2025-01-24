# 🛠️ Build a simple LLM application with chat models and prompt templates

# 🦜 LangChain Offical Docs Tutorial 1편

## 🤖 Make What?
- 영어 번역 프로그램

## 🎯 Goal
- Language Model 사용
- prompt template 사용
- LangSmith를 활용한 디버깅 및 애플리케이션 추적

<br>

## I. Set-up 💾
- #### Tutorial
```
pip install langchain
```

- LangSmith 환경 설정
```
export LANGSMITH_TRACING="true"
export LANGSMITH_API_KEY="..."
```



- #### 추가
```shell
pip install python-dotenv==1.0.0
```

```python
from dotenv import load_dotenv

load_dotenv()
```
<br>

## II. Using Language Models 🤖

- ### [ChatModel](https://python.langchain.com/docs/concepts/chat_models/)
    - 랭체인에서 제공하는 다양한 언어 모델 인터페이스
    - 일관된 인터페이스로 다양한 모델전이를 지원
    - 메시지 기반 통신 (시스템/사용자 메시지 구분)
    - Runnable의 인스턴스임
- ### [Runnable](https://python.langchain.com/docs/concepts/runnables/)
    - 실행가능한 컴포넌트를 추상화한 인터페이스
    - 일관된 메서드 제공
    - 조합 가능성

> message를 `.invoke` 메서드를 활용하여 간단하게 AI 모델을 호출할 수 있음

- invoke 메서드는 Runnable 인터페이스의 컴포넌트를 실행하는 역할을 함

- ### [messages](https://python.langchain.com/docs/concepts/messages/)
    - LLM 대화를 구조화하는 기본 단위
    - 다양한 타입으로 메시지 구분 (ex. [SystemMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html), [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html), AIMessage)
    
- LangChainSmith에서 로그를 확인 가능함

- ChatModel은 메시지 오브젝트를 받아 메시지 오브젝트를 생성하여 아웃풋으로 반환함
- message 오브젝트는 conversation [roles](https://python.langchain.com/docs/concepts/messages/#role)와 중요한 정보, tool calls, 토큰 사용량 등을 반환함

- ### Streaming
    - ChatModel이 Runnable이라 async/streaming mode가 포함되어 있음

<br>

## III. Prompt Templates ⌨️

- message는 user input과 애플리케이션 로직으로 만들어진다.
- 애플리케이션 로직은 raw user-input을 message list로 만들고 LM(Language Model)에 전달함
- 보통 이러한 전달은 system message나 formatting templates를 함께 포함하기도 함

- [Prompt Templates는](https://python.langchain.com/docs/tutorials/llm_chain/#:~:text=the%20user%20input.-,Prompt%20templates,-are%20a%20concept)는 이러한 전달 과정을 도와주기 위해 디자인 되었음
- LLM에 전달할 프롬프트를 템플릿화하여 제공
    - 주요기능
        - 템플릿 문자열
        - 입력 변수 지정
        - 포맷팅 메서드 제공
        - 검증 기능 내장
    - 장점
        - 재사용성
        - 동적생성 가능
- raw-user-input을 LM에 보낼 준비가 된 데이터로 반환하여 줌
- LangChain은 해당 데이터를 조작하여 메시지로 바꿀 수 있음
    - 자연어 같은 깔끔한 응답이 나올 수 있게 됨

- [ChatPromptTempate](https://python.langchain.com/docs/tutorials/llm_chain/#:~:text=API%20Reference%3A-,ChatPromptTemplate,-Note%20that%20ChatPromptTemplate) : 프롬프트 템플릿을 관리하는 클래스
- .to_messages() : 프롬프트 템플릿 오브젝트를 메시지 오브젝트로 변환해줌
- message를 invoke함으로써 자연어 같은 깔끔한 결과를 얻게되는 것임

<br>

## IV. 추가 공부 내용
- #### to-do
    - LangChain Docs 추천 : [Conceptual Guides](https://python.langchain.com/docs/tutorials/llm_chain/#:~:text=we%27ve%20got%20detailed-,Conceptual%20Guides,-.), [Chat models](https://python.langchain.com/docs/tutorials/llm_chain/#:~:text=how%2Dto%20guides%3A-,Chat%20models,-Prompt%20templates) [Prompt Templates](https://python.langchain.com/docs/tutorials/llm_chain/#:~:text=Chat%20models-,Prompt%20templates,-And%20the%20LangSmith)
    - 개인 공부
        - 