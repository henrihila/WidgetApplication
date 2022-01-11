from flask_restful import Resource, reqparse
from models.widget import WidgetModel


class Widget(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('number_of_parts',
                        type=int,
                        required=True,
                        help='This field cannot be blank'
                        )

    def get(self, name):
        widget = WidgetModel.find_by_name(name)
        if widget:
            return widget.json()
        return {'message', 'Widget not found'}, 400

    def post(self, name):
        if WidgetModel.find_by_name(name):
            return {'message': "An widget with name '{}' already exists".format(name)}, 400
        data = Widget.parser.parse_args()
        widget = WidgetModel(name, data['number_of_parts'])
        try:
            widget.save_to_db()
        except:
            return {'message': 'An error occurred inserting the widget'}, 500
        return widget.json(), 201

    def delete(self, name):
        widget = WidgetModel.find_by_name(name)
        if widget:
            widget.delete_from_db()
            return {'message': 'Widget deleted'}
        return {'message': 'Widget not found.'}, 404

    def put(self, name):
        data = Widget.parser.parse_args()
        widget = WidgetModel.find_by_name(name)
        if widget is None:
            widget = WidgetModel(name, data['number_of_parts'])
        else:
            widget.number_of_parts = data['number_of_parts']
        widget.save_to_db()
        return widget.json()


class WidgetList(Resource):
    def get(self):
        return list(map(lambda x: x.json(), WidgetModel.query.all()))
