from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

@app.route('/pim', methods=['POST'])
def process_items():
    data = request.json
    
    if not data or 'correlationid' not in data or 'match_requests' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    correlationid = data['correlationid']
    match_requests = data['match_requests']

    # Process each item in the ItemGroup
    processed_item_group = []
    for item in match_requests:
        if 'vendorname' in item and 'description' in item:
            item['PIMKEY'] = str(uuid.uuid4())
            processed_item_group.append(item)
        else:
            return jsonify({'error': 'Invalid item in ItemGroup'}), 400

    response = {
        'correlationid': correlationid,
        'ItemGroup': processed_item_group
    }

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)
