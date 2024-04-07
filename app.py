import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from lr_prediction import pred

db_username = os.environ['DB_USERNAME']
db_password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']
db_host = os.environ['DB_HOST']
db_port = os.environ['DB_PORT']
db_uri = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
print(f"Connecting db @{db_uri}")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy()
db.init_app(app)
class Team(db.Model):
    __tablename__ = "teams"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Year = db.Column(db.Integer, nullable=False)
    OBP = db.Column(db.Float, nullable=False)
    SLG = db.Column(db.Float, nullable=False)
    BA = db.Column(db.Float, nullable=False)
    G = db.Column(db.Integer, nullable=False)
    OOBP = db.Column(db.Float, nullable=False)
    OSLG = db.Column(db.Float, nullable=False)
    League_NL = db.Column(db.Integer, nullable=False)
    Playoffs_1 = db.Column(db.Integer, nullable=False)
    RD = db.Column(db.Float, nullable=True)
    def __init__(self, year, obp, slg, ba, g, oobp, oslg, league_nl, playoffs_1, rd):
        self.Year = year
        self.OBP = obp
        self.SLG = slg
        self.BA = ba
        self.G = g
        self.OOBP = oobp
        self.OSLG = oslg
        self.League_NL = league_nl
        self.Playoffs_1 = playoffs_1
        self.RD = rd

@app.route("/")
def home():
    return "Hello from my Containerized Server"

@app.route('/teams', methods=['POST'])
def add_team():
    request_data = request.get_json()
    request_data = pred(request_data)
    new_team = Team( Year= request_data['year'],
                     OBP=request_data['obp'],
                     SLG=request_data['slg'],
                     BA=request_data['ba'],
                     G=request_data['g'],
                     OOBP=request_data['oobp'],
                     OSLG=request_data['oslg'],
                     League_NL=request_data['league_nl'],
                     Playoffs_1=request_data['playoffs_1'],
                     RD = request_data('rd'))
    new_team = pred(new_team)
    db.session.add(new_team)
    db.session.commit()
    return "Team added successfully"

@app.route('/teams')
def show_teams():
    teams = Team.query.all()
    team_list = {}
    for team in teams:
        team_list[team.id] = team.Year
    return team_list

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555)