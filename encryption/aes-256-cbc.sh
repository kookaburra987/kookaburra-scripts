# Apply AES cipher with block size 256 and mode CBC. Output will be base64 encoded.
# Syntax: aes-256-cbc.sh [-e/-d] <password> <input-file> <output-file>
if [[ $1 == "-e" ]]; then
  openssl enc -aes-256-cbc -e -a -k "$2" -in "$3" -out "$4"
elif [[ $1 == "-d" ]]; then
  openssl enc -aes-256-cbc -d -a -k "$2" -in "$3" -out "$4"
elif [[ $1 == "-h" ]]; then
  echo "Syntax: aes-256-cbc.sh [-e/-d] <password> <input-file> <output-file>"
fi