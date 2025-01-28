# 🛠️ [Build a semantic search engine](https://python.langchain.com/docs/tutorials/retrievers/)


# 🦜 LangChain Offical Docs Tutorial 2편

## 🤖 Make What?
- PDF document Search Engine


## 🎯 Goal
- Familiarize with
    - documents & document loader
    - Text Splitters
    - Embeddings
    - Vector stores and retrievers

- Dcoument Loader와 embedding, vector store의 경우 vector db 기반 검색과 다른 소스 검색을 도와준다
- [RAG](https://python.langchain.com/docs/concepts/rag/)와 같은 data 추론 모델 인터페이스에 중요함

<br>

## I. Set-up 💾
- #### Tutorial
```shell
pip install langchain-community pypdf
```

## II. Dcouments and Docmument Loaders 🧾
### [Dcoument](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html)
- 랭체인에 기본으로 포함되어 있는 추상화 클래스
- 텍스트와 메타데이터를 나태냄

- attribute
    - page_conent : 컨텐츠 문자열
    - metadata : meta 데이터 딕셔너리
        - 문서 소스에 대한 정보 포함
        - 다른 문서와의 관계를 포함함
        - Document 오브젝트가 다른 거대 문서의 청크가 될 수 도 있기 때문에
    - id(optional) : 문서 식별자

### [Dcoument Loader](https://python.langchain.com/docs/concepts/document_loaders/) 
- 다양한 데이터 소스에서 문서를 로드하게 해주는 클래스
- 다양한 파일 소스 지원
- 문서 변환
- 텍스트 임베딩 모델, 벡터 저장소 사용 가능

### [PyPDFLoader](https://python.langchain.com/docs/integrations/document_loaders/pypdfloader/)
- LangChain에서 사용가능한 PDF Loader의 한 종류로
- 상대적으로 가벼움
- PDF 파일을 로드할 때 각 페이지를 개별적인 Document 객체로 분류
- 분류된 각 객체에 첩근해 데이터를 가져 올 수 있음
- .load()함수는 데이터 소스에 접근해 데이터를 추출하고 Document 객체 리스트를 반한홤

## III. Splitting ✂️
### [text splitters](https://python.langchain.com/docs/concepts/text_splitters/)
>  정보 검색과 그에 따른 질문을 한번에 구현하면 표현히 조잡해 질 수 있음 
> Dcoument의 필요한 정보가 다른 정보에 희석되는걸 완화하는 것이 목표이다.
> 이를 도와줄 수 있는것이 text splitter임

- 텍스트 분할
- 청크 크기 조정
- overlap 설정 -> 문맥을 유지할 수 있음 (하나의 문장이 잘리는 것을 완화)

### [RecursiveCharacterTextSplitter](https://python.langchain.com/docs/how_to/recursive_text_splitter/)
- 의미있는 단위를 기반으로 재귀적으로 문서를 분할 (여러 단계에 걸쳐 분할하여 설정 청크 크기 까지)
- 청크 크기 및 중첩 설정
- 언어별 최적화 분할 지원
- add_start_index를 포함하여 청크의 시작 글자가 원본 문서의 몇번재 인덱스인지를 지정
    - 문맥 복원
    - 정확한 검색 및 데이터 분석

## IV. [Embeddings](https://python.langchain.com/docs/concepts/embedding_models/)
> Vector Search를 위한 과정

- Vector Search : 비정형화된 데이터를 검색하는 보편적인 방법, 텍스트와 관련된 수많은 벡터들을 저장하는 기법이다.
- 쿼리가 주어지면 같은 차원의 Vector로 [Embed](https://python.langchain.com/docs/concepts/embedding_models/) 벡터 유삿어 측정법(cosine 유사도 측정)을 통해 관련된 텍스트를 찾아낸다.
- LangChain은 다양한 제공사들로부터 다양한 임베딩 방법을 제공한다.

- Embedding 클래스
    - 텍스트 데이터를 벡터로 변환하는 기능을 가지고 있음
    - embed_query() 메서드를 통해 쿼리를 벡터로 변환

## V. [Vector Store](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html)
- LangChain의 벡터 저장 객체는 텍스트와 Document Object를 저장할 수 있음
- 이를 쿼리하여 다양한 유사도 측정법에 활용 할 수 있음
- 임베딩 모델들과 같이 사용되기도 함
- 몇몇 Vector Store는 써드 파티에 의해 제공되기도 하며 이를 사용하기 위해 추가적인 설정이 필요함
- 써드 파티, 로컬, 메모리 기반 벡터 저장소 등 다양한 종류가 있음


- Vector Store구현은 client, index name 등등의 정보를 제공하며 연결을 제공
- 벡터 저장소는 벡터 데이터를 저장하고 검색하는 기능을 제공하며 이를 쿼리로 전환할 수 있음
- Vector Store는 벡터 데이터 쿼리화를 위한 메서드를 제공함
    - 동기, 비동기
    - 문자열 쿼리화와 벡터 쿼리화
    - 유사도 측정값 반환여부
    - 유사도 측정과 MMR을 활용



## VI. Retriever
- Retriever는 Runnable임 / 벡터 저장소는 Runnable이 아님
- invoke, batch 메서드를 통해 쿼리를 실행할 수 있음
- 벡터 저장소, 비 벡터 저장소에 접근하여 검색이 가능함


- #### 추가

<br>


##  추가 공부 내용
- #### to-do
    
    - 개인 공부
        - 