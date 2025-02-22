from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Sample data for the dashboard
water_data = {
    'total': 10,
    'pending': 3,
    'unresolved': 2
}

power_data = {
    'total': 5,
    'pending': 2,
    'unresolved': 1
}

garbage_data = {
    'total': 8,
    'pending': 4,
    'unresolved': 3
}

class Dashboard(Resource):
    def get(self):
        return jsonify({
            'water': water_data,
            'power': power_data,
            'garbage': garbage_data
        })

api.add_resource(Dashboard, '/dashboard')

if __name__ == '__main__':
    app.run(debug=True)