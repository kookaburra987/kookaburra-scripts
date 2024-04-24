# Script to base64 encode a file
# Syntax: base64-file.sh [-e/-d] <input-file> <output-file>
if [[ $1 == "-e" ]]; then
  openssl base64 -in "$2" -out "$3"
elif [[ $1 == "-d" ]]; then
  openssl base64 -d -in "$2" -out "$3"
elif [[ $1 == "-h" ]]; then
  echo "Syntax: base64-file.sh [-e/-d] <input-file> <output-file>"
fi
