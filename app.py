from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

@app.route('/process', methods=['GET'])
def process_items():
    data = request.json
    
    if not data or 'GroupId' not in data or 'ItemGroup' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    group_id = data['GroupId']
    item_group = data['ItemGroup']

    # Process each item in the ItemGroup
    processed_item_group = []
    for item in item_group:
        if 'ItemID' in item and 'Description' in item:
            item['PIMKEY'] = str(uuid.uuid4())
            processed_item_group.append(item)
        else:
            return jsonify({'error': 'Invalid item in ItemGroup'}), 400

    response = {
        'GroupId': group_id,
        'ItemGroup': processed_item_group
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
