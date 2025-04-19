import csv
import json
import sys
from typing import Dict, List

def read_csv(file_path: str) -> List[Dict]:
    """CSVファイルを読み込み、データを辞書のリストとして返す"""
    mappings = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # ヘッダーをスキップ
        for row in reader:
            if len(row) >= 4:
                mapping = {
                    'method': row[0],
                    'input': row[1],
                    'output': row[2],
                    'description': row[3]
                }
                mappings.append(mapping)
    return mappings

def generate_rpc_mapping(mappings: List[Dict]) -> Dict:
    """RPCマッピングを生成する"""
    rpc_mapping = {}
    for mapping in mappings:
        rpc_mapping[mapping['method']] = {
            'input': mapping['input'],
            'output': mapping['output'],
            'description': mapping['description']
        }
    return rpc_mapping

def save_mapping(mapping: Dict, output_path: str) -> None:
    """マッピングをJSONファイルとして保存する"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, ensure_ascii=False, indent=2)

def main():
    if len(sys.argv) != 3:
        print('Usage: python main.py input.csv output.json')
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        mappings = read_csv(input_file)
        rpc_mapping = generate_rpc_mapping(mappings)
        save_mapping(rpc_mapping, output_file)
        print(f'Successfully generated RPC mapping: {output_file}')
    except Exception as e:
        print(f'Error: {str(e)}')
        sys.exit(1)

if __name__ == '__main__':
    main()