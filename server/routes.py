

from flask import request, jsonify
from models import db, Episode, Guest, Appearance

def register_routes(app):

    @app.route('/episodes')
    def get_episodes():
        return jsonify([{ "id": e.id, "date": e.date, "number": e.number } for e in Episode.query.all()])

    @app.route('/episodes/<int:id>')
    def get_episode(id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404
        return jsonify({
            "id": episode.id,
            "date": episode.date,
            "number": episode.number,
            "appearances": [
                {
                    "id": a.id,
                    "rating": a.rating,
                    "guest_id": a.guest_id,
                    "episode_id": a.episode_id,
                    "guest": {
                        "id": a.guest.id,
                        "name": a.guest.name,
                        "occupation": a.guest.occupation
                    }
                } for a in episode.appearances
            ]
        })

    @app.route('/guests')
    def get_guests():
        return jsonify([{ "id": g.id, "name": g.name, "occupation": g.occupation } for g in Guest.query.all()])

    @app.route('/appearances', methods=['POST'])
    def create_appearance():
        data = request.get_json()
        try:
            appearance = Appearance(
                rating=data['rating'],
                episode_id=data['episode_id'],
                guest_id=data['guest_id']
            )
            db.session.add(appearance)
            db.session.commit()

            return jsonify({
                "id": appearance.id,
                "rating": appearance.rating,
                "guest_id": appearance.guest_id,
                "episode_id": appearance.episode_id,
                "episode": {
                    "id": appearance.episode.id,
                    "date": appearance.episode.date,
                    "number": appearance.episode.number
                },
                "guest": {
                    "id": appearance.guest.id,
                    "name": appearance.guest.name,
                    "occupation": appearance.guest.occupation
                }
            }), 201
        except Exception as e:
            return {"errors": [str(e)]}, 400