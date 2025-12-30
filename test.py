from retriever import write_data, add_chunk_to_database
from data_load import load_arc_dataset

#데이터셋 로드
dataset = load_arc_dataset()
dataset.to_json('qa.jsonl')

#데이터셋 벡터 DB에 추가

