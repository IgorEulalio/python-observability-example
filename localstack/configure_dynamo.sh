echo "creating ddb table"

echo "awslocal dynamodb create-table \
  --region sa-east-1 \
  --table-name games \
  --attribute-definitions \
    AttributeName=game_id, AttributeType=N \
  --key-schema \
    AttributeName=game_id, AttributeType=N \
  --provisioned-troughput \
    ReadCapacityUnits=1, WriteCapacityUnits=1"

awslocal dynamodb create-table \
  --region sa-east-1 \
  --table-name games \
  --attribute-definitions \
    AttributeName=game_id,AttributeType=S \
  --key-schema \
    AttributeName=game_id,KeyType=HASH \
  --provisioned-throughput \
    ReadCapacityUnits=1,WriteCapacityUnits=1

#aws --endpoint-url=http://localhost:4566  dynamodb put-item --table-name games --item file://game_item.json

#aws --endpoint-url=http://localhost:4566 dynamodb get-item --table-name games --key '{"game_id": {"N": "1"}}'

