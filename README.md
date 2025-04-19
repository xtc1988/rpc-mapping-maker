# RPC Mapping Maker

RPCマッピングツールは、CSVファイルに記載されたRPC名とクラス名のマッピングを元に、
指定されたディレクトリ内のJavaScriptファイルを検索し、RPC名が使用されているファイルを特定して
新しいマッピングファイルを生成するツールです。

## 必要要件

- Python 3.6以上

## 使用方法

```bash
python rpc_mapper.py <入力CSVファイルパス> <JS検索パス> [--output 出力ファイル名]
```

### 引数

- `入力CSVファイルパス`: RPC名とクラス名のマッピングが記載されたCSVファイルのパス
  - CSVには `rpc_name` と `rpc_class` の2つのカラムが必要です
- `JS検索パス`: JavaScriptファイルを検索するディレクトリパス
- `--output`: 出力ファイル名（省略時は `rpc_mapping.csv`）

### 入力CSVファイル形式

```csv
rpc_name,rpc_class
example_rpc,ExampleClass
another_rpc,AnotherClass
```

### 出力CSVファイル形式

```csv
rpc_name,rpc_class,js_file
example_rpc,ExampleClass,path/to/file1.js
another_rpc,AnotherClass,path/to/file2.js
```

## 使用例

```bash
python rpc_mapper.py input_mapping.csv /path/to/js/files --output result_mapping.csv
``` 