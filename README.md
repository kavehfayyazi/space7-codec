# space7-codec

**Custom encoder/decoder for `.kaveh` file format using modified Huffman encoding**

This project implements custom compression and decompression of ASCII text using a modified Huffman encoding. The system uses a unique character representation scheme:  
- `' '` (space) represents binary `0`  
- `'7'` represents binary `1`  

The encoder generates `.kaveh` files by:
- Constructing a frequency-based binary tree
- Encoding ASCII characters into a unique variable length code
- Storing the tree and message in a single `.kaveh` file using only `' '` (space) and `'7'`

The decoder reads `.kaveh` files, reconstructs the Huffman tree, and decodes the original message.

## Features
- Lightweight tree-based encoder/decoder
- Custom binary format using only two printable characters
- File output with `.kaveh` extension
- CLI-friendly interface

## Usage
```bash
# Encode
python3 space7-codec input.txt          # Outputs: encoded.kaveh
python3 space7-codec input.txt output.kaveh

# Decode
python3 space7-codec output.kaveh       # Outputs: decoded.txt
python3 space7-codec output.kaveh decoded.txt