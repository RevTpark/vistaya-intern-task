from flask_restful import reqparse, Resource
from models import SlotData, db
from flask import request, session

# Setup Parser to get collect arguments in API's
parser = reqparse.RequestParser()
parser.add_argument('items', type=list, location="json")


class InputValidatorAPI(Resource):

    def post(self):
        args = parser.parse_args()

        result = {
            "valid_entries": 0,
            "invalid_entries": 0,
            "min": None,
            "max": None,
            "average": 0,
        }

        for item in args["items"]:
            if isinstance(item, int):
                if item > 0:
                    result["valid_entries"] += 1
                    result["average"] += item

                    if not result["max"] or item > result["max"]:
                        result["max"] = item

                    if not result["min"] or item < result["min"]:
                        result["min"] = item

                else:
                    result["invalid_entries"] += 1
            else:
                result["invalid_entries"] += 1

        if result["valid_entries"]:
            result["average"] = result["average"] / result["valid_entries"]

        return result, 200


class SlotBookingAPI(Resource):

    def get(self):
        queryset = SlotData.query.all()
        result = {
            "length": len(queryset),
            "slots": []
        }
        for item in queryset:
            names = []
            if item.slot_one:
                names.append(item.slot_one)
            if item.slot_two:
                names.append(item.slot_two)

            result["slots"].append({
                "slot": item.slot_time,
                "name": names
            })

        return result, 200

    def post(self):
        data = request.get_json()
        time = data["slot"]
        name = data["name"]

        if not 0 <= time <= 23:
            return {
                "status": "Invalid Slot..."
            }, 404

        slot_data = SlotData.query.filter_by(slot_time=time).first()
        if slot_data:
            if not slot_data.slot_one:
                slot_data.slot_one = name
                result_status = "Confirmed"
                result_code = 201
                db.session.commit()

            elif not slot_data.slot_two:
                slot_data.slot_two = name
                result_status = "Confirmed"
                result_code = 201
                db.session.commit()
            else:
                result_status = f"slot full, unable to save booking for {name} in slot {time}"
                result_code = 400
        else:
            new_slot = SlotData(slot_time=time, slot_one=name)
            db.session.add(new_slot)
            db.session.commit()
            result_status = "Confirmed"
            result_code = 201

        return {
            "status": result_status
        }, result_code


class SlotCancelAPI(Resource):

    def post(self):
        data = request.get_json()
        time = data["slot"]
        name = data["name"]
        slot_info = SlotData.query.filter_by(slot_time=time).first()
        if slot_info:
            if slot_info.slot_one == name:
                result_status = f"canceled booking for {name} in slot {time}"
                result_code = 200
                slot_info.slot_one = None
                db.session.commit()
            elif slot_info.slot_two == name:
                result_status = f"canceled booking for {name} in slot {time}"
                result_code = 200
                slot_info.slot_two = None
                db.session.commit()
            else:
                result_status = f"no booking for the name {name} in slot {time}"
                result_code = 404
        else:
            result_status = f"no booking for the name {name} in slot {time}"
            result_code = 404

        return {
            "status": result_status
        }, result_code


class SquareCheck(Resource):

    def post(self):
        if session.get("Found", False):
            p1, p2, p3, p4 = session["Found"]
            return {
                "status": f"Success {p1} {p2} {p3} {p4}"
            }, 200
        data = request.get_json()
        x, y = data["x"], data["y"]
        if not session.get("points"):
            session["points"] = []

        session["points"] += [(x, y)]
        points = session["points"]
        grid = {p: 1 for p in points}
        while len(points) >= 4:
            p1 = points.pop()
            for p2 in points:
                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]
                for delta in [(dy, -dx), (-dy, dx)]:
                    p3 = (p2[0] + delta[0], p2[1] + delta[1])
                    if grid.get(p3, False):
                        p4 = (p3[0] - dx, p3[1] - dy)
                        if grid.get(p4, False):
                            session["Found"] = [p1, p2, p3, p4]
                            return {
                                "status": f"Success {p1} {p2} {p3} {p4}"
                            }, 200
        # session["points"].pop(0)
        return {
            "status": "accepted"
               }, 200
